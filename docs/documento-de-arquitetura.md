<!-- # Histórico de Versão

 **Data** | **Versão** | **Descrição** | **Autor(es)**
---|---|---|---
31/03/2019 | 0.1 | Iniciação | Lucas Penido
01/04/2019 | 0.2 | Definição das tecnologias e padrão arquitetural | Lucas Penido

# Iniciando Documento de Arquitetura

## Padrão Arquitetural:

Nosso projeto deve conter microsserviços, com isso a utilização de APIs.

O padrão arquitetural que será utilizado é o Broker, sua arquitetura lida muito bem com sistemas distribuídos, assim como microsserviços.  

Links que podem ajudar:

Entendendo microsserviços:  
https://www.redhat.com/pt-br/topics/microservices  
https://www.redhat.com/pt-br/topics/microservices/what-are-microservices  
https://sensedia.com/blog/soa/de-soa-a-microservicos/  

Para entender um pouco melhor as boas práticas HTTP e REST:  
http://downloads.sensedia.com/webinar-design-de-apis-restful (Webinar)  

https://docplayer.com.br/590648-Padroes-arquiteturais-sistemas-distribuidos-broker.html  
https://www.dimap.ufrn.br/~thais/MES20061/aulaEstilos.pdf  

## Tecnologias:

### Telegram Bot API:
Versão 4.1

Para fazer uma comunicação com o Bot é utilizado uma API do Telegram.  
Link: https://core.telegram.org/bots

### python-telegram-bot
Versão 11.1.0  

Há uma biblioteca que fornece uma interface Python para utilizar a API do telegram.  
Link: https://github.com/python-telegram-bot/python-telegram-bot

## MongoDB
Versão 4.0.8

Para o banco de dados iremos utilizar o MongoDB.  
Link: https://www.mongodb.com/

Para utilizar o MongoDB a partir do Python será utilizado o **PyMongo**  
Versão 3.7.2  
Link: https://pypi.org/project/pymongo/

### Rasa

Crie assistentes de IA que vão além de FAQs.  

Link: https://rasa.com/  

Artigos interessantes:  
Aprimorando modelos NLU Rasa com componentes personalizados.  
https://medium.com/rasa-blog/enhancing-rasa-nlu-models-with-custom-components-6f54040c4a77  

Qual pipeline Rasa NLU escolher para o seu projeto.  
https://medium.com/rasa-blog/rasa-nlu-in-depth-part-1-intent-classification-cb17e27fb169

### Rasa Core
Versão 0.13.4  

Um framework de chatbot com gerenciamento de diálogo baseado em aprendizado de máquina.  

Link: https://rasa.com/docs/core/

### Rasa NLU
Versão 0.14.6

Uma biblioteca para compreensão de linguagem natural com intenção de classificação e extração de entidade

Links: https://rasa.com/docs/nlu/

Biblioteca para o Python: https://rasa.com/docs/nlu/python/

### Stack Exchange API
Versão 2.2  

API utilizada para a funcionalidade de procurar e fazer perguntas no StackOverflow.  
Link: https://api.stackexchange.com/


## Documentos de Arquitetura que podem ajudar  
https://botlino.github.io/docs/doc-arquitetura  
https://github.com/fga-eps-mds/2017.2-Receita-Mais/wiki/Documento-de-Arquitetura  
https://github.com/fga-eps-mds/2017.1-Trezentos/wiki/Documento-de-Arquitetura  
https://github.com/fga-eps-mds/2017.2-MerendaMais/wiki/Documento-de-Arquitetura   -->



# Histórico de Revisão

| Data   | Versão | Modificação  | Autor  |
| :------- | :--------- | :---------------- | :------- |
| 31/03/2019 | 0.1   |  Iniciação  | Lucas Penido  |
| 01/04/2019 | 0.2   | Definição das tecnologias e padrão arquitetural  | Lucas Penido  |
| 04/04/2019 | 0.3   | Aprimoração do documento  | MDS(Todos)  |

#### 1. Introdução  

<p  align="justify">  Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do ChatBot Ludum, garantindo uma facilidade de visualização dos requisitos e da estrutura para com os desenvolvedores.</p>

##### 1.1 Finalidade  

<p  align="justify">   Ao esboçar uma visão ampla da arquitetura do ChatBot, é possível evidenciar seus aspectos. Sendo assim, nesse documento buscaremos transparecer as decisões arquiteturais que foram tomadas em relação ao Bot Ludum.</p>

##### 1.2 Escopo

<p  align="justify">  O Ludum tem como principal objetivo auxiliar os alunos que desejam aprender a desenvolver jogos em Python, à partir da utilização de tecnologias de fluxo de conversa e de bancos de dados para o registro de usuário. O Ludum servirá como uma ferramenta de auxílio a pessoas que possuírem interesse em desenvolvimento de jogos em Python, podendo ajudar desde a configuração do ambiente, auxilio no desenvolvimento de jogos com tutoriais e uso do código fornecido em ferramentas externas </p>

##### 1.3 Visão Geral

<p  align="justify">  Documento, cujo objetivo, por meio de tópicos busca detalhar os requisitos e a arquitetura do ChatBot. Com o objetivo de esclarecer dúvidas, facilitar o desenvolvimento e o entendimento de suas funções.</p>

Estrutura do documento:  

<html>
<ul>

<li> Introdução; </li>
<li> Representação da Arquitetura; </li>
<li> Metas e Restrições de Arquitetura; </li>
<li> Visão lógica;   </li>

</ul>
</html>

##### 1.4 Definições, Acrônimos e Abreviações

<html>
<ul>

<li> API: Application Programming Interface </li>
<li> DB: Banco de Dados, <i>DataBase</i> </li>

</ul>
</html>

##### 1.5 Referências


> MELO, Thalisson; ALVES, Álax; MARTINS, Lucas; RICHARD, Matheus; BERNARDO, Matheus de Sousa; Joranhezon. <b>Owla:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-Owla/wiki/Documento-de-Arquitetura>.


> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.


#### 2. Representação da Arquitetura

##### 2.1 Diagrama de Relações

<p  align="justify">&emsp;&emsp;O projeto foi moldado e pensado para uma arquitetura híbrida, incluindo Microsserviços com elementos da arquitetura de repositórios, representando os serviços que serão mostrados adiante.</p>

<p align="justify">&emsp;&emsp; A existência de um diálogo é de grande importância pro contexto do bot, que por possuir características de <i>Machine Learning</i> e <i> Artificial Intelligence</i>  consegue melhorar suas conversas, para sempre manter o diálogo correto e apropriado com o usuário.</p>

<p  align="justify">&emsp;&emsp;O Rasa Core é um dos componentes importantes dentro da arquitetura do Bot, em associação ao Rasa Core, existe outro componente tecnológico atrelado ao ChatBot: <i>Rasa NLU</i>, que trabalha com o processamento natural de linguagem e, a partir dela, o desenvolvedor abre portas relacionadas ao processamento de texto que o permitem criar um ambiente de comunicação mais interativo e humano, podendo assim criar uma comunicação mais fluida e dinâmica com o usuário.</p>

<p align="justify">&emsp;&emsp;A utilização da tecnologia no desenvolvimento de um ChatBot permite a implementação de uma comunicação mais humanizada, permitindo assim uma maior interatividade com o usuário. Com o tempo, a interação com o usuário permitirá ao programa um treinamento dele mesmo para melhor se comunicar com o exterior. Este é o principal objetivo da utilização do <i>Rasa NLU</i> para o processamento de linguagem do projeto em questão.</p>
<p  align="justify">&emsp;&emsp;Algumas dos principais benefícios da tecnologia são:</p>

<html>
<ul>

<li>  Manuseio de conversação com <i>deep learning</i> para auto-evolução; </li>
<li>  <i>Open source</i> e customizável para o panorama do projeto; </li>
<li>  <i>Machine learning</i> integrado para melhores resultados. </li>

</ul>
</html>

<p  align="justify">&emsp;&emsp;A tecnologia irá se comunicar com outras com o intuito de captar e processar informações do exterior, de acordo com as necessidades do usuário.</p>

<p align="justify">&emsp;&emsp;Relacionado a parte de arquitetura de micro serviços, foram definidos 4 serviços internos (serviços a serem implementados), além dos 3 serviços externos (serviços a serem utilizados), sendo eles:</p>

###### 2.1.1 Serviços Internos

<html>
<ul>

</ul>
</html>

###### 2.1.2 Serviços Externos

<html>
<ul>

</ul>
</html>


<p align="justify">&emsp;&emsp;Além de tais serviços, também existe a integração de um painel para a análise de dados relativos às métricas associadas no Backlog de produto.</p>

##### 2.2 Tecnologias

###### 2.2.1 API Telegram Messenger

<p  align="justify">&emsp;&emsp;Telegram Messenger é um aplicativo de comunicação e bate-papo serviço de mensagens instantâneas baseadas em nuvens. O aplicativo da liberdade para seus usuários desenvolvedores implementarem diferentes funcionalidades e <i>bots</i>, a partir de sua API.</p>


<p  align="justify">&emsp;&emsp;As <i>APIs</i> dessas duas plataformas serão as pontes de comunicação com o usuário. A partir da implementação e integração do código-fonte com o <i>Rasa NLU</i>, o Telegram irá interagir com o usuário, recebendo suas mensagens e respondendo apropriadamente.</p>

###### 2.2.2 Python Telegram Bot 
<p align=”justify”> <i>Bots</i> do Telegram são contas simples, controladas e operadas por software que faz uso de algumas tecnologias como a inteligência artificial e <i>machine learning</i> para desenvolver e executar suas funcionalidades, como por exemplo, ensinar, pesquisar, conectar, integrar com outras plataformas e ambientes ou até mesmo passar informações para a Internet de acordo com sua programação.</p>

###### 2.2.3 MongoDB

<p  align="justify">&emsp;&emsp;A tecnologia MongoDB é um banco de dados <i>open-source</i> orientado a documentos. Classificado como NoSQL, a tecnologia utiliza documentos com padrão JSON.</p>

<p  align="justify">&emsp;&emsp;Esta tecnologia se comunicará com o projeto de maneira que receberá os dados fornecidos pelas conversas e interações realizadas no ChatBot e as armazenará em um banco de dados, para posteriormente serem usadas na metrificação da utilização do ChatBot.</p>

###### 2.2.4 Rasa

<p  align="justify">&emsp;&emsp;O Rasa é um conjunto de ferramentas de machine learning de código aberto para os desenvolvedores criarem chatbots e assistentes contextuais baseados em texto e voz. 

###### 2.2.5 Rasa Core

<p  align="justify">&emsp;&emsp;Um framework de chatbot com gerenciamento de diálogo baseado em machine learning.

###### 2.2.6 Rasa NLU

<p  align="justify">&emsp;&emsp;Uma biblioteca para compreensão de linguagem natural com intenção de classificação e extração de entidade.

###### 2.2.7 Stack Exchange API

<p  align="justify">&emsp;&emsp;API utilizada para a funcionalidade de procurar e fazer perguntas no StackOverflow.

##### 2.3 Representação dos Serviços

<p align="justify">&emsp;&emsp;Relacionado aos microserviços propostos pela equipe, faz-se o uso de serviços internos desenvolvidos e os serviços externos, utilizados para atingir a finalidade do Lino. Entre eles, temos:</p>

* <i>Webcrawler</i> do Restaurante Universitário - WebCrawler RU
* <i>Webcrawler</i> do Calendário de Matrícula - WebCrawler Matrícula
* Captação de e-mails através da API <i>G-mail</i> - Lino-Alerta
* Notificações de alerta - Cronjob Lino

Além disso, temos o core do projeto, que apesar da relevância, uma suposta falha não afeta o funcionamento dos demais serviços existes. O Lino, tem a capacidade de fazer, atualmente, uma integração com os mensageiros Telegram e Facebook Messenger, buscando realizar uma comunicação de forma mais natural e entendível, fazendo uso das tecnologias de inteligência artificial para compreensão de linguagem natural e integrando com demais serviços que fornecem informações para o Bot tratar adequadamente.

#### 3. Metas e Restrições de Arquitetura

<p align="justify">&emsp;&emsp;As restrições de arquitetura do projeto são:</p>

<html>
<ul>

<li> Utilização de um Banco de Dados <i>MongoDB</i> de versão 4.0.8 para cada serviço interno e para ser utilizado a partir do Python será utilizado PyMongo na versão 3.7.2  </li>
<li> Utilização da ferramenta Docker para a virtualização dos ambientes de forma prática e adequada </i>
<li> Conexão com a internet necessária. </li>

</ul>
</html>

<p align="justify">    As metas do projeto são:</p>

<html>
<ul>

<li> Disponibilizar um fluxo de conversa com o usuário a fim de atender/suprir as dúvidas em relação à procedimentos voltados ao desenvolvimento de jogos em Python. </li>
<li> Fornecer aos usuários links e dicas de como configurar seu ambiente </li>
<li>Fornecer ao usuário uma maneira de rodar seus códigos em uma ferramenta externa.</li>

</ul>
</html>

#### 4. Visão Lógica

##### 4.1 Diagrama de Pacotes

<p  align="justify">    Neste tópico se encontram o diagrama de pacotes bem como suas explicações e utilidades.</p>

<html>
<ul>

<li> O pacote <i>2019.1-Ludum</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto. </li>
<li> No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>. </li>
<li> No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>. </li>

</ul>
</html>

<br>
