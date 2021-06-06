## Testing module for the AnonymousSurvey class 

import unittest
from TestingClass import AnonymousSurvey

class TestAnonSurvey(unittest.TestCase):

    """Tests for the AnonymousSurvey class"""

    def setUp(self):

        """ Sets up repetitive objects/variables for testing"""

        question = "What language are you fluent in?"
        self.languageSurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Spanish']          ## These responses are separate from the survey's responses

    def test_single_response(self):
        
        """Test that a single response is stored correctly"""

        self.languageSurvey.storeResponses(self.responses[0])

        self.assertIn(self.responses[0], self.languageSurvey.responses)

    def test_three_responses(self):

        """Test that 3 responses are stored correctly"""

        for response in self.responses:
            self.languageSurvey.storeResponses(response)

        for response in self.responses:
            self.assertIn(response, self.languageSurvey.responses)


# We can see that the first test for single responses work, so let's implement multiple response tests now.

# Now that we've implemented a test that ensures multiple responses are stored correctly, we can see that
# these tests are a bit repetitive, so we'll use another feature of unittest to make this more efficient.

## Rather than repeatedly create an AnonymousSurvey object and question, we can use a setup() function to create
# them once at the beginning and use them for testing for the rest of the program.

# when we include setUp() in our class, Python runs it first before any tests.

# When we use the setUp() method, it can make test cases easier to write as they're less cluttered
# and is much more easier thann making a set of attributes/objects in each test

## Exercises

from TestingClass import Employee

class EmployeeTesting(unittest.TestCase):

    def setUp(self):

        self.employee = Employee('eric', 'xie', 300000)


    def test_default_giveRaise(self):

        self.assertEqual(self.employee.giveRaise(), 300000 + 5000)

    
    def test_custom_giveRaise(self):

        amount = 25432
        self.assertEqual(self.employee.giveRaise(amount), 300000 + amount)


unittest.main()