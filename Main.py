import core.agenda
import core.cadastro
import core.consultaService
from core.menu import Menus
import core.suporte
import dataBase.conexao.oracleConexao
import dataBase.crud.consultaCRUD
import dataBase.crud.pacienteCRUD
import dataBase.crud.suporteCRUD
import models.agendaModel
import models.consultaModel
import models.pacienteModel
import models.suporteModel
from utils.validacao import Validacao

def main():
    while True:
        menuTeste = Menus()
        val = Validacao()

        menuTeste.menu_principal()
        val.escolha_menu()
        
main()