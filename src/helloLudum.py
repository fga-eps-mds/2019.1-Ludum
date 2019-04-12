import telebot
import logging

from subprocess import call

# log settings
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

#Criar o bot
token = open('tolken.txt', 'r').read()
ludumBot = telebot.TeleBot(token)

#Texto de inicio

inicio_string = []
inicio_string.append("Olá, eu sou o Ludum! :D\n" +
                     "Vou te mostrar tudo que sei sobre desenvolvimento de jogos em Python!\n"+
                     "Mas antes, jovem padawan, devo te fazer uma pergunta: Você já conhece minhas funcionalidades?")

@ludumBot.message_handler(commands=['start'])
def send_start(mensagem):
    ludumBot.send_message(mensagem.chat.id,inicio_string,)
ludumBot.polling()
