'''Creating translator instance and creating english to french and french to english functions'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-08-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''This function translates the english text to french'''
    try:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except ValueError:
        return None

def frenchToEnglish(french_text):
    '''This function translates the french text to english'''
    try:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except ValueError:
        return None
