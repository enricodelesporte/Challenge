from core.consultaService import consultaService
from core.menu import Menus
from core.agenda import Agenda

def main():
    while True:
        menu = Menus()
        consulta = consultaService()
        agenda = Agenda()

        menu.menu_principal()

        consulta.agendarConsulta()
        
        agenda.exibir_agenda()
        

        
main()