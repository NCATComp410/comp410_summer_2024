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
    def test_us_itin(self):
        """Test to make sure a US_ITIN is recognized"""
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
        
        # negative test case - US_SSN is not replaced
        test_itin = '123456789'
        test_string = 'My ITIN is ' + test_itin
        expected_result = 'My SSN is 123456789'
        actual_result = anonymize_text(test_string, ['US_SSN'])
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
=======
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
        test_dls = '1253445'
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'  # Expect anonymized value
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)
        
        # negative test case - too long
        test_dls = '1253463511123'
        test_string = 'My driver license is ' + test_dls
        expected_result = 'My driver license is <US_DRIVER_LICENSE>'  # Expect anonymized value
        actual_result = anonymize_text(test_string, ['US_DRIVER_LICENSE'])
        self.assertEqual(expected_result, actual_result)

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