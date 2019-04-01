# Histórico de Versão

 **Data** | **Versão** | **Descrição** | **Autor(es)**
---|---|---|---
31/03/2019 | 0.1 | Iniciação | Lucas Penido
01/04/2019 | 0.2 | Definição das tecnologias e padrão arquitetural | Lucas Penido

# Iniciando Documento de Arquitetura

## Padrão Arquitetural:

Nosso projeto deve conter microsserviços, com isso a utilziação de APIs.

O padrão arquitetetural que será utilziado é o Broker, sua arquitetura lida muito bem com sistemas distribuidos, assim como microsserviços.  

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
https://github.com/fga-eps-mds/2017.2-MerendaMais/wiki/Documento-de-Arquitetura  
