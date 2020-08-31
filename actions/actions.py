
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from rasa_sdk.executor import CollectingDispatcher
from .helpers import *

class ReactToComplain(Action):
    def name(self) -> Text:
        return "action_react_to_complain"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        specialist = specialist_mapping[tracker.get_slot('part_of_body')]
        dispatcher.utter_message(text=f"I'm looking at the schedule of {specialist}")
        dispatcher.utter_message(text="Schedule of specialist is found. What Should we do next?",
                                 buttons=[{"title": "Make an appointment", "payload":"/show_avaliabe_dates"},
                                          {"title": "Make a house call", "payload":"/make_house_call"}])
        return [SlotSet('specialist', specialist),
                SlotSet('address', medical_structure_address)]

class MakeHouseCall(Action):
    def name(self) -> Text:
        return "action_make_house_call"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Please, write your address.")
        return []

class ShowAvailableDates(Action):
    def name(self) -> Text:
        return "action_show_avaliabe_dates"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
         spec = tracker.get_slot('specialist')
         dates = AVAILABLE_TIMETABLE[spec]['dates']
         buttons_list = [{"title":available_date, "payload":f"""/store_date{{"date":"{available_date}"}}"""}
                         for available_date in dates]
         dispatcher.utter_message(text="Available dates: ", buttons=buttons_list)
         return []

class StoreDate(Action):
    def name(self) -> Text:
        return "action_store_date"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"You chose date: {tracker.get_slot('date')}")
        return []


class ShoWAvailableTimeSlots(Action):
    def name(self) -> Text:
        return "action_show_available_time_slots"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        buttons_list = [
            {"title": str(available_time), "payload": f"""/store_time{{"time":"{str(available_time)}"}}"""}
            for available_time in AVAILABLE_TIMETABLE[tracker.get_slot('specialist')]['time_slots']]
        dispatcher.utter_message(text="Available time slots: ", buttons=buttons_list)
        return []

class StoreDate(Action):
    def name(self) -> Text:
        return "action_store_time"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_appointment_card")
        return []