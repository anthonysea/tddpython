from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    # setUp method is run before each test
    def setUp(self):
        self.browser = webdriver.Firefox("C:/Users/Anthony/Documents/coding/python_projects/tddpython")

    # tearDown method is run after each test
    def tearDown(self):
        self.browser.quit()

    # Any method whose name starts with test is a test method, and will be run by the test runner
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Users goes to check out to-do list homepage
        self.browser.get("http://localhost:8000")

        # User notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # User is invite to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # User types "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")


        # User hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for rows in rows)
        )

        # There is still a text box inviting the user to add another item. She
        # enters "Use peacock feathers to make a fly"
        self.fail("Finish the test!")

        # The page updates again, and now shows both items on the user's list

        # The page has generated a unique URL for the user 

        # User visits that URL, and the to-do list is still there

        # User leaves the page

if __name__ == "__main__":
    unittest.main(warnings="ignore")
