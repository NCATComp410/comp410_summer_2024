"""Tests for Team Traveling Salesmen"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestTeamTravelingSalesmen(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_nrp(self):
        """Test to make sure NRP is anonymized"""
        self.assertEqual('My religion is <NRP>',
                         anonymize_text('My religion is Christian', ['NRP']))

        self.assertEqual('My NRP is Unknown',
                         anonymize_text('My NRP is Unknown', ['NRP']))
        
    def test_uk_nhs (self):

        """Test to make sure NHS is recognized"""

        # negative test case - too short
        test_nhs = '123 456 789'
        test_string = 'My nhs is ' + test_nhs
        expected_result = 'My nhs is 123 456 789'
        actual_result = anonymize_text(test_string, ['UK_NHS'])
        self.assertEqual(expected_result,
                          actual_result)

        # negative test case - too long
        test_nhs = '123 456 789123'
        test_string = 'My nhs is ' + test_nhs
        expected_result = 'My nhs is 123 456 789123'
        actual_result = anonymize_text(test_string, ['UK_NHS'])
        self.assertEqual(expected_result,
                         actual_result)
        # positive test case
        prefix = '123 '
        mid= '456 '
        ending = '7829'
        test_nhs = prefix + mid + ending
        test_string = 'My nhs is ' + test_nhs
        expected_result = 'My nhs is 123 456 7829'
        actual_result = anonymize_text(test_string, ['UK_NHS'])
        self.assertEqual(expected_result,
                         actual_result)      