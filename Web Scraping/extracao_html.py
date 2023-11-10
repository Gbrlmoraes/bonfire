# Imports necessários
import requests

# Função para extrair HTML de sites que precisam de header na requisição
def super_get(link, log = False):
    try:
        # Definindo parâmetros 
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }

        # Fazendo requisição para a página
        resposta = requests.get(link, headers = headers).content

        if log:
            print('HTML coletado com sucesso!\n')

        return resposta
    
    except Exception as e:
        print('Falha na extração:', e)