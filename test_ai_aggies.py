"""Tests for Team AI Aggies"""
import unittest
from pii_scan import show_aggie_pride, anonymize_text

class TestTeamAIAggies(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_nrp(self):
        """Test to make sure NRP is anonymized"""
        self.assertEqual('My political affiliation is <NRP>',
                         anonymize_text('My political affiliation is Democrat', ['NRP']))

        self.assertEqual('My NRP is Unknown',
                         anonymize_text('My NRP is Unknown', ['NRP']))

    def test_person(self):
        """Test to ensure a Person is recognized and anonymized correctly"""
        # Positive test case - Person should be anonymized
        test_person = 'Nicholas Dewitt'
        test_string = 'My name is ' + test_person
        expected_result = 'My name is <PERSON>'
        actual_result = anonymize_text(test_string, ['PERSON'])
        self.assertEqual(expected_result,
                        actual_result)

        # Positive test case - Person should be anonymized
        test_person = 'Mansa Musa'
        test_string = 'My name is ' + test_person
        expected_result = 'My name is <PERSON>'
        actual_result = anonymize_text(test_string, ['PERSON'])
        self.assertEqual(expected_result,
                         actual_result)

        # Negative test case - number/name not anonymized
        test_person = '12345'
        test_string = 'My name is ' + test_person
        expected_result = 'My name is 12345'
        actual_result = anonymize_text(test_string, ['PERSON'])
        self.assertEqual(expected_result,
                         actual_result)
        
        # Positive test case - Account length is greater than 8 and less than 17
    def test_US_BANK_NUMBER(self):
        """test to make sure bank account is required"""
        test_account = "123456789"
        test_string = "My account number is " + test_account
        expected_result = "My account number is <US_BANK_NUMBER>"
        actual_result = anonymize_text(test_string, ["US_BANK_NUMBER"])
        self.assertEqual(expected_result,
                        actual_result)
         
        # Negative test case - Account length is less than 8
        test_account = "1234567"
        test_string = "My account number is " + test_account
        expected_result = "My account number is 1234567"
        actual_result = anonymize_text(test_string, ["US_BANK_NUMBER"])
        self.assertEqual(expected_result,
                         actual_result)

   
         
         
        