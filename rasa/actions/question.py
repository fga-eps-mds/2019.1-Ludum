from rasa_core_sdk import Action
import requests


class ActionQuestion(Action):
    def name(self):
        return "action_question"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Pesquisando perguntas pesquisadas para você')
        try:
            requests.get('https://ludum-duvidas.herokuapp.com/api/duvidas')
            data = {
                'text': 'https://ludum-duvidas.herokuapp.com/api/duvidas'
            }
            dispatcher.utter_response(data)
        except ValueError:
            dispatcher.utter_message(ValueError)
