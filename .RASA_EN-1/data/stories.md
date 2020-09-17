## happy path
* greet
    - utter_greet
* request_consultation
    - consultation_form
    - form{"name": "consultation_form"}
    - form{"name": null}
    - utter_slots_values	
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* request_consultation
    - consultation_form
    - form{"name": "consultation_form"}	
* chitchat
    - utter_chitchat
    - consultation_form
    - form{"name": null}	
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* request_consultation
    - consultation_form
    - form{"name": "consultation_form"}	
* chitchat
    - utter_chitchat
    - consultation_form
* chitchat
    - utter_chitchat
    - consultation_form
* chitchat
    - utter_chitchat
    - consultation_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries	

## bot challenge
* bot_challenge
  - utter_iamabot