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
 15-detect-credit_card
                         anonymize_text('My NRP is Unknown', ['NRP']))
       
    def test_credit_card(self):
        """Test to make sure CREDIT_CARD is recognized"""
        #Positive Test Case 
        sec1 = '5105'
        sec2 = '1051'
        sec3 = '0510'
        sec4 = '5100'
        test_cc = sec1 + sec2 + sec3 + sec4
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is <CREDIT_CARD>'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,actual_result) 

        #Negative Test Case - Credit Card Number invalid
        test_cc = '1232 8324 3847 3488' 
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324 3847 3488'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,actual_result)

        #Negative Test Case - Credit Card Number too short
        test_cc = '1232 8324' 
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,actual_result)

        #Negative Test Case - Credit Card Number too long: beyond 19 digits
        test_cc = '1232 8324 3453 2353 6575 2344' 
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1232 8324 3453 2353 6575 2344'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,actual_result)

        #Negative Test Case - Credit Card Number contains non numerical characterss
        test_cc = '1242 y348 jh28 2343' 
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is 1242 y348 jh28 2343'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,actual_result)

    
                         anonymize_text('My NRP is Unknown', ['NRP']))   
    
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
 main
