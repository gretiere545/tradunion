from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ConsultationForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "consultation_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["purpose","objective","age", "pain_yn", "pain_level"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "purpose": self.from_entity(entity="purpose", not_intent="chitchat"),
            "objective": self.from_entity(entity="objective", not_intent="chitchat"),
            "age": self.from_entity(entity="number", intent=["inform", "request_consultation","enter_age"]),
            "pain_level": self.from_entity(entity="pain_level", intent=["request_consultation","inform_pain_level"]),    
            "pain_yn": self.from_entity(entity="pain_yn", intent=["request_consultation","inform_pain_yn"]),              
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def purpose_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "medical",
            "dental",
            "surgery",
        ]

    @staticmethod
    def objective_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "consultation",
            "rendez-vous",
            "urgency",
        ]


    def pain_level_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "low",
            "medium",
            "high",
        ]
        
    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_purpose(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.purpose_db():
            # validation succeeded, set the value of the "purpose" slot to value
            # dispatcher.utter_message(template="utter_slots_values")
            return {"purpose": value}
        else:
            dispatcher.utter_message(template="utter_wrong_purpose")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"purpose": None}
            
    def validate_objective(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.objective_db():
            # validation succeeded, set the value of the "objective" slot to value
            # dispatcher.utter_message(template="utter_slots_values")
            return {"objective": value}
        else:
            dispatcher.utter_message(template="utter_wrong_objective")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"objective": None}            

    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate age value."""

        if self.is_int(value) and int(value) > 0:
            return {"age": value}
        else:
            dispatcher.utter_message(template="utter_wrong_age")
            # validation failed, set slot to None
            return {"age": None}
 
 
    def validate_pain_yn(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate outdoor_seating value."""

        if isinstance(value, str):
            if "yes" in value:
                # convert "out..." to True
                return {"pain_yn": True}
            elif "no" in value:
                # convert "in..." to False
                return {"pain_yn": False}
            else:
                dispatcher.utter_message(template="utter_wrong_pain_yn")
                # validation failed, set slot to None
                return {"pain_yn": None}

        else:
            # affirm/deny was picked up as T/F
            return {"pain_yn": value}
     
     
    def validate_pain_level(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate pain_level value."""
        return {"pain_level": value}
        # if any(tracker.get_latest_entity_values("pain_level")):
        # if value.lower() in self.pain_level_db():
            # return {"pain_level": value}
        # else:
            # dispatcher.utter_message(template="utter_wrong_age")
            # # validation failed, set slot to None
            # return {"pain_level": None}
            
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []        