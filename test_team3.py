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
        
    def test_date_time(self):
            """Test to make sure a DATE_TIME is recognized"""
            # positive test case 
            prefix = '12'
            mid ='-12-'
            ending ='1234'
            test_date_time = prefix + mid + ending
            test_string = 'The date is ' + test_date_time
            expected_result = 'The date is <DATE_TIME>'
            actual_result = anonymize_text(test_string, ['DATE_TIME'])
            self.assertEqual(expected_result,
                                actual_result)
            
             # negative test case - DATE_TIME is not replaced
            test_date_time ='12345678'
            test_string = 'The date is ' + test_date_time
            expected_result = 'The date is 12345678'
            actual_result = anonymize_text(test_string, ['DATE_TIME'])
            self.assertEqual(expected_result,
                                actual_result)
            
            # negative test case - too short
            test_date_time ='1234567'
            test_string = 'The date is ' + test_date_time
            expected_result = 'The date is 1234567'
            actual_result = anonymize_text(test_string, ['DATE_TIME'])
            self.assertEqual(expected_result,
                                actual_result)