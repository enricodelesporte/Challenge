from core.consultaService import consultaService
from core.cadastro import Cadastro as cad
from core.consultaService import consultaService as cons
from core.suporte import Suporte as sup

def main():
    while True:
        consulta = consultaService()

        while True:
            print("----Menu Principal----")
            print("Selecione uma opção para prosseguir:")
            print("(1) Fazer o cadastro.")
            print("(2) Marcar consulta.")
            print("(4) Falar com o suporte.")
            print("(5) Para sair.")

            opcao = input()

            if (not opcao.isdigit() or int(opcao) not in range(1, 5)):
                print("Opção inválida. Digite um número de 1 a 4 para poder continuar.")
                continue

            opcao = int(opcao)

            if (opcao == 1):
                cad.fazer_cadastro()

            elif (opcao == 2):
                consulta.agendarConsulta()
                
            elif (opcao == 3):
                sup.registrar_suporte()

            elif (opcao == 4):
                print("Obrigado por contar o Hospital das Clínicas, espero te ver em breve!!")
                return False

            consulta.agendarConsulta()
        
        

        
main()