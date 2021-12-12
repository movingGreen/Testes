from bs4 import BeautifulSoup
import requests

#Pega o html da primeira pagina e inicializa em um objeto do beautifulsoup
html_texto = requests.get('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss').text
pagina_html = BeautifulSoup(html_texto, 'lxml')

#Salva em uma variavel separada a tag <a> e depois guarda o link para a segunda pagina 
link_em_html = pagina_html.find('a', class_ ='alert-link internal-link')
href_para_pdf = str(link_em_html['href'])

#Pega o html da segunda pagina e inicializa em um objeto
html_pagina_pdf = requests.get(href_para_pdf).text
pagina_pdf = BeautifulSoup(html_pagina_pdf, 'lxml')

#Repete o processo de pegar um link do html e guarda o link do pdf
html_link_pdf = pagina_pdf.find('a', class_ ='btn btn-primary btn-sm center-block internal-link')
html_link_pdf_href = str(html_link_pdf['href'])



print(html_link_pdf_href)