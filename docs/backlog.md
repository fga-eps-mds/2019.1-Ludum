# Histórico de Versão

 **Data** | **Versão** | **Descrição** | **Autor(es)**
---|---|---|---
01/04/2019| 0.1| Criação da versão 1 do Backlog| Gabriela, Guilherme e Lucas Lermen
01/04/2019| 0.2| Pontuação e definição de novas histórias - Versão 1| Toda equipe
11/04/2019| 0.3| Adicionando nova história e criando versão 2| Gabriela Moraes
24/04/2019| 0.4| Criando versão 3| Gabriela Moraes, Guilherme e Lucas Lermen

## Sumário

1. [Versão 3](#_1-versão-3)
2. [Versão 2](#_2-versão-2)
3. [Versão 1](#_3-versão-1)


# **Backlog do Produto**

## 1. **Versão 3**
### **Épico Sobre o Ludum**

#### Feature 01 - Apresentar o Ludum e seu objetivo
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US01| <p align="justify">Eu, como usuário, desejo visualizar informações gerais sobre o Ludum assim que ele for inicializado</p> | Muito Alta | 3
US02| <p align="justify">Eu, como usuário, desejo visualizar um menu com todas as funções disponibilizadas pelo o Ludum</p> | Muito Alta | 3

#### Feature 02 - Contextualizar sobre as funções do Ludum
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US03 | <p align="justify">Eu, como usuário, desejo ver informações acerca do tutorial de instalação do PyGame</p>| Alta | 5
US04 | <p align="justify">Eu, como usuário, desejo saber mais a disponibilização de materiais</p> | Alta | 5
US05 | <p align="justify">Eu, como usuário, desejo compreender mais sobre o tópico de resolução de dúvidas</p>  | Alta | 5
US06 | <p align="justify">Eu, como usuário, desejo compreender sobre a funcionalidade de auxílio no desenvolvimento jogos</p> | Alta | 5
US16 | <p align="justify">Eu, como usuário, desejo compreender sobre a funcionalidade de contribuição com materiais, links e tutoriais</p> | Alta | 5

### **Épico Tutorial de Instalação**

#### Feature 03 - Coletar informações do ambiente do usuário
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US07 | <p align="justify">Eu, como usuário, desejo que o Ludum pergunte sobre o meu ambiente de desenvolvimento</p> | Muito Alta| 3
TS01 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do core da aplicação</p>|Muito Alta| 5
TS02 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do core da aplicação </p>| Muito Alta | 8
TS03 | <p align="justify">Eu, como desenvolvedor, desejo armazenar informações sobre o ambiente de desenvolvimento do usuário </p>| Alta | 5 

#### Feature 04 - Ensinar a instalar as dependências do PyGame
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US08| <p align="justify">Eu, como usuário, desejo que o Ludum indique quais dependências estão faltando no meu ambiente de desenvolvimento</p>| Muito Alta| 5
US09| <p align="justify">Eu, como usuário, desejo que o Ludum guie passo a passo como instalar essas dependências faltantes</p>| Muito Alta | 5

### **Épico Colaboração de Materiais, Links e Tutoriais**

#### Feature 10 - Criar estrutura do Microsserviço de Materiais, Links e Tutoriais
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS10 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do microsserviço de materiais, links e tutoriais</p>|Muito Alta| 3
TS11 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do microsserviço de materiais, links e tutoriais </p>| Muito Alta | 5
TS12| <p align="justify">Eu, como desenvolvedor, desejo criar a etapa de comunicação com o core do Ludum para o microsserviço de Materiais, Links e Tutoriais.</p>|Média| 5
TS13 | <p align="justify"> Eu, como desenvolvedor, desejo criar interface do webclient onde será feita a contribuição e aprovação das mesmas</p>|Muito Alta| 13
TS14| <p align="justify">Eu, como desenvolvedor, desejo conectar o Microsserviço de Materiais, Links e Tutoriais com o webclient.</p>|Média| 5

#### Feature 11 - Contribuir/Gerenciar com o conteúdo do Ludum
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US17 | <p align="justify"> Eu, como usuário, desejo cadastrar um tutorial</p>|Muito Alta| 13
US18 | <p align="justify"> Eu, como usuário, desejo cadastrar um link</p>|Muito Alta| 13
US19 | <p align="justify"> Eu, como usuário, desejo cadastrar um material</p>|Muito Alta| 13
TS15 | <p align="justify"> Eu, como desenvolvedor, desejo gerenciar o envio de materiais/links </p>|Muito Alta| 5
TS16 | <p align="justify"> Eu, como desenvolvedor, desejo gerenciar o envio de tutoriais </p>|Muito Alta| 5

### **Épico Recomendação de Materiais e Links**

#### Feature 05 - Apresentar materiais
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS04| <p align="justify">Eu, como desenvolvedor, desejo popular o banco com links e materiais interessantes</p>| Média| 3
US10| <p align="justify">Eu, como usuário, desejo que o Ludum recomende materiais e links úteis que possam complementar meu estudo</p>| Média | 3

### **Épico Resolução de dúvidas**

#### Feature 06 - Conectar à aplicação externa
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS17 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do microsserviço de conexão com o StackOverflow</p>|Muito Alta| 5
TS18 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do microsserviço de conexão com o StackOverflow </p>| Muito Alta | 8
TS06| <p align="justify">Eu, como desenvolvedor, desejo criar a etapa de comunicação com o core do Ludum para o microsserviço de Pesquisar Dúvidas.</p>|Média| 5
TS07| <p align="justify">Eu, como desenvolvedor, desejo comunicar o microsserviço de perguntas e respostas com o StackOverflow.</p>|Média| 13

#### Feature 07 - Apresentar FAQ
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS05| <p align="justify">Eu, como desenvolvedor, desejo popular com as perguntas mais frequentes o banco do microsserviço de conexão com o StackOverflow.</p>|Alta| 3 
US11| <p align="justify">Eu, como usuário, desejo visualizar as perguntas feitas com mais frequencia.</p>|Média| 3
US12| <p align="justify">Eu, como usuário, desejo pesquisar minha dúvida caso ela não esteja presente no FAQ.</p>|Média| 5

### **Épico Auxílio na criação de jogos**

#### Feature 08 - Criar jogo 
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS08| <p align="justify">Eu, como desenvolvedor, desejo criar um jogo de baixa complexidade para elaborar o tutorial</p>| Média| 13
TS09| <p align="justify">Eu, como desenvolvedor, desejo criar um jogo de complexidade um pouco mais alta para elaborar o tutorial</p>| Média| 13
US13| <p align="justify">Eu, como usuário, desejo selecionar a complexidade do jogo em que receberei auxílio</p>| Média | 2 
US14| <p align="justify">Eu, como usuário, desejo aprender a criar um jogo de baixa complexidade</p>| Baixa| 13
US15| <p align="justify">Eu, como usuário, desejo aprender a criar um jogo de complexidade um pouco mais alta</p>| Baixa| 13
US20| <p align="justify">Eu, como usuário, desejo escolher um tutorial da comunidade</p>| Baixa| 2

### **Épico Notificar sobre adição de novos materiais/links e tutoriais**

#### Feature 09 - Enviar email de notificação em relação à novidades para o usuário 
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS19| <p align="justify">Eu, como desenvolvedor, desejo criar o microsserviço de Notificações </p>| -| 5
TS20| <p align="justify">Eu, como desenvolvedor, desejo conectar o microsserviço de Noticações com o core do Ludum </p>| -| 5
TS21| <p align="justify">Eu, como desenvolvedor, desejo conectar o microsserviço de Notificações com a API do Gmail </p>| -| 5
US21| <p align="justify">Eu, como usuário, desejo receber um email informando sobre as novidades adicionadas </p>| -| 5

## 2. **Versão 2**
- [Versão 2 do Backlog](/backlog-versao2.md)

## 3. **Versão 1**
- [Versão 1 do Backlog](/backlog-versao1.md)