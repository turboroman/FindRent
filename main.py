from os import environ
from ZillowAnalyzer import ZillowAnalyzer
from RentingForm import RentingForm
from time import sleep

FORM_URL = environ.get('FORM_URL')
# RESPONSES_URL = environ.get('https://docs.google.com/forms/d/1Xx4laPyluM2Mvcqi0R59nzF6-rZnk5uQBbuaUiBx1vY/edit#responses')
ZILLOW_URL = environ.get('ZILLOW_URL')

zillow_analyzer = ZillowAnalyzer()
properties_list = zillow_analyzer.get_properties(ZILLOW_URL)

renting_form = RentingForm()

for prop in properties_list:
    renting_form.fill_form(FORM_URL, prop)
    sleep(3)

# renting_form.create_sheet(RESPONSES_URL)




