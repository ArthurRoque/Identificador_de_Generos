from requests import get
from json import loads

def genero(api_key, nome):
    url_base = 'https://api.brasil.io'
    nome = nome.upper().replace(" ","")

    link = f'{url_base}/v1/dataset/genero-nomes/nomes/data/?first_name={nome}'
    response = get(link, headers={"Authorization": f"Token {api_key}"})

    if response.status_code == 200:
        pass
    else:
        print('Erro')
        print(response)

    response = loads(response.content)
  
    try:
      response = response.get('results')
      response = response[0]
      genero = response.get('classification')
      return genero
    except:
      print('Nome não encontrado')
