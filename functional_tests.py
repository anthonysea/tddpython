from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    # setUp method is run before each test
    def setUp(self):
        self.browser = webdriver.Firefox()

    # tearDown method is run after each test
    def tearDown(self):
        self.browser.quit()

    # Any method whose name starts with test is a test method, and will be run by the test runner
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Users goes to check out to-do list homepage
        self.browser.get("http://localhost:8000")

        # User notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test!')

        # User is invite to enter a to-do item straigth away

        # User types "Buy peacock feathers" into a text box

        # User hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting the user to add another item. She
        # enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on the user's list

        # The page has generated a unique URL for the user 

        # User visits that URL, and the to-do list is still there

        # User leaves the page

if __name__ == "__main__":
    unittest.main(warnings="ignore")
