import telebot
import logging

# log settings
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Criar o bot
token = open('token.txt', 'r').read()
ludumBot = telebot.TeleBot(token)

# Texto de inicio

inicio_string = []
inicio_string.append("Olá, eu sou o Ludum! :D\n" +
                     "Vou te mostrar tudo que sei sobre "
                     " desenvolvimento de jogos em Python!\n" +
                     "Mas antes, jovem padawan, devo te fazer uma pergunta:"
                     " Você já conhece minhas funcionalidades?")

menu_string = []
menu_string.append("1) Tutorial: Vamos construir um jogo juntos!" +
                   " Vou te ensinar sobre o desenvolvimento de jogos"
                   "em Python desde as partes mais básicas" +
                   " e quando você perceber já estará"
                   " jogando seu próprio jogo!\n" +
                   "2) Ambiente: "
                   "Irei te auxiliar a preparar todo"
                   " seu ambiente de desenvolvimento"
                   "com os programas adequados.\n" +
                   "3) FAQ: Tentarei sanar todas as duvidas"
                   " que você pode vir a ter.\n" +
                   "4) Materiais e links: "
                   "Tentarei te enviar links e materiais que"
                   " possam ser utéis para você.\n" +
                   "Começar com o que, devemos?")


@ludumBot.message_handler(commands=['start'])
def send_start(mensagem):
    ludumBot.send_message(mensagem.chat.id, inicio_string, )
    ludumBot.send_message(mensagem.chat.id, menu_string, )


ludumBot.polling()
