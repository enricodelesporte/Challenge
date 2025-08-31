import core.agenda
import core.cadastro
import core.consultaService
import core.suporte
import dataBase.conexao.oracleConexao
import dataBase.crud.consultaCRUD
import dataBase.crud.pacienteCRUD
import dataBase.crud.suporteCRUD
import models.agendaModel
import models.consultaModel
import models.pacienteModel
import models.suporteModel
import utils.validacao

def main():
    while True:
        menu = core.menu.Menus().menu_principal(opcao)
        opcao = utils.validacao.Validacao().escolha_menu(opcao)
        if opcao == '1':
            core.cadastro.cadastrarPaciente()
        elif opcao == '2':
            core.consultaService.marcarConsulta()
        elif opcao == '3':
            core.agenda.verAgenda()
        elif opcao == '4':
            core.suporte.suporte()
        elif opcao == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Obrigado por contar o Hospital das Clínicas, espero te ver em breve!!")

main()