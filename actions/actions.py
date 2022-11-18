# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

from .connect_sqldb import save_to_db

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:

        # tell the user they are being passed to a customer service agent
        dispatcher.utter_message(text="I am passing you to a human...")
     
        # pause the tracker so that the bot stops responding to user input
        return [UserUtteranceReverted()]


class ActionMakeEnrollment(Action):

    def name(self) -> Text:
        return "action_make_enrollment"

    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of requried slots that the form has to fill"""
        return ["fill_name", "email", "gender", "course_intake_value"]
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domainL: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:

        full_name = tracker.get_slot("full_name")
        email = tracker.get_slot("email")
        gender = tracker.get_slot("gender")
        course_intake_value = tracker.get_slot("course_intake_value")

        save_to_db(full_name, email, gender, course_intake_value)

        dispatcher.utter_message(text="You have been successfully enrolled. You will see an email with other details.")

        return []

# class ActionTagFeedback(Action):
#     """Tag a conversation in Rasa X as positive or negative feedback"""

#     def name(self):
#         return "action_tag_feedback"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         feedback = tracker.get_slot("feedback_value")

#         if feedback == "positive":
#             label = '[{"value":"postive feedback","color":"76af3d"}]'
#         elif feedback == "negative":
#             label = '[{"value":"negative feedback","color":"ff0000"}]'
#         else:
#             return []

#         return []
