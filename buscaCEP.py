# Importando a biblioteca "urllib" que serve para solicitações de dados na web e manipulção de cookies
from urllib.request import urlopen
# Importando a biblioteca "BeautifulSoup" que não é padrão do python e é utilizada para buscar informações em uma página HTML
from bs4 import BeautifulSoup
# Importando biblioteca para ler Json
import json
# pegando as informações do site
html = urlopen("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm")

# pegando o conteudo do site e passando para o objeto "soup"
soup = BeautifulSoup(html, "html.parser")
# pegando tudo que está sendo solicitado no texto do HTML e armazenando na tag "tag"
uf = soup.findAll(text=("AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"))

# loop na variável "uf" e armazenando o resultado em "u"
for u in uf:
    print(u)

    # Transformando o objeto "u" em string
    infoUF = str(u)
    # pegando as informações da nova url e acrescentando a variável "uf"
    url = ("https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/carrega-faixa-cep-uf-localidade.php?uf=" + infoUF)

    # armazenando as informações novas com a variável
    htmlUF = urlopen(url)

    # pegando tudo que está dentro do site e colocando no objeto "soupUf"
    soupUF = BeautifulSoup(htmlUF, "html.parser")

    #puxando as informações em Json do site e amazenado na variável
    site_json = json.loads(soupUF.text)

    # fazendo um print do 'faixasCep' dentro de um loop do Json pegado a parte dos 'dados' se for da 'faixasCep'
    print([d.get('faixasCep') for d in site_json['dados'] if d.get('faixasCep')])