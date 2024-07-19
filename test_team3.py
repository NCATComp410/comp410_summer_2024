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
11-detect-ip_address
                         anonymize_text('My NRP is Unknown', ['NRP']))

    def test_ip_address(self):
        """"Test to make sure a IP Adress is recognized"""
        #positive test case
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
        #negative test case
        test_ipv4= '12345'
        test_string = 'My IPv4 Address is: ' + test_ipv4
        expected_result = 'My IPv4 Address is: 12345'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                            actual_result)
        #Positive test case-Class A
        test_classa= '10.5.6.7'
        test_string = 'My IP class A Address is: ' + test_classa
        expected_result = 'My IP class A Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                            actual_result)
         #Positive test case-Class B
        test_classb= '123.45.67.89'
        test_string = 'My IP class A Address is: ' + test_classb
        expected_result = 'My IP class A Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                            actual_result)
#Positive test case-Class C
        test_classc= '192.168.1.100'
        test_string = 'My IP class C Address is: ' + test_classc
        expected_result = 'My IP class C Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                            actual_result)
        #Positive test case-Class D
        test_classd= '224.0.0.1'
        test_string = 'My IP class D Address is: ' + test_classd
        expected_result = 'My IP class D Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                            actual_result)
         #Positive test case-Class E
        test_classe= '250.1.3.4'
        test_string = 'My IP class E Address is: ' + test_classe
        expected_result = 'My IP class E Address is: <IP_ADDRESS>'
        actual_result = anonymize_text(test_string, ['IP_ADDRESS'])
        self.assertEqual(expected_result,
                         actual_result)
        
        
        

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
