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

    def test_ip_address(self):
        """"Test to make sure a IP Adress is recognized"""
        # positive test case
        # prefix = '192'
        # mid = '.158.'
        # ending = '38'
        # test_ipv4 = prefix + mid + ending
        test_ipv4 = '192.168.1.1'
        test_string = 'My IPv4 Address is: ' + test_ipv4
        expected_result = 'My IPv4 Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # negative test case
        test_ipv4 = '12345'
        test_string = 'My IPv4 Address is: ' + test_ipv4
        expected_result = 'My IPv4 Address is: 12345'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # Positive test case-Class A
        test_classa = '10.5.6.7'
        test_string = 'My IP class A Address is: ' + test_classa
        expected_result = 'My IP class A Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # Positive test case-Class B
        test_classb = '123.45.67.89'
        test_string = 'My IP class A Address is: ' + test_classb
        expected_result = 'My IP class A Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # Positive test case-Class C
        test_classc = '192.168.1.100'
        test_string = 'My IP class C Address is: ' + test_classc
        expected_result = 'My IP class C Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # Positive test case-Class D
        test_classd = '224.0.0.1'
        test_string = 'My IP class D Address is: ' + test_classd
        expected_result = 'My IP class D Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        # Positive test case-Class E
        test_classe = '250.1.3.4'
        test_string = 'My IP class E Address is: ' + test_classe
        expected_result = 'My IP class E Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)

    def test_credit_card(self):
        """Test to make sure CREDIT_CARD is recognized"""
        # Positive Test Case
        sec1 = '5105'
        sec2 = '1051'
        sec3 = '0510'
        sec4 = '5100'
        test_cc = sec1 + sec2 + sec3 + sec4
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is <CREDIT_CARD>'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result, actual_result)

        # Negative Test Case - Credit Card Number invalid
        test_cc = '1232 8324 3847 3488'
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324 3847 3488'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result, actual_result)

        # Negative Test Case - Credit Card Number too short
        test_cc = '1232 8324'
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result, actual_result)

        # Negative Test Case - Credit Card Number too long: beyond 19 digits
        test_cc = '1232 8324 3453 2353 6575 2344'
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324 3453 2353 6575 2344'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result, actual_result)

        # Negative Test Case - Credit Card Number contains non numerical characterss
        test_cc = '1242 y348 jh28 2343'
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1242 y348 jh28 2343'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result, actual_result)

    def test_iban_code(self):
        """Test to make sure a IBAN_CODE is recognizable"""
        # positive test case
        country_code = 'BR'  # Brazil country code
        check_digits = '97'
        bban = '00360305000010009795493P1'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is <IBAN_CODE>'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # positive test case
        country_code = 'DE'  # Germany country code
        check_digits = '89'
        bban = '370400440532013000'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is <IBAN_CODE>'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - incorrect country code requiring different pattern length
        country_code = 'FR'  # France country code
        check_digits = '89'
        bban = '370400440532013000'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is FR89370400440532013000'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - too short
        country_code = 'GB'  # United Kingdom country code
        check_digits = '29'
        bban = 'NWBK6016133192681'
        test_iban = country_code + check_digits + bban
        test_string = 'My iban code is ' + test_iban
        expected_result = 'My iban code is GB29NWBK6016133192681'
        actual_result = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - too long
        country_code = 'GB'  # United Kingdom country code
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
