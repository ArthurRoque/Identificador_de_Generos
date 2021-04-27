# Identificador_de_Generos
Python script que identifica o gênero de um nome brasileiro através do consumo da API de gêneros Brasil.io.

O script se resume a uma simples função python que recebe um nome brasileiro e retorna "F" se o nome for feminino e "M" se o nome for masculino. Ele faz isso por meio do consumo da API:https://brasil.io/dataset/genero-nomes/nomes/. A própria API retorna qual gênero mais registrou o nome solicitado. 

Simples exemplo de uso:

[![Capturar.png](https://www.imagemhost.com.br/images/2021/04/27/Capturar.png)](https://www.imagemhost.com.br/image/2rcHMy)

[![Output.png](https://www.imagemhost.com.br/images/2021/04/27/Output.png)](https://www.imagemhost.com.br/image/2r1lOq)

Caso o nome seja neuro como "Dominique", será retornado o gênero que mais registrou o nome no Brasil (apenas "M" ou "F"). 

# Obtendo a Api key

* Crie uma conta no site Brasil.io: https://brasil.io/auth/entrar/. 

* Se direcione para: https://brasil.io/auth/tokens-api/ e clique em "CRIAR NOVA CHAVE DE API"
