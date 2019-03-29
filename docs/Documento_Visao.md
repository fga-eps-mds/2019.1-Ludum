
| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
| 27/03/19 | 0.1 | Abertura do Documento de Visão | MDS (Todos) |
| 28/04/19 | 0.3 | Construção do Documento de Visão | MDS (Todos) |
| 28/03/19 | 0.4 | Construção do Documento de Visão | Wictor Girardi, João de Assis |
| 29/03/19 | 0.5 | Formatação em markdown e revisão | Wictor Girardi |

# 1. Introdução

Esta introdução fornece uma visão geral de todo o documento de visão. Ela inclui o propósito, escopo, definições, acrônimos, abreviações, referências e visão geral de todo o documento.

## 1.1 Propósito

Este documento tem como objetivo definir os requisitos, necessidades e os recursos necessários, especificamente os de alto nível, para que o investidor possa compreender e tenha o completo entendimento do projeto Ludum.

## 1.2 Escopo

O ChatBot Ludum é um projeto realizado para as disciplinas Métodos de Desenvolvimento de Software (MDS) e Engenharia de Produto de Software (EPS), do curso Engenharia de Software da Faculdade UnB Gama (FGA) da Universidade de Brasília (UnB).
O projeto, a ser realizado pela equipe 8, composta por alunos das duas disciplinas, possui como objetivo auxiliar os alunos da universidade em dúvidas que eles tenham em relação ao desenvolvimento de jogos utilizando a linguagem em ascensão python. Isso envolve como obter dicas, guias a linguagem, tutoriais ao desenvolvimento de games, ferramentas necessárias e integração ao ambiente de desenvolvimento Jupyter. A partir da interação com o ChatBot, o usuário poderá requisitar destes serviços, ajudas, informes relacionados à linguagem python e sua biblioteca pygame.

## 1.3 Definições, acrônimos e abreviações

| Sigla | Definição |
| :--:|:------------------------:|
| UnB | Universidade de Brasília |
| FGA | Faculdade do Gama |
| MDS | Métodos de desenvolvimento de software |
| EPS | Engenharia do Produto de Software |

## 1.4 Referências

https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_6.0.5/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html

https://fga-eps-mds.github.io/2018.2-ComexStat/docs/docVisao

https://botlino.github.io/docs/doc-visao

## 1.5 Visão geral

Este documento descreve os detalhes sobre as características do software Ludum, especificando os problemas que estimularam a criação dessa solução em software. O documento se divide de maneira a separar as especificações e descrever as mesmas.

# 2.  Posicionando

## 2.1 Oportunidade de Negócios

Hoje em dia, muitas pessoas se interessam em aprender a desenvolver jogos e como Python é considerada uma linguagem de programação de fácil aprendizado, muitas vezes é escolhida por iniciantes como porta de entrada e como a biblioteca Pygame é uma das principais bibliotecas utilizadas para o desenvolvimento de jogos em Python é também muito escolhida para se iniciar.

## 2.2 Descrição do Problema

<table> 
<tr><th>O problema de</th><td>A dificuldade de um iniciante no aprendizado da biblioteca Pygame para o desenvolvimento de jogos.</td></tr>
<tr><th>Afeta</th><td>O entusiasmo no que diz respeito ao início dos estudos de desenvolvimento de jogos.</td></tr>
<tr><th>Cujo Impacto é</th><td>Menor chances da continuação dos estudos de desenvolvimento de jogos devido à frustração.</td></tr>
<tr><th>Uma boa solução seria</th><td>Um chatbot que de maneira simples e direta auxiliaria o aprendizado para o desenvolvimento de jogos baseados na linguagem de programação Python e em sua biblioteca Pygame.</td></tr>
</table>

## 2.3 Instrução de Posição do Produto

<table> 
<tr><th>Para</th><td>Estudantes da área de programação e pessoas interessadas no desenvolvimento de jogos.</td></tr>
<tr><th>Que</th><td>Buscam num software uma maneira prática e acessível de aprender e desenvolver um jogo na linguagem Python através da biblioteca  Pygame.</td></tr>
<tr><th>O Ludum</th><td>É um ChatBot.</td></tr>
<tr><th>Diferente de</th><td>Todas as opções disponíveis para aprender a desenvolver jogos usando a biblioteca pygame.</td></tr>
<tr><th>NossoProduto</th><td>Responde perguntas sobre o desenvolvimento de jogos em Python, e sua biblioteca Pygame. Além de facilitar o estudo por meio da integração ao ambiente Jupyter.</td></tr>
</table>

# 3. Descrições da Parte Interessada e do Usuário

## 3.1 Demográficos de Mercado

Os principais envolvidos neste projeto serão as equipes de desenvolvimento (MDS), gestores (EPS) e monitores, sendo que esses não necessariamente irão ser usuários do aplicativo.
O público-alvo do projeto, que irá interagir com o Ludum, são alunos da FGA, sejam eles de graduação ou pós-graduação.
Os principais artefatos que o Ludum propõe é a maior interatividade e facilidade para o desenvolvimento de pessoas não ligadas a software dentro da Universidade de Brasília.

## 3.2 Resumo dos envolvidos

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Equipe de desenvolvimento de software|Estudantes da Disciplina Métodos de Desenvolvimento de Software.|Desenvolvimento e Testes do Software descrito no documento.|
|Equipe de engenharia de produto de software|Estudantes da Disciplina Engenharia de Produto de Software.|Gestão da Equipe de Desenvolvimento, bem como manutenção de ambientes e entrega contínua.|
|Orientador|Professora na Universidade de Brasília, no campus Faculdade Gama (FGA - UnB), atual professora das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software.|Orientar as equipe de desenvolvimento e gestão em eventuais dúvidas.|

## 3.3 Resumo do Usuário

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Estudantes|Alunos da universidade de Brasília e interessados|Interagir com o Ludum por meio da plataforma Telegram, receber auxílio e sanar suas dúvidas sobre o desenvolvimento de jogos em python|

## 3.4 Principais Necessidades dos Usuários e dos Envolvidos

Os usuários realizarão a interação com o Ludum por meio do Telegram, serviço de mensagens instantâneas, para receberem instruções sobre o Pygame, além de poderem consultar sempre que tiverem dúvidas ou desejarem maiores esclarecimentos a respeito do desenvolvimento com Pygame.

## 3.5 Perfis das Partes Interessadas

## 3.5.1 Equipe de desenvolvimento de software

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Lucas Ganda, Wictor Girardi, João de Assis, João Pedro, Thallys Silva.</td></tr>
<tr><th>Descrição</th><td>Desenvolvimento de Software.</td></tr>
<tr><th>Tipo</th><td>Estudantes da Universidade de Brasília, da disciplina de Métodos de Desenvolvimento de Software.</td></tr>
<tr><th>Responsabilidades</th><td>Desenvolver, testar e implantar o software.</td></tr>
<tr><th>Critérios de Sucesso</th><td>Finalizar o desenvolvimento e realizar a entrega do bot no tempo estipulado.</td></tr>
<tr><th>Envolvimento</th><td>Alto.</td></tr>
<tr><th>Problemas/comentários</th><td>Desenvolver o software no tempo estabelecido pela equipe de EPS. Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o software.</td></tr>
</table>

## 3.5.2 Equipe de engenharia de produtos de software

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Guilherme Siqueira Brandão, Gabriela Chaves de Moraes, Lucas Arthur Lermen, Lucas Penido Antunes.</td></tr>
<tr><th>Descrição</th><td>Gerenciamento do Projeto.</td></tr>
<tr><th>Tipo</th><td>Estudantes da Universidade de Brasília, da disciplina de engenharia de produtos de software.</td></tr>
<tr><th>Responsabilidades</th><td>Monitorar, motivar, orientar e preparar a equipe de desenvolvimento. Definir prazos para as atividades propostas.</td></tr>
<tr><th>Critérios de Sucesso</th><td>Manter os prazos estabelecidos sem atraso, e gerenciar a qualidade do software em desenvolvimento, finalizando o projeto no tempo estipulado.</td></tr>
<tr><th>Envolvimento</th><td>Alto.</td></tr>
<tr><th>Problemas/comentários</th><td>Desenvolver o software no tempo estabelecido pela equipe de EPS. Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o software.</td></tr>
</table>

## 3.6 Perfil do Usuário

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Alunos da Universidade de Brasília, no campus Faculdade do Gama (FGA - UnB).</td></tr>
<tr><th>Descrição</th><td>Alunos que tenham interesse no desenvolvimento de jogos em python.</td></tr>
<tr><th>Tipo</th><td>Estudantes da FGA que tenham dúvidas e necessitem de ajuda com o desenvolvimento de jogos em python.</td></tr>
<tr><th>Responsabilidades</th><td>Interagir com o Ludum por meio da aplicação Telegram.
</td></tr>
<tr><th>Critérios de Sucesso</th><td>Desenvolver jogos com ajuda do bot Ludum</td></tr>
<tr><th>Envolvimento</th><td>Alto.</td></tr>
<tr><th>Problemas/comentários</th><td>Não possuir cadastro no Telegram.</td></tr>
</table>

## 3.7 Principais Necessidades da Parte Interessada ou do Usuário

| Necessidade| Prioridade | Preocupação | Solução proposta | Solução Atual |
|:----:|:---------:|:-----------------:|:------------------:|:------:|
|Sanar dúvidas que tangem o quesito de desenvolvimento de jogos em python|Alta|Falta de interação com o Ludum|Um ChatBot de Telegram que consiga auxiliar os universitários respondendo suas dúvidas e necessidades| Videos no youtube, Stackoverflow e sites de desenvolvimento|
|Ajudar a configuração de ambientes|Média|Falta de interação com o Ludum ou hardware antigo|Guias propostos pelo Ludum para auxiliar de maneira rápida a configuração do ambiente|Google e fóruns|
|Execução de códigos no Jupyter|Alta|Códigos mal digitados ou em outras linguagens|A identificação de códigos e a rápida execução e debug dentro do chat|Instalar a ferramenta Jupyter no computador|

## 3.8 Alternativas e Concorrência  

Não existem.

# 4. Visão Geral do Produto

## 4.1 Perspectiva do Produto  

 O ChatBot Ludum tem como objetivo auxiliar e tornar o desenvolvimento de jogos na tecnologia python uma atividade mais prazerosa, onde o usuário será guiado desde o nível básico da linguagem até o nível avançado onde será possível a criação de jogos mais complexos, isso tudo aliado ao auxílio para configuração do ambiente de trabalhos e de suas ferramentas necessárias.

## 4.2 Resumo das Capacidades

 *Resume os principais benefícios e recursos que o produto fornecerá. Por exemplo, um sistema de suporte ao cliente pode usar essa parte para endereçar a documentação do problema, o roteamento e o relato de status sem elaborar em detalhes o que essas funções requerem. Organize as funções de modo que a lista seja compreensível para o cliente ou para qualquer outra pessoa que leia o documento pela primeira vez. Uma simples tabela que lista os principais benefícios cujos recursos de suporte são suficientes, como no exemplo a seguir.*

<table> 
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
<tr><th> -- </th><td> -- </td></tr>
</table>

# 5. Recursos do Produto

O ChatBot Ludum é capaz de:

Realizar a integração entre bot, usuário e jupyter.
Ensinar noções básicas de python e como trabalhar com a biblioteca Pygame.
Dar dicas de como configurar o ambiente de desenvolvimento e aplicações úteis ao desenvolvimento para leigos.
Realizar o desenvolvimento de jogos de diferentes níveis de dificuldade de desenvolvimento.

# 6. Restrições

## 6.1 Restrições de implementação

O chatbot deverá ser implementado na linguagem Python, com API em Django Rest.

## 6.2 Restrições externas

Dentre as restrições externas as que mais irão influenciar são a inexperiência com a linguagem e frameworks, além de possíveis transtornos entre a equipe de desenvolvimento.

## 6.3 Restrições de confiabilidade

O sistema deverá ter cobertura de testes - mínimo de 90%.

# 7. Faixas de Qualidade

Para maior eficiência, a aplicação será mobile, sendo executada por meio da aplicação de comunicação Telegram, para uma forma segura e rápida de gerenciamento de dados e informações.

# 8. Requisitos do produto

## 8.1 Requisitos do Sistema

Esta aplicação deverá ser acessada através de dispositivos que possuem a aplicação Telegram em que o sistema operacional é variável de acordo com o dispositivo de utilização, podendo ser: Android, iOS, Windows, Linux, Chrome OS…

## 8.2 Requisitos de implementação

 Para maior eficiência, o Ludum será desenvolvido para ser utilizado em uma das maiores plataformas de comunicação Telegram, onde a implementação de funcionalidades se mostra viável.

## 8.3 Requisitos de design

A composição deste software será feita de maneira a tornar sua utilização autoexplicativa e fácil, para acesso em tempo real, ou seja, atendendo todas as especificações de boas práticas referentes à experiência de usuário.
