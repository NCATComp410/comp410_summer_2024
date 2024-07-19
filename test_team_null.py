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
        
    def test_us_driver_license(self):
        """Test to make sure a US_DRIVER_LICENSE is recognized"""
        # positive test case
        prefix = '123'
        mid = '456'
        ending = '123456'
        test_dl = prefix + mid + ending
        test_string = 'My driver license is ' + test_dl
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - US_DRIVER_LICENSE is not replaced
        test_dl = '123456789011'
        test_string = 'My Driver License ' + test_dl
        expected_result = 'My driver license is 123456789011'
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case - too short
        test_dl = '12345678'
        test_string = 'My driver license is ' + test_dl
        expected_result = 'My driver license is 12345678'
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        
        