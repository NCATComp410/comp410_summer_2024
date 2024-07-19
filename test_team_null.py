"""Tests for Team NULL"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestTeamNull(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_nrp(self):
        """Test to make sure NRP is anonymized"""
        self.assertEqual('My NRP is <NRP>',
                         anonymize_text('My NRP is Democrat', ['NRP']))
        
    def test_us_ssn(self):
        """Test to make sure a US_SSN is recognized"""
        # positive test case
        prefix = '123'
        mid = '-12-'
        ending = '1234'
        test_ssn = prefix + mid + ending
        test_string = 'My ssn is ' + test_ssn
        expected_result = 'My ssn is <US_SSN>'
        actual_result = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - US_SSN is not replaced
        test_ssn = '123456789'
        test_string = 'My ssn is ' + test_ssn
        expected_result = 'My ssn is 123456789'
        actual_result = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - too short
        test_ssn = '12345678'
        test_string = 'My ssn is ' + test_ssn
        expected_result = 'My ssn is 12345678'
        actual_result = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - too long
        test_ssn = '1234567890'
        test_string = 'My ssn is ' + test_ssn
        expected_result = 'My ssn is 1234567890'
        actual_result = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected_result,
                         actual_result)
    
    def test_au_abn(self):
        """Test to make sure an AU_ABN is recognized and anonymized"""
       
        # Negative test case - incorrect format (too short)
        test_abn = '12 345 678 90'
        test_string = 'My ABN is: ' + test_abn
        expected_result = 'My ABN is: 12 345 678 90'
        actual_result = anonymize_text(test_string, ['AU_ABN'])
        self.assertEqual(expected_result, actual_result)

        # Negative test case - incorrect format (contains letters)
        test_abn = '12 345 ABC DE1'
        test_string = 'My ABN is: ' + test_abn
        expected_result = 'My ABN is: 12 345 ABC DE1'
        actual_result = anonymize_text(test_string, ['AU_ABN'])
        self.assertEqual(expected_result, actual_result)

        # Negative test case - to long
        test_abn = '142 345 681 004'
        test_string = 'My ABN is: ' + test_abn
        expected_result = 'My ABN is: 142 345 681 004'
        actual_result = anonymize_text(test_string, ['AU_ABN'])
        self.assertEqual(expected_result, actual_result)
        
        # Positive test case - valid ABN
        prefix = '51 '
        first_mid = '824 '
        sec_mid = '753 '
        end = '556'
        test_abn = prefix + first_mid + sec_mid + end
        test_string = 'My ABN is: ' + test_abn
        expected_result = 'My ABN is: <AU_ABN>'
        actual_result = anonymize_text(test_string, ['AU_ABN'])
        self.assertEqual(expected_result, actual_result)
