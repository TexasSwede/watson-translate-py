from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')


def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return englishText