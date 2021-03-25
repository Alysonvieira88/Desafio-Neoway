<h1 align="center">Desafio de Busca CEP no Site dos Correios</h1>

<p align="center">Saudações viajantes!!</br> Neste projeto iremos nos aventurar em um desafio nunca feito por mim sobre uma busca de dados usando Web Scraping em Python no Site dos correios. O objetivo do projeto é buscar o maximo de Unidades Federativas e suas faixas de CEP🚀.</p>
</br>
</br>
<h2 align="center">🔨 Construção do projeto 🔨</h2>

<p align="center">Confeso que no projeto eu desafiei meus conhecimentos com algo totalmente do zero e nunca visto por mim, achei imprecionante a quantidade de informações e códigos que podem ser feitos com o famoso Web Scraping.</br></br>Foram longas 22 horas desenvolvendo e buscando informações para a melhor forma de entregar o produto. Inicialmente eu comprei um curso na Udemy de 12 horas sobre Web Scraping em Python onde gerou um <a href="https://www.udemy.com/certificate/UC-f508f580-298c-469b-87f6-dd7c467fb6d6/">curriculo</a> ao concluir o curso, além disso passei por muitas pesquisas no google e examinação de códigos em HTML. Mostrarei a seguir passo a passo do que foi feito</p>
</br>

<h3 align="center">⚒️ BUILTWITH ⚒️</h3>
	   
<p align="center">Bom, o meu primeiro passo foi instalar a biblioteca "builtwith" para verificar as tecnologias utilizadas no site dos correios, ele analisa a URL informada e em seguida retornará todas as tecnologias utilizadas pelo site. Instalei a biblioteca utilizando um comando pelo prompt de comando ("pip install builtwith") e importei para o Python utilizando o ("import builtwith"), após isso eu utilizei o método paps("builtwith.parse('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')") onde ele traz as tecnologias.</p>
</br>

<h3 align="center">⚒️ PYTHON WHOIS ⚒️</h3>
	   
<p align="center">Meu segundo passo foi utilizar a biblioteca Python Whois que serve para identificação de propriedades do site. Instalei também pelo prompt utilizando o comando ("pip instal python-whois") e importei também utilizando o prompt de comando("import whois") e imprimi o resultado dentro do python utilizando o comando (whois.whois(‘buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')</p>
</br>

<h3 align="center">⚒️ URLLIB E BEAUTIFULSOUP⚒️</h3>
	   
<p align="center">Urllib é uma biblioteca padrão do python e contem funções para solicitação de dados web e manipulação de cookies. Dentro dessa biblioteca eu utilizei a função ("urlopen") que serve para ler um objeto remoto por meio de uma rede e ler esse objeto. Esse objeto pode ser arquivos HTML, arquivos de imagens ou qualquer outro fluxo de arquivos. Importei para o Python utilizando ("from urllib.request import urlopen")e abri as informações do site com("urlopen("https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/index.php")"), em seguida utilizei a biblioteca BeauifulSoup que não é padrão do Python e é utilizada para buscar informações em uma página HTML. Baixei ela manualmente no site ("https://www.crummy.com/software/BeautifulSoup/bs4/download/4.9/beautifulsoup4-4.9.0.tar.gz") e instalei pelo prompt de comando utilizando o ("pip install beautifulsoup4") e importei ela dentro do Python utilizando ("from bs4 import BeautifulSoup")</p>

</br>
</br>
<h4 align="center"> 
	🚧  Em construção...  🚧
</h4>

### Conquistas

- [x] Busca de informações no site.
- [x] Busca de todas UFs no site.
- [ ] Busca da faixa de CEP de todos UFs.
- [ ] Colocar os dados em JSON.

Redes Sociais
------------ |
<a href="https://www.instagram.com/alysonvieira88/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
<a href="https://www.linkedin.com/in/alyson-mendon%C3%A7a-vieira-330551181/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />

