
from rasa_core_sdk import Action
import json
import requests
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction

url = 'https://produ-o.ludum-materiais.ludumbot.club'


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Mensagem enviada por uma custom aaaa')
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


class ActionQuestion(FormAction):
    def name(self):
        return "action_question"

    @staticmethod
    def required_slots(tracker):
        return ["pergunta"]

    def submit(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Espere jovem padawan,' +
                                     'vou procurar uma resposta' +
                                     'no Stack Overflow para você')
        except ValueError:
            dispatcher.utter_message(ValueError)
        try:
            pergunta = str(tracker.get_slot('pergunta'))
            api = url + '/api/duvidas'
            apiPergunta = api + '/pesquisar' + '/:{' + pergunta + '}'
            link = requests.get(apiPergunta)
            stack = json.loads(link.text)
            utterString = ''
            if(len(stack['data']['answer']) == 0):
                utterString += ('Que pena... Nem mesmo os grandes' +
                                ' mestres Jedi do stack' +
                                ' overflow sabem a resposta para sua ' +
                                'pergunta.\nQue tal perguntar de outra forma?')
            else:
                for i in range(0, len(stack['data']['answer'])):
                    utterString += 'Resposta ' + str(i + 1) + '\n'
                    utterString += 'Titulo: '
                    utterString += (str(stack['data']['answer'][i]['title']))
                    utterString += '\n'
                    utterString += 'Link: '
                    utterString += str(stack['data']['answer'][i]['link'])
                    utterString += '\n'
                dispatcher.utter_message(utterString)
                stringFinal = "Esses são os links mais uteis que eu encontrei"
                stringFinal += "\nEspero ter te ajudado!"
                stringFinal += " Se tiver Qualquer outra duvida"
                stringFinal += " estou aqui pra auxilia-lo!"
                dispatcher.utter_message(stringFinal)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet('pergunta', None)]

    def slot_mappings(self):
        return {
            "pergunta": self.from_text()
        }


class ActionFaq(Action):
    def name(self):
        return "action_faq"

    def run(self, dispatcher, tracker, domain):
        try:
            string = ''
            f = open('../rasa/actions/faq/perguntas_faq.txt', 'r')
            string = f.read()
            f.close()
            dispatcher.utter_message(string)
            finalizar = 'Se não tiver encontrado sua pergunta'
            finalizar += ' aqui, posso fazer uma pesquisa no stack overflow'
            dispatcher.utter_message(finalizar)
            dispatcher.utter_message('Deseja que eu faça isso?')
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


class ActionTutoriais(Action):
    def name(self):
        return "action_tutoriais"

    def run(self, dispatcher, tracker, domain):
        try:
            api = url + '/api/tutoriais/aprovados/S/'
            link = requests.get(api)
            tutoriais = json.loads(link.text)
            utterString = ''
            for i in range(0, len(tutoriais['data'])):
                utterString += str(i) + ")"
                utterString += str(tutoriais['data'][i]['name'])
                utterString += '\n'

        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
