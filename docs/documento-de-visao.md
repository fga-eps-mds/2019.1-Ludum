# Histórico de Versão

 **Data** | **Versão** | **Descrição** | **Autor(es)**
|:----:|:------:|:---------:|:-----:|
| 27/03/19 | 0.1 | <p align="justify">Abertura do Documento de Visão</p> | MDS (Todos) |
| 28/04/19 | 0.3 | <p align="justify">Construção do Documento de Visão</p> | MDS (Todos) |
| 28/03/19 | 0.4 | <p align="justify">Construção do Documento de Visão</p> | Wictor Girardi, João de Assis |
| 29/03/19 | 0.5 | <p align="justify">Formatação em markdown e revisão</p> | Wictor Girardi |
| 30/03/19 | 0.6 | <p align="justify">Revisão e mudanças</p> | Lucas Ganda, Wictor Girardi, João Pedro Correia |
| 31/03/19 | 0.7 | <p align="justify">Revisão do documento</p> | Wictor Girardi |
| 01/04/19 | 0.8 | <p align="justify">Formatação do documento</p> | Lucas Ganda, João de Assis |
| 01/04/19 | 0.9 | <p align="justify">Pequenas correções no documento</p> | Lucas Ganda, João de Assis |

# 1. Introdução

<p align = "justify">Esta introdução fornece uma visão geral de todo o documento de visão. Ela inclui o propósito, o escopo, as definições, os acrônimos, as abreviações, as referências e a visão geral de todo o documento.</p>

## 1.1 Propósito

<p align = "justify">Este documento tem como objetivo definir os requisitos, necessidades e os recursos necessários, especificamente os de alto nível, para que o investidor possa compreender e tenha o completo entendimento do projeto Ludum.</p>

## 1.2 Escopo

<p align = "justify">O ChatBot Ludum é um projeto realizado para as disciplinas Métodos de Desenvolvimento de Software (MDS) e Engenharia de Produto de Software (EPS), do curso de Engenharia de Software da Faculdade UnB Gama (FGA) da Universidade de Brasília (UnB).
O projeto, a ser realizado pela equipe 8, composta por alunos das duas disciplinas, possui como objetivo auxiliar os interessados em progamações e desenvolvimento de jogos em dúvidas que eles tenham em relação ao desenvolvimento de jogos utilizando a linguagem em ascensão Python. Isso envolve obter dicas, guias da linguagem, tutoriais ao desenvolvimento de games, ferramentas necessárias e integração a uma ferramenta externa. A partir da interação com o ChatBot, o usuário poderá requisitar destes serviços, ajudas, informes relacionados à linguagem Python e sua biblioteca Pygame.</p>

## 1.3 Definições, acrônimos e abreviações

| Sigla | Definição |
| :--:|:------------------------:|
| UnB | Universidade de Brasília |
| FGA | Faculdade do Gama |
| MDS | Métodos de desenvolvimento de software |
| EPS | Engenharia do Produto de Software |
| Ludum | Nome do Projeto |

## 1.4 Referências

https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_6.0.5/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html

https://fga-eps-mds.github.io/2018.2-ComexStat/docs/docVisao

https://botlino.github.io/docs/doc-visao

## 1.5 Visão geral

<p align = "justify">Este documento descreve os detalhes sobre as características do software Ludum, especificando os problemas que estimularam a criação dessa solução em software. O documento se divide de maneira a separar as especificações e descrever as mesmas.</p>

# 2.  Posicionando

## 2.1 Oportunidade de Negócios

<p align = "justify">Hoje em dia, muitas pessoas se interessam em aprender a desenvolver jogos e como Python é considerada uma linguagem de programação de fácil aprendizado, muitas vezes é escolhida por iniciantes como porta de entrada e como a biblioteca Pygame é uma das principais bibliotecas utilizadas para o desenvolvimento de jogos em Python, também é muito escolhida ao se iniciar.</p>

## 2.2 Descrição do Problema

<table> 
<tr><th>Problema de</th><td>Dificuldade de um iniciante no aprendizado da biblioteca Pygame para o desenvolvimento de jogos.</td></tr>
<tr><th>Afeta</th><td>O entusiasmo no que diz respeito ao início dos estudos de desenvolvimento de jogos.</td></tr>
<tr><th>Cujo Impacto é</th><td>Menor chances da continuação dos estudos de desenvolvimento de jogos devido à frustração.</td></tr>
<tr><th>Uma boa solução seria</th><td>Um chatbot que de maneira simples e direta auxiliaria o aprendizado para o desenvolvimento de jogos baseados na linguagem de programação Python e em sua biblioteca Pygame.</td></tr>
</table>

## 2.3 Instrução de Posição do Produto

<table> 
<tr><th>Para</th><td>Estudantes da área de programação e pessoas interessadas no desenvolvimento de jogos.</td></tr>
<tr><th>Que</th><td>Buscam em um software uma maneira prática e acessível de aprender e desenvolver um jogo na linguagem Python através da biblioteca Pygame.</td></tr>
<tr><th>O Ludum</th><td>É um ChatBot.</td></tr>
<tr><th>Diferente de</th><td>Todas as opções disponíveis para aprender a desenvolver jogos usando a biblioteca Pygame.</td></tr>
<tr><th>Nosso Produto</th><td>Responde perguntas sobre o desenvolvimento de jogos em Python e sua biblioteca Pygame.</td></tr>
</table>

# 3. Descrições da Parte Interessada e do Usuário

## 3.1 Demográficos de Mercado

<p align = "justify">Os principais envolvidos neste projeto serão as equipes de desenvolvimento (MDS), gestores (EPS) e monitores, sendo que esses não necessariamente irão ser usuários do aplicativo.
O público-alvo do projeto, que irá interagir com o Ludum, são pessoas interessadas em programação e desenvolvimento de jogos, sejam eles de graduação ou pós-graduação.
Os principais artefatos que o Ludum propõe é a maior interatividade e facilidade para o desenvolvimento de pessoas não ligadas a software dentro da Universidade de Brasília.</p>

## 3.2 Resumo dos envolvidos

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Equipe de desenvolvimento de software|Estudantes da Disciplina Métodos de Desenvolvimento de Software.|Desenvolvimento e Testes do Software descrito no documento.|
|Equipe de engenharia de produto de software|Estudantes da Disciplina Engenharia de Produto de Software.|Gestão da Equipe de Desenvolvimento, bem como manutenção de ambientes e entrega contínua.|
|Orientador|Professoras da Universidade de Brasília no campus Faculdade Gama (FGA - UnB) das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software.|Orientar as equipe de desenvolvimento e gestão em eventuais dúvidas.|

## 3.3 Resumo do Usuário

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Estudantes|Interessados em programações de jogos|Interagir com o Ludum por meio da plataforma Telegram, receber auxílio e sanar suas dúvidas sobre o desenvolvimento de jogos em Python|

## 3.4 Principais Necessidades dos Usuários e dos Envolvidos

<p align = "justify">Os usuários realizarão a interação com o Ludum por meio do Telegram, serviço de mensagens instantâneas, para receberem instruções sobre o Pygame, além de poderem consultar sempre que tiverem dúvidas ou desejarem maiores esclarecimentos a respeito do desenvolvimento com Pygame.</p>

## 3.5 Perfis das Partes Interessadas

## 3.5.1 Equipe de desenvolvimento de software (MDS)

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Lucas Ganda, Wictor Girardi, João de Assis, João Pedro Correia, Thallys Silva.</td></tr>
<tr><th>Descrição</th><td>Desenvolvimento de Software.</td></tr>
<tr><th>Tipo</th><td>Estudantes da Universidade de Brasília, da disciplina de Métodos de Desenvolvimento de Software.</td></tr>
<tr><th>Responsabilidades</th><td>Desenvolver, testar e implantar o software.</td></tr>
<tr><th>Critérios de Sucesso</th><td>Finalizar o desenvolvimento e realizar a entrega do bot no tempo estipulado.</td></tr>
<tr><th>Envolvimento</th><td>Alto.</td></tr>
<tr><th>Problemas/comentários</th><td>Desenvolver o software no tempo estabelecido pela equipe de EPS. Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o software.</td></tr>
</table>

## 3.5.2 Equipe de engenharia de produto de software (EPS)

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Guilherme Siqueira Brandão, Gabriela Chaves de Moraes, Lucas Arthur Lermen, Lucas Penido Antunes</td></tr>
<tr><th>Descrição</th><td>Gerenciamento do Projeto.</td></tr>
<tr><th>Tipo</th><td>Estudantes da Universidade de Brasília, Disciplina de Engenharia de Produto de Software (EPS)</td></tr>
<tr><th>Responsabilidades</th><td>Monitorar, motivar, orientar e preparar a equipe de desenvolvimento. Definir prazos para as atividades propostas.</td></tr>
<tr><th>Critérios de Sucesso</th><td>Manter os prazos estabelecidos sem atraso, e gerenciar a qualidade do software em desenvolvimento, finalizando o projeto no tempo estipulado</td></tr>
<tr><th>Envolvimento</th><td>Alto</td></tr>
<tr><th>Problemas/comentários</th><td>Organizar prazos e metas de acordo com o tempo disponível</td></tr>
</table>

## 3.6 Perfil do Usuário

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Interessados em programações de jogos</td></tr>
<tr><th>Descrição</th><td>Interessados no desenvolvimento de jogos em Python</td></tr>
<tr><th>Tipo</th><td>Interessados no desenvolvimento de jogos que tenham dúvidas e necessitem de ajuda com o desenvolvimento de jogos em Python</td></tr>
<tr><th>Responsabilidades</th><td>Interagir com o Ludum por meio da aplicação Telegram.
</td></tr>
<tr><th>Critérios de Sucesso</th><td>Desenvolver jogos com ajuda do bot Ludum</td></tr>
<tr><th>Envolvimento</th><td>Alto</td></tr>
<tr><th>Problemas/comentários</th><td>Não possuir cadastro no Telegram, não possuir conexão com a internet e possuir hardware insuficiente para a execução da aplicação</td></tr>
</table>

## 3.7 Principais Necessidades da Parte Interessada ou do Usuário

| Necessidade| Prioridade | Preocupação | Solução proposta | Solução Atual |
|:----:|:---------:|:-----------------:|:------------------:|:------:|
|Sanar dúvidas que tangem o quesito de desenvolvimento de jogos em Python|Alta|Falta de interação com o Ludum|Um ChatBot de Telegram que consiga auxiliar o público alvo respondendo suas dúvidas e necessidades| Videos no youtube, Stackoverflow e sites de desenvolvimento|
|Ajudar a configuração de ambientes|Média|Falta de interação com o Ludum ou hardware antigo|Guias propostos pelo Ludum para auxiliar de maneira rápida a configuração do ambiente|Google e fóruns|

## 3.8 Alternativas e Concorrência  

<p align = "justify">Não existem.</p>

# 4. Visão Geral do Produto

## 4.1 Perspectiva do Produto  

<p align = "justify">O ChatBot Ludum tem como objetivo auxiliar e tornar o desenvolvimento de jogos na tecnologia Python uma atividade mais prazerosa, onde o usuário será guiado desde o nível básico da linguagem até o nível avançado, onde será possível a criação de jogos mais complexos, isso tudo aliado ao auxílio para configuração do ambiente de trabalhos e de suas ferramentas necessárias.</p>

## 4.2 Resumo das Capacidades

| Benefício para o cliente | Recursos de suporte |
|:------------------------:|:-------------------:|
| Auxiliar o desenvolvimento de jogos |O ChatBot Ludum irá auxiliar o usuário de maneira prática a desenvolver jogos desde a dificuldade inicial até a mais avançada|
| Conexão com uma ferramenta externa | O Ludum poderá acessar uma ferramenta externa para buscar informações sobre a biblioteca PyGame |
| Configuração de ambiente | O ChatBot irá auxiliar o usuário, antes do desenvolvimento, a configurar o ambiente. |
| Sanar duvidas | O Ludum permitira que as duvidas do usuário sejam sanadas por meio de um FAQ, indicando links e materiais utéis |

# 5. Recursos do Produto

O ChatBot Ludum é capaz de:

<p align = "justify">Realizar a integração entre bot, usuário e ferramenta externa.
Ensinar noções básicas de Python e como trabalhar com a biblioteca Pygame.
Dar dicas de como configurar o ambiente de desenvolvimento.
Recomendar links e materiais úteis.
Realizar o desenvolvimento de jogos de diferentes níveis de dificuldade de desenvolvimento.</p>

# 6. Restrições

## 6.1 Restrições de implementação

<p align = "justify">O ChatBot deverá ser implementado na linguagem Python utilizando a arquitetura de microsserviços.</p>

## 6.2 Restrições externas

<p align = "justify">Dentre as restrições externas, as que mais irão influenciar são a inexperiência com a linguagem e frameworks, além de possíveis transtornos entre a equipe de desenvolvimento.</p>

## 6.3 Restrições de confiabilidade

<p align = "justify">O sistema deverá ter cobertura de testes - mínimo de 90%.</p>

# 7. Faixas de Qualidade

<p align = "justify">Para maior eficiência, será utilizado por meio da aplicação Telegram, para uma forma segura e rápida de gerenciamento de dados e informações.</p>

# 8. Requisitos do produto

## 8.1 Requisitos do Sistema

<p align = "justify">Esta aplicação deverá ser acessada através de dispositivos que possuem a aplicação Telegram em que o sistema operacional é variável de acordo com o dispositivo de utilização, podendo ser: Android, iOS, Windows, Linux, Chrome OS.</p>

## 8.2 Requisitos de implementação

<p align = "justify">Para maior eficiência, o Ludum será desenvolvido para ser utilizado em uma das maiores plataformas de comunicação Telegram, onde a implementação de funcionalidades se mostra viável.</p>

## 8.3 Requisitos de design

<p align = "justify">A composição deste software será feita de maneira a tornar sua utilização autoexplicativa e fácil, para acesso em tempo real, ou seja, atendendo todas as especificações de boas práticas referentes à experiência de usuário.</p>
