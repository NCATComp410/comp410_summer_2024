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
        
    def test_au_medicare(self):
        """Test to make sure an AU_MEDICARE is recognized"""
        # negative test case 
        test_medicare = '3888 87568 0'
        test_string = 'My medicare number is ' + test_medicare
        expected_result = 'My medicare number is 3888 87568 0'
        actual_result = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case "Too short"
        test_medicare = '3888 8768 0'
        test_string = 'My medicare number is ' + test_medicare
        expected_result = 'My medicare number is 3888 8768 0'
        actual_result = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # negative test case "Too short"
        test_medicare = '38884 87868 0'
        test_string = 'My medicare number is ' + test_medicare
        expected_result = 'My medicare number is 38884 87868 0'
        actual_result = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        #positive test case "medium"
        start = '3111 '
        middle = '32311 '
        end = '1'
        test_medicare = start + middle + end
        test_string = 'My medicare number is ' + test_medicare
        expected_result = 'My medicare number is <AU_MEDICARE>'
        actual_result = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected_result,
                         actual_result)
        
        #positive test case "low"
        first = '21113'
        last = '22311'
        test_medicare = first + last
        test_string = 'My medicare number is ' + test_medicare
        expected_result = 'My medicare number is <AU_MEDICARE>'
        actual_result = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected_result,
                         actual_result)
