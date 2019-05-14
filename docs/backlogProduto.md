# Histórico de Versão

 **Data** | **Versão** | **Descrição** | **Autor(es)**
---|---|---|---
01/04/2019| 0.1| Criação da versão 1 do Backlog| Gabriela, Guilherme e Lucas Lermen
01/04/2019| 0.2| Pontuação e definição de novas histórias - Versão 1| Toda equipe
11/04/2019| 0.3| Adicionando nova história e criando versão 2| Gabriela Moraes
24/04/2019| 0.4| Criando versão 3| Gabriela Moraes, Guilherme e Lucas Lermen
02/05/2019| 0.5| Ajustes versão 3| Gabriela Moraes e Lucas Lermen
13/05/2019| 0.6| Criação da Versão 4| Gabriela Moraes

## Sumário

1. [Versão 4](#_1-versão-4)
1. [Versão 3](#_2-versão-3)
2. [Versão 2](#_3-versão-2)
3. [Versão 1](#_4-versão-1)


# **Backlog do Produto**

## 1. **Versão 4**
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
US04 | <p align="justify">Eu, como usuário, desejo saber mais a disponibilização de links</p> | Alta | 5
US05 | <p align="justify">Eu, como usuário, desejo compreender mais sobre o tópico de resolução de dúvidas</p>  | Alta | 5
US06 | <p align="justify">Eu, como usuário, desejo compreender sobre a funcionalidade de auxílio no desenvolvimento jogos</p> | Alta | 5
US16 | <p align="justify">Eu, como usuário, desejo compreender sobre a funcionalidade de contribuição com links e tutoriais</p> | Alta | 5

### **Épico Recomendação de Links**

#### Feature 03 - Apresentar Links
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US10| <p align="justify">Eu, como usuário, desejo que o Ludum recomende links úteis que possam complementar meu estudo</p>| Baixa | 3
US08| <p align="justify">Eu, como usuário, desejo que o Ludum me informe sobre a possibilidade de contribuição com links.</p>| Baixa | 3

#### Feature 04 - Criar estrutura do Microsserviço de Links e Tutoriais
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS10 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do microsserviço de links e tutoriais.</p>|Média| 3
TS11 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do microsserviço de links e tutoriais. </p>| Média | 5
TS04| <p align="justify">Eu, como desenvolvedor, desejo popular o banco com links interessantes</p>| Baixa| 3
TS14| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint para acesso aos links.</p>|Média| 5
TS15| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint para acesso aos tutoriais.</p>|Média| 5
TS03| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint que permite armazenar novos links.</p>|Média| 5
TS05| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint que permite edição de um link.</p>|Média| 5
TS12| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint que permite edição de um tutorial.</p>|Média| 5
TS13| <p align="justify">Eu, como desenvolvedor, desejo criar um endpoint que permite armazenar novos tutoriais.</p>|Média| 5


### **Épico Colaboração de Links e Tutoriais**

#### Feature 05 - Contribuir com o conteúdo do Ludum
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US17 | <p align="justify"> Eu, como usuário, desejo cadastrar um tutorial</p>| Alta | 8
US18 | <p align="justify"> Eu, como usuário, desejo cadastrar um link</p>| Média | 8

#### Feature 06 - Gerenciar os novos conteúdos
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US09 | <p align="justify"> Eu, como administrador, desejo gerenciar o envio de links </p>| Baixa| 5
US19 | <p align="justify"> Eu, como administrador, desejo gerenciar o envio de tutoriais </p>| Baixa | 5

### **Épico Resolução de dúvidas**

#### Feature 07 - Conectar à aplicação externa
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS17 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do microsserviço de conexão com o StackOverflow</p>|Muito Alta| 5
TS18 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do microsserviço de conexão com o StackOverflow </p>| Muito Alta | 8
TS06| <p align="justify">Eu, como desenvolvedor, desejo criar a etapa de comunicação com o core do Ludum para o microsserviço de Pesquisar Dúvidas.</p>|Muito Alta| 5
TS07| <p align="justify">Eu, como desenvolvedor, desejo comunicar o microsserviço de perguntas e respostas com o StackOverflow.</p>|Muito Alta| 13

#### Feature 08 - Apresentar FAQ
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US11| <p align="justify">Eu, como usuário, desejo visualizar as perguntas feitas com mais frequência.</p>|Alta| 3
US12| <p align="justify">Eu, como usuário, desejo pesquisar minha dúvida no StackOverflow caso ela não esteja presente no FAQ.</p>|Alta| 5

### **Épico Auxílio na criação de jogos**

#### Feature 09 - Criar jogo 
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
US07| <p align="justify">Eu, como usuário, desejo que o Ludum pergunte sobre o meu ambiente de desenvolvimento.</p>| Muito Alta | 3 
US24| <p align="justify">Eu, como usuário, desejo receber uma lista de recomendações em relação a ferramentas de desenvolvimento.</p>| Média| 3
TS08| <p align="justify">Eu, como desenvolvedor, desejo criar um jogo de baixa complexidade para elaborar o tutorial</p>| Alta | 8
TS09| <p align="justify">Eu, como desenvolvedor, desejo criar um jogo de complexidade um pouco mais alta para elaborar o tutorial</p>| Alta | 13
US13| <p align="justify">Eu, como usuário, desejo selecionar a complexidade do jogo em que receberei auxílio</p>| Média | 2 
US14| <p align="justify">Eu, como usuário, desejo aprender a criar um jogo de baixa complexidade</p>| Média | 8
US15| <p align="justify">Eu, como usuário, desejo aprender a criar um jogo de complexidade um pouco mais alta</p>| Média| 8
US20| <p align="justify"> Eu, como usuário, desejo visualizar os tutoriais da comunidade disponíveis </p>| Média | 2
US22| <p align="justify"> Eu, como usuário, desejo acessar um tutorial da comunidade</p>| Média | 2

### **Épico Notificar sobre adição de novos links e tutoriais**

#### Feature 10 - Enviar email de notificação em relação à novidades para o usuário 
**ID**|**Descrição**|**Prioridade**| **Pontos**
:---:|:---|:---:|:---:
TS01 | <p align="justify"> Eu, como desenvolvedor, desejo modelar o banco de dados do core da aplicação</p>| Baixa | 5
TS02 | <p align="justify">Eu, como desenvolvedor, desejo implementar o banco de dados do core da aplicação </p>| Baixa | 8
US23 | Eu, como usuário, desejo que meu email seja cadastrado para receber notificações de adição de conteúdo | Baixa | 3
TS19| <p align="justify">Eu, como desenvolvedor, desejo conectar a API do Gmail ao microsserviço de links e tutoriais </p>| Baixa | 5
US21| <p align="justify">Eu, como usuário, desejo receber um email informando sobre as novidades adicionadas </p>| Baixa | 5

## 2. **Versão 3**
- [Versão 3 do Backlog](/backlog-versao3.md)

## 3. **Versão 2**
- [Versão 2 do Backlog](/backlog-versao2.md)

## 4. **Versão 1**
- [Versão 1 do Backlog](/backlog-versao1.md)