from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core_sdk import Action


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)

class ActionAmbiente(Action):
    def name(self):
        return "action_ambiente"

    def run(self, dispatcher, tracker, domain):
        interpreter = Interpreter.load('./models/nlu/current')
        tutorial = 0
        while(tutorial<3):
            if(tutorial==0):
                try: 
                    disptacher.utter_message("Você já tem o python 3.6")
                    FollowupAction("action_listen")
                    if(interpreter.parse(dispatcher.tracker.latest_message.text) == interpreter.parse("Sim")):
                        dispatcher.utter_message("UHuuu")
                        tutorial+=1
                    else:
                        disptacher.utter_message("Aff")
                except ValueError:
                    dispatcher.utter_message(ValueError)