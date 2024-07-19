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
        
    def test_us_itin(self):
        """Test to make sure a US_SSN is recognized"""
        # positive test case
        prefix = '123'
        mid = '-12-'
        ending = '1234'
        test_itin = prefix + mid + ending
        test_string = 'My ITIN is ' + test_itin
        expected_result = 'My ITIN is <US_ITIN>'
        actual_result = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - US_ITIN is not replaced
        test_itin = '123456789'
        test_string = 'My ITIN is ' + test_itin
        expected_result = 'My ITIN is 123456789'
        actual_result = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - too short
        test_itin = '12345678'
        test_string = 'My ITIN is ' + test_itin
        expected_result = 'My ITIN is 12345678'
        actual_result = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - too long
        test_itin = '1234567890'
        test_string = 'My ITIN is ' + test_itin
        expected_result = 'My ITIN is 1234567890'
        actual_result = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected_result,
                         actual_result)