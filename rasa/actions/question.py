from rasa_core_sdk import Action
import requests


class ActionQuestion(Action):
    def name(self):
        return "action_question"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Estou pesquisando todas as perguntas pesquisadas para você, amiguinhx!')
        try:
            requests.get(
                f'https://ludum-duvidas.herokuapp.com/api/duvidas',
                timeout=3
            )
            data = {
                'text': 'Essas são as perguntas que eu consegui recuperar para você:',
                'text': f'https://ludum-duvidas.herokuapp.com/api/duvidas'
            }
            dispatcher.utter_response(data)
        except ValueError:
            dispatcher.utter_message(ValueError)
