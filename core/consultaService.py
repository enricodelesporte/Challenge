from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD
from utils import validacao as val
from dataBase.conexao.db_manager import DBManager
from dataBase.crud.pacienteCRUD import pacienteCRUD

from datetime import datetime, time
import re

class consultaService:
    def __init__(self):
        conn, cursor = DBManager.conectar()
        
        self.consultaCRUD = consultaCRUD(conn)
        self.consultaCRUD.criarTabelaConsulta()

    def _formatar_hora(hora_raw):
        if not hora_raw:
            return ""

        if isinstance(hora_raw, (datetime, time)):
            return hora_raw.strftime("%H:%M")

        s = str(hora_raw).strip()

        match = re.search(r'([01]?\d|2[0-3]):([0-5]\d)', s)
        if match:
            return match.group(0)

        return s

    def exibir_consulta(self):
        vali = val.Validacao()

        paciente_crud = pacienteCRUD(conexao=DBManager.conexao)
        pacientes = paciente_crud.listarPacientes()

        nome_digitado = input("Digite seu nome para ver suas consultas: ").strip().lower()
        if not nome_digitado:
            print("Nome vazio. Digite um nome válido.")
            return

        paciente_encontrado = None
        for p in pacientes:
            if hasattr(p, "nome") and (p.nome or "").strip().lower() == nome_digitado:
                paciente_encontrado = p
                break

        if not paciente_encontrado:
            print("Paciente não encontrado.")
            return

        print("---- Consultas ----")
        headers = ["Data", "Hora", "Especialidade", "ID"]
        col_widths = [12, 8, 20, 12]

        header_line = "".join(header.ljust(width) for header, width in zip(headers, col_widths))
        print(header_line)
        print("-" * sum(col_widths))

        consultas = self.listarConsultas()
        encontrou = False
        for consulta in consultas:
            if consulta.paciente_id == paciente_encontrado.id:
                hora_str = consultaCRUD.normalizar_hora_banco(consulta.hora)

                linha = (
                    f"{str(consulta.data).ljust(col_widths[0])}"
                    f"{hora_str.ljust(col_widths[1])}"
                    f"{str(consulta.especialidade).ljust(col_widths[2])}"
                    f"{str(consulta.id).ljust(col_widths[3])}"
                )
                print(linha)
                encontrou = True

        if not encontrou:
            print("Nenhuma consulta encontrada para este paciente.")

    def agendarConsulta(self):
        vali = val.Validacao()

        print("----Menu de Consulta----")
        print("Qual seu nome:")
        paciente = vali.validar_usuario(input())

        if paciente is None:
            print("Paciente não cadastrado. Voltando ao menu principal...")
            return 
        
        print("Selecione uma opção para prosseguir:")
        print("(1) Marcar consulta.")
        print("(2) Ver minha consulta.")
        print("(3) Desmarcar consulta.")
        print("(4) Remarcar minha consulta.")
        print("(5) Voltar ao menu principal")

        opcao = int(input())

        if opcao == 1:
            especialidade = vali.validar_especialidade(input("Qual a especialidade médica: "))
            data = vali.validar_data(input("Qual a data da consulta: "))
            hora = vali.validar_hora(input("Qual o horário da consulta: "))

            nova_consulta = Consulta(
                paciente_id= paciente.id,
                especialidade=especialidade,
                data=data,
                hora=hora,
                id= None
            )

            consulta = consultaService()
            consulta.consultaCRUD.criarConsulta(nova_consulta)

            print("Consulta agendada com sucesso!")
            return 
        elif opcao == 2:
            self.exibir_consulta()
            return
        elif opcao == 3:
            self.cancelarConsulta()
            return
        elif opcao == 4:
            self.remarcarConsulta()
            return
        
        else:
            print("Opção inválida. Digite um número de 1 a 5 para poder continuar")


    def listarConsultas(self):
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self):
        vali = val.Validacao()
        print("Qual seu CPF: ")
        cpf_paciente = vali.validar_cpf(input())

        while cpf_paciente is None:
            print("CPF inválido. Digite novamente: ")
            cpf_paciente = vali.validar_cpf(input())

        consulta_crud = consultaCRUD(conexao=DBManager.conexao)
        consultas = consulta_crud.listarConsultas()

        id_digitado = input("Digite o ID da consulta que deseja desmarcar: ").strip()

        if not id_digitado.isdigit():
            print("ID inválido. Digite um número válido.")
            return

        id_digitado = int(id_digitado)

        id_encontrado = None
        for consulta in consultas:
            if consulta.id == id_digitado:
                id_encontrado = id_digitado
                break

        if not id_encontrado:
            print("ID não encontrado.")
            return

        consulta_crud.deletarConsulta(id_encontrado)
        print("Consulta desmarcada com sucesso!")

    def remarcarConsulta(self):
        vali = val.Validacao()
        print("Qual seu CPF: ")
        cpf_paciente = vali.validar_cpf(input())

        while cpf_paciente is None:
            print("CPF inválido. Digite novamente: ")
            cpf_paciente = vali.validar_cpf(input())

        consulta_crud = consultaCRUD(conexao=DBManager.conexao)
        consultas = consulta_crud.listarConsultas()

        id_digitado = int(input("Digite o ID da consulta que deseja remarcar: "))

        if not isinstance(id_digitado, int):
            print("ID inválido. Digite um número válido.")
            return

        id_encontrado = None
        for consulta in consultas:
            if consulta.id == id_digitado:
                id_encontrado = id_digitado
                break

        if not id_encontrado:
            print("ID não encontrado.")
            return

        nova_data = vali.validar_data(input("Qual a nova data da consulta: "))
        nova_hora = vali.validar_hora(input("Qual o novo horário da consulta: "))

        consulta_crud.atualizarConsulta(id_encontrado, nova_data, nova_hora)
        print("Consulta remarcada com sucesso!")