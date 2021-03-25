<h1 align="center">Desafio de Busca CEP no Site dos Correios</h1>

<p align="center">Saudações viajantes!!</br> Neste projeto iremos nos aventurar em um desafio nunca feito por mim sobre uma busca de dados usando Web Scraping em Python no Site dos correios. O objetivo do projeto é buscar o maximo de Unidades Federativas e suas faixas de CEP🚀.</p>
</br>
</br>
<h2 align="center">🔨 Construção do projeto 🔨</h2>

<p align="center">Confeso que no projeto eu desafiei meus conhecimentos com algo totalmente do zero e nunca visto por mim, achei imprecionante a quantidade de informações e códigos que podem ser feitos com o famoso Web Scraping.</br></br>Foram longas 22 horas desenvolvendo e buscando informações para a melhor forma de entregar o produto. Inicialmente eu comprei um curso na Udemy de 12 horas sobre Web Scraping em Python onde gerou um <a href="https://www.udemy.com/certificate/UC-f508f580-298c-469b-87f6-dd7c467fb6d6/">certificado</a> ao concluir o curso, além disso passei por muitas pesquisas no google e examinação de códigos em HTML. Mostrarei a seguir passo a passo do que foi feito</p>
</br>

<h3 align="center">⚒️ BUILTWITH ⚒️</h3>
	   
<p align="center">Bom, o meu primeiro passo foi instalar a biblioteca "builtwith" para verificar as tecnologias utilizadas no site dos correios, ele analisa a URL informada e em seguida retornará todas as tecnologias utilizadas pelo site. Instalei a biblioteca utilizando um comando pelo prompt de comando ("pip install builtwith") e importei para o Python utilizando o ("import builtwith"), após isso eu utilizei o método paps("builtwith.parse('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')") onde ele traz as tecnologias.</p>
</br>

<h3 align="center">⚒️ PYTHON WHOIS ⚒️</h3>
	   
<p align="center">Meu segundo passo foi utilizar a biblioteca Python Whois que serve para identificação de propriedades do site. Instalei também pelo prompt utilizando o comando ("pip instal python-whois") e importei também utilizando o prompt de comando("import whois") e imprimi o resultado dentro do python utilizando o comando (whois.whois(‘buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')</p>
</br>

<h3 align="center">⚒️ URLLIB E BEAUTIFULSOUP⚒️</h3>
	   
<p align="center">Urllib é uma biblioteca padrão do python e contem funções para solicitação de dados web e manipulação de cookies. Dentro dessa biblioteca eu utilizei a função ("urlopen") que serve para ler um objeto remoto por meio de uma rede e ler esse objeto. Esse objeto pode ser arquivos HTML, arquivos de imagens ou qualquer outro fluxo de arquivos. Importei para o Python utilizando ("from urllib.request import urlopen")e abri as informações do site com("urlopen("https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/index.php")"), em seguida utilizei a biblioteca BeauifulSoup que não é padrão do Python e é utilizada para buscar informações em uma página HTML. Baixei ela manualmente no site ("https://www.crummy.com/software/BeautifulSoup/bs4/download/4.9/beautifulsoup4-4.9.0.tar.gz") e instalei pelo prompt de comando utilizando o ("pip install beautifulsoup4"), importei ela dentro do Python utilizando ("from bs4 import BeautifulSoup"), peguei o conteúdo do site e armazenei em uma variável utilizando o ("BeautifulSoup(COLOQUE_AQUI_A_VARIAVEL, "COLOQUE_AQUI_A_VARIAVEL.parser")") e em seguida coloquei alguns parametros a serem seguidos. </p>
</br>
</br>

<h2 align="center">🔨 DESENVOLVIMENTO DO PROJETO 🔨</h2>

<p align="center">Nessa parte eu explicarei como foi meu raciocínio e os caminhos que eu percorri.</br>Iniciei o código inserindo todas as bibliotecas que eu iria utilizar onde que se encontram a cima, em seguida utilizei algumas funções do Urllib e BeautifulSoup para puxar algumas informações, tive algumas dificuldades com o site até que encontrei um caminho pelo "Inspecionar" na parte "Sources" onde mostrava como o JavaScript da página funcionava, percebi que dentro de uma tag possuia algumas informações que poderiam carregar a forma de buscar o CEP na pagina, e o que eu encontrei foi a seguinte informação "carrega-faixa-cep-uf.php", foi então onde eu modifiquei a URL da pagina acrescentando o que foi encontrado e ficou da seguinte maneira "https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/carrega-faixa-cep-uf-localidade.php" e eu acrescentei umas funções para puxar apenas os dados de cada UF, utilizando "?uf=" no final do link, onde depois do "=" receberia a UF desejada. Foi ai que voltei para o código e fiz algumas alterações, coloquei uma função do BeautifulSoup para puxar apenas o texto das UFs na página "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm", em seguida criei um loop na função utilizada anteriormente e armazenando a informação em outro objeto, mandei imprimir essa objeto e em seguida transformei-o em uma string para utilizar na URL que encontrei, concatenei as informações da URL com a variável para que em cada rodada do loop ela apresente as informações do UF selecionado, utilizei essa variável novamente nas bibliotecas citadas a cima só que dessa vez eu utilizei uma função do JSON para ler a pagina que está no formato JSON, fiz outro loop para mostrar as informações solicitadas com alguns parâmetros e encerrei o código.</p>

</br>
</br>
<h4 align="center"> 
	🚧  Em construção...  🚧
</h4>

### Conquistas do projeto

- [x] Busca de informações no site.
- [x] Busca de todas UFs no site.
- [x] Busca da faixa de CEP de todos UFs.
- [ ] Colocar os dados em JSON.
</br>
</br>

Feito por Alyson Vieira 🚀 Entre em contato!!


[![Linkedin Badge](https://img.shields.io/badge/-Alyson-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/alyson-mendon%C3%A7a-vieira-330551181/)](https://www.linkedin.com/in/alyson-mendon%C3%A7a-vieira-330551181/) 
[![Gmail Badge](https://img.shields.io/badge/-alysonvieira88@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:alysonvieira88@gmail.com)](mailto:alysonvieira88@gmail.com)
