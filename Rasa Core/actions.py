# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hey there I am your MEDBOT 👨🏽‍⚕️, How may I help you today")

        return [UserUtteranceReverted()] 

class ActionDynamicLink(Action):
    def name(self) -> Text:
        return "action_dynamic_link"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link="https://www.ge.com/digital/need-technical-help"
        # dispatcher.utter_message(text="Hello World!")
        
        dispatcher.utter_template("utter_canthelp",tracker,link=Link)
        return []