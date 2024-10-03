# Importa as bibliotecas necessárias: requests para fazer requisições HTTP, BeautifulSoup para analisar o HTML
#da página, e pandas para organizar os dados em um DataFrame e exportá-los para um arquivo CSV.

import requests
from bs4 import BeautifulSoup
import pandas as pd

#Armazena a URL da página da qual os dados serão extraídos.
url = "https://www.psicologianapratica.com/material-gratuito"

#Faz uma requisição GET para a URL definida e armazena a resposta na variável request.
request = requests.get(url)

#Converte o conteúdo da resposta HTTP em um objeto BeautifulSoup, o que facilita a busca por elementos no HTML.
soup = BeautifulSoup(request.content, 'html.parser')

#Utiliza o BeautifulSoup para buscar todos os elementos da página que possuem as seguintes classes CSS:
#   <h3> com classes específicas (títulos).
#   <p> com classes específicas (descrições).
#   <a> com classes específicas (links de download).
#   <img> com classes específicas (imagens).
titulo = soup.find_all('h3',class_='h4 card-title text-center border-bottom pb-1 mb-2')
descricao = soup.find_all('p',class_='card-text text-center')
link_download = soup.find_all('a',class_='mt-2 btn w-100 fw-bold')
imagem=soup.find_all('img', class_='card-img-top img-thumbnail w-100')


#Inicializa uma lista vazia chamada titulos. Depois, percorre cada elemento da lista titulo (obtido anteriormente)
# e extrai o texto (removendo quebras de linha), adicionando à lista titulos.
titulos=[]
for i in titulo:
    titulos.append(i.text.strip().replace('\n', '').replace('\r', '').strip())

#Semelhante ao processamento dos títulos, mas agora para as descrições. Os textos são extraídos da lista descricao
# e armazenados em descricoes.
descricoes=[]
for desc in descricao:
    descricoes.append(desc.text.strip().replace('\n', '').replace('\r', '').strip())

#Inicializa uma lista links. Para cada link encontrado, adiciona a URL base à parte específica do link extraído (href),
# criando a URL completa para o download.
links=[]
for link in link_download:
    links.append(url + link.get('href'))

#Inicializa uma lista imgs. Para cada elemento de imagem encontrado, extrai o valor da propriedade src
# (que contém o link da imagem) e o adiciona à lista.
imgs=[]
for img in imagem:
    imgs.append(img.get('src'))


#Cria um DataFrame usando o pandas, onde as colunas são 'titulo', 'descricao', 'link' e 'img',
# e os dados vêm das listas processadas anteriormente.
df = pd.DataFrame({
    'titulo': titulos,
    'descricao': descricoes,
    'link': links,
    'img': imgs
})

#Exporta o DataFrame para um arquivo CSV no diretório docs, com o nome dataset.csv. O parâmetro
# index=False garante que o índice (numeração das linhas) não será incluído no arquivo CSV.
df.to_csv('docs/scrapingconteudosgratuitos.csv', index=False)


