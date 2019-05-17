
from rasa_core_sdk import Action
import json
import requests
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction

class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Mensagem enviada por uma custom action')
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
            pergunta = str(tracker.get_slot('pergunta'))
            api = 'https://ludum-duvidas.herokuapp.com/api/duvidas'
            apiPergunta = api + '/pesquisar' + '/:{' + pergunta + '}'
            dispatcher.utter_message('Espere jovem padawan,' +
                                     'vou procurar uma resposta' +
                                     'no Stack Overflow para você')
        except ValueError:
            dispatcher.utter_message(ValueError)
        try:
            link = requests.get(apiPergunta)
            stack = json.loads(link.text)
            utterString = ''
            if(len(stack['data']['answer']) == 0):
                utterString += ('Que pena... Nem mesmo os grandes' +
                                ' mestres Jedi do stack' +
                                ' overflow sabem a resposta para sua' +
                                ' pergunta. \nQue tal perguntar de outra forma?')
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
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet('pergunta', None)]
    def slot_mappings(self):

        return {
            "pergunta":self.from_text()
        }