# 📌 Estudo de Viabilidade | Web Scraping do Site Psicologia Na Prática

Este projeto realiza a coleta automatizada de informações do site [Psicologia Na Prática](https://www.psicologianapratica.com/material-gratuito). As informações extraídas incluem o título do material, descrição, imagem e link para download.

## **🏷️ Nota** 
Nesta implementacao utilizamos o python em sua versao 3.10.4, a biblioteca python BeautifulSoup em sua versão 4.12.2 ela é utilizada para realizar a raspagem de dados (web scraping), biblioteca python NLTK na versão 3.8.1 para o processo do pré-processamento com a tokenização, utilizado o dicionario [LIWC Portugues](http://143.107.183.175:21380/portlex/index.php/pt/projetos/liwc), também utilizado a Interface de Programação de Aplicação (API) GPT-3.5-Turbo para realizar a analise, identificação e listagem das expressões desejadas, por ultimo, utilizado a biblioteca Requests 2.31.0 para realizar a requisiçao nos sites obtendo o "Hypertext Transfer Protocol" (HTTP). O desenvolvimento foi realizado em uma máquina com sistema operacional de 64 bit- Windows 10 Home.

## **📝 Requisitos/Instalação ⚙️** 

▶️ **Python 3.10.4:** Download no site oficial do Python
(https://www.python.org).

▶️ **Biblioteca Beautiful Soup 4.12.2:** Utilizada para extrair e manipular dados de arquivos HTML e XML. [Documentação do BeautifulSoup](https://pypi.org/project/beautifulsoup4/).

Para a instalação da biblioteca é necessário utilizar o gerenciador de pacotes 'pip'. Abra o terminal ou prompt de comando e execute o seguinte comando: 
```terminal
pip install beautifulsoup4==4.12.2
```

▶️ **Biblioteca Requests 2.31.0:** Usada para fazer requisições HTTP. [Documentação do requests](https://docs.python-requests.org/) 
    Para a instalação da biblioteca é necessário utilizar o gerenciador de pacotes 'pip'. Abra o terminal ou prompt de comando e execute o seguinte comando: 
```terminal
pip install requests==2.31.0
```
▶️ **Biblioteca Pandas 2.1.2:** Para manipulação e análise de dados em formato tabular. [Documentação do Pandas](https://pandas.pydata.org/)
    Para a instalação da biblioteca é necessário utilizar o gerenciador de pacotes 'pip'. Abra o terminal ou prompt de comando e execute o seguinte comando: 
```terminal
pip install pandas==2.1.2
```

## 🔧🎲 Processo de Extração de Dados

O processo de extração de dados segue os passos descritos abaixo:

1. 🔗 Definir a URL da página a ser acessada:
   ```python
   url = "https://www.psicologianapratica.com/material-gratuito"
   ```
2. 📨 Fazer uma requisição HTTP GET para a URL definida:
  ```python
      request = requests.get(url)
  ```
3. 📦 Converter o conteúdo da resposta em um objeto BeautifulSoup para facilitar a busca por elementos HTML:
   ```python
   soup = BeautifulSoup(request.content, 'html.parser')
   ```
   
4. 🔎 Buscar os elementos da página correspondentes ao título, descrição, links e imagens:
   ```python
   titulo = soup.find_all('h3', class_='h4 card-title text-center border-bottom pb-1 mb-2')
    descricao = soup.find_all('p', class_='card-text text-center')
    link_download = soup.find_all('a', class_='mt-2 btn w-100 fw-bold')
    imagem = soup.find_all('img', class_='card-img-top img-thumbnail w-100')
    ```
5. 🔠 Extrair os textos dos títulos e descrições, criando listas com os dados:
   ```python
   titulos = [i.text.strip().replace('\n', '').replace('\r', '').strip() for i in titulo]
    descricoes = [desc.text.strip().replace('\n', '').replace('\r', '').strip() for desc in descricao]
    ```
6. 🔗 Criar a URL completa dos links de download:
   ```python
   links = [url + link.get('href') for link in link_download]
    ```
7. 🖼️ Extrair o link das imagens:
   ```python
   imgs = [img.get('src') for img in imagem]
    ```
   
## 🎲📅 Armazenamento dos Dados 
   
8. 📄 Criar um DataFrame usando pandas com os dados extraídos:
     ```python
   df = pd.DataFrame({
    'titulo': titulos,
    'descricao': descricoes,
    'link': links,
    'img': imgs
    })
    ```
9. 🗂️ Exportar o DataFrame para um arquivo CSV:
    ```python
   df.to_csv('docs/scrapingconteudosgratuitos.csv', index=False)
    ```
