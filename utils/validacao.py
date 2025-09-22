from models.pacienteModel import Paciente
from models.consultaModel import Consulta

import datetime
from datetime import datetime
import re



from dataBase.crud.pacienteCRUD import pacienteCRUD
from dataBase.crud.consultaCRUD import consultaCRUD
from dataBase.conexao.db_manager import DBManager

class Validacao:
    conn, cursor = DBManager.conectar()
    
    def validar_criar_conta_senha(self, senha):
        while not senha or len(senha) <= 5:
            if not senha:
                print("Senha inválida. A senha não pode estar vazia.")
            elif len(senha) <= 5:
                print("Senha fraca. A senha deve ter pelo menos 6 caracteres.")
                senha = input("Digite a senha novamente: ")
        return senha

    def validar_criar_conta_cpf(self, cpf):
        while not cpf or len(cpf) != 11 or not cpf.isdigit():
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif len(cpf) != 11:
                print("CPF inválido. O CPF deve ter 11 dígitos.")
                cpf = input("Digite o CPF novamente: ")
        return cpf
    
    def validar_criar_conta_idade(self, idade):
        while not idade or not idade.isdigit() or int(idade) <= 16 or int(idade) >= 120:
            if not idade:
                print("Idade inválida. A idade não pode estar vazia.")
            elif not idade.isdigit():
                print("Idade inválida. A idade deve ser um número.")
            elif int(idade) <= 16 or int(idade) >= 120:
                print("Idade inválida. A idade deve ser maior que 15 anos.")
            idade = input("Digite a idade novamente: ")
        return idade
    
    def validar_nome(self, nome):
        while not nome or len(nome) < 3:
            print("Nome inválido. O nome deve ter pelo menos 2 caracteres.")
            nome = input("Digite o nome novamente: ")
        return nome

    def validar_email(self, email):
        while not email or "@" not in email or "." not in email:
            print("Email inválido.")
            email = input("Digite o email novamente: ")
        return email

    def validar_cpf(self, cpf):
        while not cpf or len(cpf) != 11 or not cpf.isdigit():
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif len(cpf) != 11:
                print("CPF inválido. O CPF deve ter 11 dígitos.")
            elif not cpf.isdigit():
                print("CPF inválido. O CPF deve conter apenas dígitos.")
            cpf = input("Digite o CPF novamente: ")
        return cpf

    def validar_login_cpf(self, cpf):
        pacientes = pacienteCRUD.listarPacientes()

        while not cpf or not any(p.cpf == cpf for p in pacientes):
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif not any(p.cpf == cpf for p in pacientes):
                print("CPF inválido. O CPF não corresponde a nenhum paciente cadastrado.")
            cpf = input("Digite o CPF novamente: ")
        return cpf
    
    def validar_login_senha(self, senha):
        pacientes = pacienteCRUD.listarPacientes()

        while not senha or len(senha) <= 7 or not any(p.senha == senha for p in pacientes):
            if not senha:
                print("Senha inválida. A senha não pode estar vazia.")
            elif len(senha) <= 7:
                print("Senha fraca. A senha deve ter pelo menos 8 caracteres.")
            elif not any(p.senha == senha for p in pacientes):
                print("Senha incorreta. Tente novamente.")
        return senha

    def validar_usuario(self, nome_digitado: str):
        paciente_crud = pacienteCRUD(conexao= DBManager.conexao)
        pacientes = paciente_crud.listarPacientes()

        nome_digitado = (nome_digitado or "").strip().lower()
        if not nome_digitado:
            print("Nome vazio. Digite um nome válido.")
            return None

        for p in pacientes:
            if hasattr(p, "nome"):
                if (p.nome or "").strip().lower() == nome_digitado:
                    return p

            else:
                try:
                    nome_row = p[1]
                except Exception:
                    nome_row = None

                if isinstance(nome_row, str) and nome_row.strip().lower() == nome_digitado:
                    return p

        return None

    def validar_consulta(self, consulta: Consulta):
        while consulta not in consultaCRUD.listarConsultas():
            print("Consulta não encontrada. Verifique se foi marcada corretamente.")
            return False
        return consulta

    def validar_especialidade(self, especialidade):
        while not especialidade:
            print("Especialidade inválida. A especialidade não pode estar vazia.")
            especialidade = input("Digite a especialidade novamente: ")
        return especialidade

    def validar_data(self, data):
        data = data.strip()
        parts = data.split('/')
        if len(parts) == 2:
            ano = datetime.now().year
            data = f"{data}/{ano}"

        try:
            dt = datetime.strptime(data, "%d/%m/%Y").date()
            return dt
        except ValueError:
            print("Data inválida! Use DD/MM ou DD/MM/YYYY.")
            return input("Digite a data (DD/MM ou DD/MM/YYYY): ")

    def validar_hora(hora):
        hora = (hora or "").strip()
        while True:
            try:
                t = datetime.strptime(hora, "%H:%M")
                return t.strftime("%H:%M")
            except ValueError:
                print("Hora inválida! Use o formato HH:MM (ex: 14:30).")
                hora = input("Digite o horário novamente: ").strip()

    def validar_problema(self, problema):
        while not problema or len(problema) <= 100:
            if not problema:
                print("Esse campo não pode estar vazio!")
                problema = input("Tente novamente. Qual probelam deseja relatar:")
            else:
                print("O relato deve conter no minimo 100 caracteres!")
                problema = input("Tente novamente. Qual probelam deseja relatar:")
                
        return problema