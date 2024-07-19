"""Tests for Team3"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestTeam3(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_nrp(self):
        """Test to make sure NRP is anonymized"""
        self.assertEqual('My nationality is <NRP>',
                         anonymize_text('My nationality is American', ['NRP']))

        self.assertEqual('My NRP is Unknown',

                         anonymize_text('My NRP is Unknown', ['NRP']))
      
      # 21-detect-iban_code
    def test_iban_code(self):
        """Test to make sure a IBAN_CODE is recognizable"""
        # positive test case
        country_code = 'BR' # Brazil country code
        check_digits = '97'
        bban = '00360305000010009795493P1'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is <IBAN_CODE>'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # positive test case
        country_code = 'DE' # Germany country code
        check_digits = '89'
        bban = '370400440532013000'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is <IBAN_CODE>'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - incorrect country code requiring different pattern length
        country_code = 'FR' # France country code
        check_digits = '89'
        bban = '370400440532013000'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is FR89370400440532013000'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - too short
        country_code = 'GB' # United Kingdom country code
        check_digits = '29'
        bban = 'NWBK6016133192681'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is GB29NWBK6016133192681'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - too long
        country_code = 'GB' # United Kingdom country code
        check_digits = '29'
        bban = 'NWBK601613319268192'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is GB29NWBK601613319268192'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)
    
    def test_crypto(self):
        """Test to make sure a Crypto is recognized and anonymized"""
        
        # Positive test case 1: Bitcoin address should be anonymized
        test_bitcoin_address_1 = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
        expected_anonymized_result_1 = 'My Bitcoin address is <CRYPTO>'
        actual_anonymized_result_1 = anonymize_text(f'My Bitcoin address is {test_bitcoin_address_1}', ['CRYPTO'])
        self.assertEqual(expected_anonymized_result_1, actual_anonymized_result_1,
                        f"Expected: {expected_anonymized_result_1}, but got: {actual_anonymized_result_1}")

        # Positive test case 2: Another Bitcoin address should be anonymized
        test_bitcoin_address_2 = '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy'
        expected_anonymized_result_2 = 'My Bitcoin address is <CRYPTO>'
        actual_anonymized_result_2 = anonymize_text(f'My Bitcoin address is {test_bitcoin_address_2}', ['CRYPTO'])
        self.assertEqual(expected_anonymized_result_2, actual_anonymized_result_2,
                        f"Expected: {expected_anonymized_result_2}, but got: {actual_anonymized_result_2}")

        # Negative test case 1: No crypto information, text should remain unchanged
        non_crypto_text_1 = 'No cryptocurrency mentioned here.'
        expected_unchanged_result_1 = 'No cryptocurrency mentioned here.'
        actual_unchanged_result_1 = anonymize_text(non_crypto_text_1, ['CRYPTO'])
        self.assertEqual(expected_unchanged_result_1, actual_unchanged_result_1,
                        f"Expected: {expected_unchanged_result_1}, but got: {actual_unchanged_result_1}")

        # Negative test case 2: Another non-crypto text should also remain unchanged
        non_crypto_text_2 = 'This text does not contain any cryptocurrency.'
        expected_unchanged_result_2 = 'This text does not contain any cryptocurrency.'
        actual_unchanged_result_2 = anonymize_text(non_crypto_text_2, ['CRYPTO'])
        self.assertEqual(expected_unchanged_result_2, actual_unchanged_result_2,
                        f"Expected: {expected_unchanged_result_2}, but got: {actual_unchanged_result_2}")
        
from presidio_analyzer import AnalyzerEngine

class TestEmailDetection(unittest.TestCase):
    """Test to make sure email addresses are recognized and anonymized"""

    def setUp(self):
        self.analyzer = AnalyzerEngine()

    def anonymize_text(self, text, entities):
        results = self.analyzer.analyze(text=text, language='en')
        for result in results:
            if result.entity_type in entities:
                text = text[:result.start] + f'<{result.entity_type}>' + text[result.end:]
        return text

    def test_email(self):
        # Positive test case 1: Email address should be anonymized
        test_email_1 = 'support@example.com'
        expected_anonymized_result_1 = 'My email address is <EMAIL_ADDRESS>'
        actual_anonymized_result_1 = self.anonymize_text(f'My email address is {test_email_1}', ['EMAIL_ADDRESS'])
        self.assertEqual(expected_anonymized_result_1, actual_anonymized_result_1,
                         f"Expected: {expected_anonymized_result_1}, but got: {actual_anonymized_result_1}")

        # Positive test case 2: Another email address should be anonymized
        test_email_2 = 'contact@company.org'
        expected_anonymized_result_2 = 'My email address is <EMAIL_ADDRESS>'
        actual_anonymized_result_2 = self.anonymize_text(f'My email address is {test_email_2}', ['EMAIL_ADDRESS'])
        self.assertEqual(expected_anonymized_result_2, actual_anonymized_result_2,
                         f"Expected: {expected_anonymized_result_2}, but got: {actual_anonymized_result_2}")

        # Negative test case 1: No email information, text should remain unchanged
        non_email_text_1 = 'No email address mentioned here.'
        expected_unchanged_result_1 = 'No email address mentioned here.'
        actual_unchanged_result_1 = self.anonymize_text(non_email_text_1, ['EMAIL_ADDRESS'])
        self.assertEqual(expected_unchanged_result_1, actual_unchanged_result_1,
                         f"Expected: {expected_unchanged_result_1}, but got: {actual_unchanged_result_1}")

        # Negative test case 2: Another non-email text should also remain unchanged
        non_email_text_2 = 'This text does not contain any email address.'
        expected_unchanged_result_2 = 'This text does not contain any email address.'
        actual_unchanged_result_2 = self.anonymize_text(non_email_text_2, ['EMAIL_ADDRESS'])
        self.assertEqual(expected_unchanged_result_2, actual_unchanged_result_2,
                         f"Expected: {expected_unchanged_result_2}, but got: {actual_unchanged_result_2}")

if __name__ == '__main__':
    unittest.main()
