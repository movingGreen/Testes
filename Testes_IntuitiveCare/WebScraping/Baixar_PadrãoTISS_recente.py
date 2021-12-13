from bs4 import BeautifulSoup
import requests

#Pega o html da primeira pagina e inicializa em um objeto do beautifulsoup
html_texto_pg1 = requests.get('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss').text
objeto_html_pg1 = BeautifulSoup(html_texto_pg1, 'lxml')

#Salva em uma variavel separada a tag <a> e depois guarda o link para a segunda pagina 
html_link_pg2 = objeto_html_pg1.find('a', class_ ='alert-link internal-link')
link_pg2 = str(html_link_pg2['href'])

#Pega o html da segunda pagina e inicializa em um objeto
html_pg2 = requests.get(link_pg2).text
objeto_html_pg2 = BeautifulSoup(html_pg2, 'lxml')

#Repete o processo de pegar um link do html e guarda o link do pdf
html_link_pdf = objeto_html_pg2.find('a', class_ ='btn btn-primary btn-sm center-block internal-link')
link_pdf = str(html_link_pdf['href'])

#Faz o download do pdf e salva ele com o nome que está na url
dados_pdf = requests.get(link_pdf, allow_redirects=True)
if link_pdf.find('/'): nome_pdf = link_pdf.rsplit('/', 1)[1]
with open(nome_pdf, 'wb') as pdf:
    pdf.write(dados_pdf.content)

print(f'O pdf do Padrão TISS mais recente é: {nome_pdf}')
