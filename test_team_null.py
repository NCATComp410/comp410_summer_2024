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
        prefix = '11'
        mid = '1234567'
        ending = '1'
        test_dls = prefix + mid + ending
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)

        # negative test case - US_DRIVER_LICENSE not matching pattern
        test_dls = '1253463511'
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'  # Expect anonymized value
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)
        # negative test case - too short
        test_dls = '12534635'
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'  # Expect anonymized value
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)
        # negative test case - too long
        test_dls = '125346351112'
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'  # Expect anonymized value
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)
        