"""Tests for Team AI Aggies"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestTeamAIAggies(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_nrp(self):
        """Test to make sure NRP is anonymized"""
        self.assertEqual('My political affiliation is <NRP>',
                         anonymize_text('My political affiliation is Republican', ['NRP']))

        self.assertEqual('My NRP is Unknown',
                         anonymize_text('My NRP is Unknown', ['NRP']))
        
    def test_location(self):
        """Test to make sure that a LOCATION  is recognized"""
        #positive test case
        test_location = 'Greensboro'
        test_string = 'My location is ' + test_location
        expected_result = 'My location is <LOCATION>'
        actual_result = anonymize_text(test_string, ['LOCATION'])
        self.assertEqual(expected_result,
                         actual_result)

        #negative test case - Candy is not a location
        test_location = 'Candy'
        test_string = 'My location is ' + test_location
        expected_result = 'My location is Candy'
        actual_result = anonymize_text(test_string, ['LOCATION'])
        self.assertEqual(expected_result,
                         actual_result)