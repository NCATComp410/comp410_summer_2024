"""PII Scan"""
import uuid
import os
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.predefined_recognizers import (ItDriverLicenseRecognizer,
                                                      ItVatCodeRecognizer,
                                                      ItFiscalCodeRecognizer,
                                                      ItIdentityCardRecognizer,
                                                      ItPassportRecognizer,
                                                      EsNifRecognizer,
                                                      PlPeselRecognizer)
from presidio_anonymizer import AnonymizerEngine

# make sure en_core_web_lg is loaded correctly
# this can also be achieved with
# python -m spacy download en_core_web_lg
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Create an analyzer object
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
# Add some language specific recognizers as english instead of default language
registry.add_recognizer(ItDriverLicenseRecognizer(supported_language='en'))
registry.add_recognizer(ItVatCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItFiscalCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItIdentityCardRecognizer(supported_language='en'))
registry.add_recognizer(ItPassportRecognizer(supported_language='en'))
registry.add_recognizer(EsNifRecognizer(supported_language='en'))
registry.add_recognizer(PlPeselRecognizer(supported_language='en'))
analyzer = AnalyzerEngine(registry=registry)
anonymizer = AnonymizerEngine()


def show_aggie_pride() -> str:
    """Show Aggie Pride"""
    return "Aggie Pride - Worldwide"


def generate_uuid():
    """Generate a UUID"""
    return uuid.uuid4()


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    :param text: the text to be anonymized
    :param entity_list: the list of entities to be anonymized
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en')

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return anonymized_text.text


if __name__ == '__main__':
    print(show_aggie_pride())
    print('-----------------')
    print('Sample text: I live in New York')
    print('Anonymized text:', anonymize_text('I live in New York', ['LOCATION']))
    print('-----------------')
    print('UUID: ', generate_uuid())
    print('CODESPACE_NAME:', os.getenv('CODESPACE_NAME'))
