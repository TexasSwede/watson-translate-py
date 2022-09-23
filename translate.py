from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    # Check for null or blank string
    if englishText == None:
        return None
    if englishText == "":
        return ""
    # Perform translation from English to French
    translationJSON = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translationJSON[0].translations
    return frenchText

def frenchToEnglish(frenchText):
    # Check for null or blank string
    if frenchText == None:
        return None
    if frenchText == "":
        return ""
    # Perform translation from French to English
    translationJSON = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translationJSON[0].translations
    return englishText