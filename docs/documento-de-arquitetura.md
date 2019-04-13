# Histórico de Revisão

| Data   | Versão | Modificação  | Autor  |
| :------- | :--------- | :---------------- | :------- |
| 31/03/2019 | 0.1   |  Iniciação  | Lucas Penido  |
| 01/04/2019 | 0.2   | Definição das tecnologias e padrão arquitetural  | Lucas Penido  |
| 04/04/2019 | 0.3   | Criação do documento  | MDS(Todos)  |
| 07/04/2019 | 0.4   | Modificação da parte 2 do documento | João Pedro, Wictor Girardi, João de Assis e Lucas Ganda |
| 11/04/2019 | 0.5   | Modificação sessão Introdução | Thallys |
| 12/04/2019 | 0.6   | Correção de estrutura e escrita| Thallys |


# 1. Introdução  

## 1.1 Finalidade  

<p  align="justify">&emsp;&emsp;Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do ChatBot Ludum, garantindo uma facilidade na visualização dos requisitos e da estrutura para com os desenvolvedores. Ao esboçar uma visão ampla da arquitetura do ChatBot, é possível evidenciar seus aspectos do sistema em diversas técnicas. Sendo assim, nesse documento buscaremos transparecer as decisões arquiteturais que foram tomadas em relação ao Bot Ludum.</p>

## 1.2 Escopo

<p  align="justify">&emsp;&emsp;O Ludum tem como principal objetivo auxiliar pessoas que desejam aprender a desenvolver jogos em Python, a partir da utilização de tecnologias de fluxo de conversa e de bancos de dados para o registro de usuário. E também servirá como uma ferramenta de auxílio a esse público, podendo ajudar desde a configuração do ambiente, auxílio no desenvolvimento de jogos com tutoriais e uso do código fornecido em ferramentas externas. </p>

## 1.3 Definições, Acrônimos e Abreviações

<html>
<ul>
<li> FAQ: <i>frequently asked questions</i></li>
<li> MDS: Método de D</li>
<li> API: <i>Application Programming Interface </i></li>
<li> DB: Banco de Dados, <i>DataBase</i> </li>

</ul>
</html>

## 1.4 Visão Geral

<p  align="justify">&emsp;&emsp;Documento, cujo objetivo, por meio de tópicos busca detalhar os requisitos e a arquitetura do ChatBot Ludum. Com o objetivo de esclarecer dúvidas, facilitar o desenvolvimento e o entendimento de suas funções.</p>

Estrutura do documento:  

<html>
<ul>

<li> Introdução; </li>
<li> Representação da Arquitetura; </li>
<li> Metas e Restrições de Arquitetura; </li>
<li> Visão lógica;   </li>

</ul>
</html>

## 1.5 Referências

> MELO, Thalisson; ALVES, Álax; MARTINS, Lucas; RICHARD, Matheus; BERNARDO, Matheus de Sousa; Joranhezon. <b>Owla:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-Owla/wiki/Documento-de-Arquitetura>.


> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.

> RODRIGUES, Pedro; BLANCO, Matheus; BRAGA, Gabriel; FILIPE, Gabriel; AUGUSTO, Guilherme; DE SOUZA, Letícia. <b>Lino:</b> Documento de Arquitetura. Disponível em:
<https://github.com/fga-eps-mds/2018.2-Lino/blob/master/docs/documento-de-arquitetura.md>.


# 2. Representação da Arquitetura

## 2.1 Diagrama de Relações


<p  align="justify">&emsp;&emsp;O projeto foi moldado e pensado para uma arquitetura híbrida, incluindo Microsserviços com elementos da arquitetura de repositórios, representando os serviços que serão mostrados adiante.</p>

<p align="justify">&emsp;&emsp; A existência de um diálogo é de grande importância pro contexto do bot, que por possuir características de <i>Machine Learning</i> e <i> Artificial Intelligence</i>  consegue melhorar suas conversas, para sempre manter o diálogo correto e apropriado com o usuário.</p>

<p  align="justify">&emsp;&emsp;O Rasa Core é um dos componentes importantes dentro da arquitetura do Bot, em associação ao Rasa Core, existe outro componente tecnológico atrelado ao ChatBot: <i>Rasa NLU</i>, que trabalha com o processamento natural de linguagem e, a partir dela, o desenvolvedor abre portas relacionadas ao processamento de texto que o permitem criar um ambiente de comunicação mais interativo e humano, podendo assim criar uma comunicação mais fluída e dinâmica com o usuário.</p>

<p align="justify">&emsp;&emsp;A utilização da tecnologia no desenvolvimento de um ChatBot permite a implementação de uma comunicação mais humanizada, permitindo assim uma maior interatividade com o usuário. Com o tempo, a interação com o usuário permitirá ao programa um treinamento dele mesmo para melhor se comunicar com o exterior. Este é o principal objetivo da utilização do <i>Rasa NLU</i> para o processamento de linguagem do projeto em questão.</p>
<p  align="justify">&emsp;&emsp;Algumas dos principais benefícios da tecnologia são:</p>

<html>
<ul>

<li>  Manuseio de conversação com <i>deep learning</i> para auto-evolução </li>
<li>  <i>Open source</i> e customizável para o panorama do projeto; </li>
<li>  <i>Machine learning</i> integrado para melhores resultados. </li>


</ul>
</html>

<p  align="justify">&emsp;&emsp;A tecnologia irá se comunicar com outras com o intuito de captar e processar informações do exterior, de acordo com as necessidades do usuário.</p>

<p align="justify">&emsp;&emsp;Na parte de arquitetura de microsserviços, foram definidos como, serviços internos (serviços a serem implementados), e serviços externos (serviço a ser utilizado pelo usuário).</p>

### 2.1.1 Serviços Internos

<html>
<ul>
<li>  Captação de dados do Banco de Dados <i>MongoDB</i> - Ludum MDB; </li>
<li>  Organizar e listar as perguntas mais frequentes- Ludum FAQ </li>
<li>  Desenvolvimento da IA e personalidade do bot - <i>Rasa </i> </li>
</ul>
</html>

### 2.1.2 Serviços Externos
<html>
<ul>
<li> Aplicativo Telegram para interação </li>
</ul>
</html>
<p align="justify">&emsp;&emsp;Além de tais serviços, também existe a integração de um painel para a análise de dados relativos às métricas associadas no Backlog de produto.</p>

## 2.2 Tecnologias

### 2.2.1 API Telegram Messenger

<p  align="justify">&emsp;&emsp;<i>Telegram Messenger</i> é um aplicativo de comunicação e bate-papo serviço de mensagens instantâneas baseadas em nuvens. O aplicativo dá liberdade para seus usuários desenvolvedores implementarem diferentes funcionalidades e <i>bots</i>, a partir de sua API.</p>


<p  align="justify">&emsp;&emsp;A <i>API</i> dessa plataforma será as pontes de comunicação com o usuário. A partir da implementação e integração do código-fonte com o <i>Rasa NLU</i>, o Telegram irá interagir com o usuário, recebendo suas mensagens e respondendo apropriadamente.</p>

### 2.2.2 Python Telegram Bot 
<p align=”justify”>&emsp;&emsp;<i>Bots</i> do Telegram são contas simples, controladas e operadas por software que faz uso de algumas tecnologias como a inteligência artificial e <i>machine learning</i> para desenvolver e executar suas funcionalidades, como por exemplo, ensinar, pesquisar, conectar, integrar com outras plataformas e ambientes ou até mesmo passar informações para a Internet de acordo com sua programação.</p>

### 2.2.3 MongoDB

<p  align="justify">&emsp;&emsp;A tecnologia MongoDB é um banco de dados <i>open-source</i> orientado a documentos. Classificado como NoSQL, a tecnologia utiliza documentos com padrão JSON.</p>

<p  align="justify">&emsp;&emsp;Esta tecnologia se comunicará com o projeto de maneira que receberá os dados fornecidos pelas conversas e interações realizadas no ChatBot e as armazenará em um banco de dados, para posteriormente serem usadas na metrificação da utilização do ChatBot.</p>

### 2.2.4 Rasa

<p  align="justify">&emsp;&emsp;O Rasa é um conjunto de ferramentas de machine learning de código aberto para os desenvolvedores criarem chatbots e assistentes contextuais baseados em texto e voz. 

### 2.2.5 Rasa Core

<p  align="justify">&emsp;&emsp;Um framework de chatbot com gerenciamento de diálogo baseado em machine learning.

### 2.2.6 Rasa NLU

<p  align="justify">&emsp;&emsp;Uma biblioteca para compreensão de linguagem natural com intenção de classificação e extração de entidade.

### 2.2.7 Stack Exchange API

<p  align="justify">&emsp;&emsp;API utilizada para a funcionalidade de procurar e fazer perguntas no StackOverflow.

### 2.3 Representação dos Serviços

<p align="justify">&emsp;&emsp;Relacionado aos microsserviços propostos pela equipe, faz-se o uso de serviços internos desenvolvidos e os serviços externos, utilizados para atingir a finalidade do Ludum. </p>

<p align="justify">&emsp;&emsp;Relacionado aos microsserviços propostos pela equipe, faz-se o uso de serviços internos desenvolvidos e os serviços externos, utilizados para atingir a finalidade do Ludum. Entre eles, temos:</p>

* Captação de dados do Banco de Dados <i>MongoDB</i> - Ludum MDB 
* Organizar e listar as perguntas mais frequentes- Ludum FAQ
* Desenvolvimento da IA e personalidade do bot <i>Rasa </i>
* <i>Webcrawler</i> do StackOverflow - <i>WebCrawler SO</i>

&emsp;&emsp;Além disso, temos o core do projeto, que apesar da relevância, uma suposta falha não afeta o funcionamento dos demais serviços existes. O Ludum, tem a capacidade de fazer, atualmente, uma integração com o mensageiro Telegram, buscando realizar uma comunicação de forma mais natural e entendível, fazendo uso das tecnologias de inteligência artificial para compreensão de linguagem natural e integrando com demais serviços que fornecem informações para o Bot tratar adequadamente.
</p>


<p align="justify">&emsp;&emsp;A respeito da estrutura geral do banco associado ao WebCrawler SO, temos a seguinte diagramação:</p>

### 2.3.1  Ludum FAQ

<p align="justify">&emsp;&emsp;O serviço Ludum FAQ tem como objetivo registrar e organizar as perguntas mais frequentes. De forma básica, o sistema trabalha com o uso do <i>MongoDB</i>, banco de dados orientado a documentos, registrando as perguntas dos usuários e as organizando por frequência, para assim listá-las.</p>
<p align="justify">&emsp;&emsp;O banco relacionado ao serviço tem uma estrutura mais simples, apenas contendo as informações das perguntas, recebendo um <i>id</i> para identificá-los individualmente, após a efetuação da pesquisa a pergunta receberá um acréscimo no número de buscas, e o banco se organizará de acordo com isso.</p>

### 2.3.2 Ludum MDB

<p align="justify">&emsp;&emsp;O Ludum MDB é um microsserviço especializado em trabalhar com a organização das respostas dadas ao usuário, pesquisando no banco a pergunta realizada e enviando ao usuário a resposta</p>

### 2.3.3  Rasa

<p align="justify">&emsp;&emsp;O uso do Rasa será um serviço focado para gerar frases respostas do bot de acordo com a entrada do usuário, o serviço será responsável por pegar a entrada do usuário, entender a intenção do que foi dito, achar as entidades e gerar a saída para o usuário  </p>

# 3. Metas e Restrições de Arquitetura

<p align="justify">&emsp;&emsp;As restrições de arquitetura do projeto são:</p>

<html>
<ul>

<li> Utilização de um Banco de Dados <i>MongoDB</i> de versão 4.0.8 para cada serviço interno e para ser utilizado a partir do Python será utilizado PyMongo na versão 3.7.2  </li>
<li> Utilização da ferramenta Docker para a virtualização dos ambientes de forma prática e adequada </i>
<li> Conexão com a internet necessária. </li>

</ul>
</html>

<p align="justify">&emsp;&emsp;As metas do projeto são:</p>

<html>
<ul>

<li> Disponibilizar um fluxo de conversa com o usuário a fim de atender/suprir as dúvidas em relação à procedimentos voltados ao desenvolvimento de jogos em Python. </li>
<li> Fornecer aos usuários links e dicas de como configurar seu ambiente </li>
<li>Fornecer ao usuário uma maneira de executar seus códigos em uma ferramenta externa.</li>

</ul>
</html>

# 4. Visão Lógica

## 4.1 Visão Lógica Geral
<p align="justify">&emsp;&emsp;Esta seção descreve as partes significativas do ponto de vista da arquitetura do modelo de design. Além disso, para cada pacote significativo, descreve suas responsabilidades, bem como algumas operações e atributos de grande importância.</p>


## 4.2 Diagrama de Pacotes

<p  align="justify">    Neste tópico se encontram a descrição de alguns pacotes utilizados bem como suas explicações e utilidades.</p>

<html>
<ul>

<li> O pacote <i>2019.1-Ludum</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto. </li>
<li> No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>. </li>
<li> No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>. </li>

</ul>
</html>

<br>
