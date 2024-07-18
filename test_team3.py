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
       
    def test_credit_card(self):
        """Test to make sure CREDIT_CARD is recognized"""
        test_cc = '4012 9450 3454 5464'
        test_string = 'My credit card number is ' + test_cc
        expected_result = 'My credit card number is <CREDIT_CARD>'
        actual_result = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected_result,
                         actual_result) 
