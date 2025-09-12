from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD
from utils import validacao as val
from dataBase.conexao.db_manager import DBManager


class consultaService:
    def __init__(self):
        conn, cursor = DBManager.conectar()
        
        self.consultaCRUD = consultaCRUD(conn)
        self.consultaCRUD.criarTabelaConsulta()

    def exibir_consulta(self):
        print("---- Consultas ----")
    
        headers = ["Data", "Hora", "Especialidade"]
        col_widths = [12, 8, 20]

        header_line = "".join(header.ljust(width) for header, width in zip(headers, col_widths))
        print(header_line)
        print("-" * sum(col_widths))

        for consulta in self.listarConsultas():
            linha = f"{str(consulta.data).ljust(col_widths[1])}" \
                    f"{str(consulta.hora).ljust(col_widths[2])}" \
                    f"{str(consulta.especialidade).ljust(col_widths[3])}"
            print(linha)
            
        return

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
        print("(2) Ver minha consultas.")
        print("(3) Voltar ao menu principal")

        opcao = int(input())

        if opcao == 1:
            especialidade = vali.validar_especialidade(input("Qual a especialidade médica: "))
            data = vali.validar_data(input("Qual a data da consulta: "))
            hora = vali.validar_hora(input("Qual o horário da consulta: "))

            nova_consulta = Consulta(
                paciente_id= paciente.id,
                especialidade=especialidade,
                data=data,
                hora=hora
            )

            consulta = consultaService()
            consulta.consultaCRUD.criarConsulta(nova_consulta)

            print("Consulta agendada com sucesso!")
            return
        elif opcao == 2:
            self.exibir_consulta()
            return
        elif opcao == 3:
            return
        
        else:
            print("Opção inválida. Digite um número de 1 a 3 para poder continuar")


    def listarConsultas(self):
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self, idConsulta):
        self.consultaCRUD.deletarConsulta(idConsulta)
        print("Consulta cancelada com sucesso!")