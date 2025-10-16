import requests

class ViaCEP:
    @staticmethod
    def buscar_cep(cep):
        cep = cep.strip().replace("-", "")
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Deve conter 8 dígitos numéricos.")
            return None
        
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code != 200:
            print("Erro ao consultar o ViaCEP.")
            return None
        
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return None
        
        return dados
