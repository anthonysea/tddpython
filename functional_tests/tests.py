from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    # setUp method is run before each test
    def setUp(self):
        self.browser = webdriver.Firefox("C:/Users/Anthony/Documents/coding/python_projects/tddpython")

    # tearDown method is run after each test
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        

    # Any method whose name starts with test is a test method, and will be run by the test runner
    def test_can_start_a_list_for_one_user(self):
        # Users goes to check out to-do list homepage
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # There is still a text box inviting the user to add another item. She
        # enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on the user's list
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # The page has generated a unique URL for the user 
        self.fail("Finish the test!")

        # User visits that URL, and the to-do list is still there

        # User leaves the page

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # User starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # User notices that her list has a unique URL
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, "/lists/.+")

        # New user 2 comes to the site

        ## We use a new browser session to make sure that no infromation
        ## of user 1's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox("C:/Users/Anthony/Documents/coding/python_projects/tddpython")

        # User 2 visits the home page. There is no sign of user 1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("User peacock feathers to make a fly", page_text)

        # User 2 starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # User 2 gets his own unique URL
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, "/lists/.+")
        self.assertNotEqual(user2_list_url, user1_list_url)

        # Again, there is no trace of user 1's list
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)