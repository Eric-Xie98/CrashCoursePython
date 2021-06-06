## We just learned how to write test cases for functions, now we'll learn how to write them for 
## classes. Similar to before, we'll implement the unittest.TestCase class' assert methods
## to ensure no errors or exceptions are raised:

# These are some of the 6 most commonly used ones:

# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIn(item, list)
# assertNotIn(item, list)

# Testing a class is similar to testing a function, let's use an anonymous survey class as an example:

class AnonymousSurvey():
    """Collects anonymous answers to a survey question"""

    def __init__(self, question):
        """Store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def showQuestion(self):
        """Display the survey question."""
        print(self.question)

    def storeResponses(self, response):
        """Store the response into the responses list"""
        self.responses.append(response)
    
    def showResults(self):
        """Prints out the responses in the list"""
        print("Survey results: ")
        for response in self.responses:
            print('-' + response)

# To show that this class works, let's write a program for it:

if __name__ == '__main__':                      ## This code stops the SurveyTesting.py import from running the code below, and only the functions 

    myQuestion = "What's your favorite food?"
    foodSurvey = AnonymousSurvey(myQuestion)

    foodSurvey.showQuestion()
    print("Type in 'quit' at any time to exit the program.")
    while True:
        
        response = input("Type in answer here: ")
        if response == 'quit':
            break
        foodSurvey.storeResponses(response)

    print("Thank you for participating in the survey!")
    foodSurvey.showResults()

# Now that this class works, let's say that we wanted to implement more features that could 
# potentially cause the AnonymousSurvey class to break. We ensure that single responses will
# not break by writing test cases.

# As mentioned in SurveyTesting.py, we'll use the setup() method of unittest to make tests more efficient:

## Rather than repeatedly create an AnonymousSurvey object and question, we can use a setup() function to create
# them once at the beginning and use them for testing for the rest of the program.

## Exercises

class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def giveRaise(self, amount = 5000):
        self.salary += amount
        return self.salary

if __name__ == '__main__':
    employee = Employee('eric', 'xie', 300000)
    print("Before: " + str(employee.salary))
    print("After: " + str(employee.giveRaise()))

    print()

    print(employee.giveRaise(25000))
