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