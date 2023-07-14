from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def format_timestamp(self, timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                # Note: use find_elements(...) to return an list of items
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, NoSuchElementException) as wait_exception:
                if time.time() - start_time > MAX_WAIT:
                    print("Test start time:", self.format_timestamp(start_time))
                    print("Current exception time:", self.format_timestamp(time.time()))
                    print(f"Waited for {MAX_WAIT} seconds")
                    raise wait_exception
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A user check a new to-do list site webpage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn("To-Do", header_text.text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"), "Enter a to-do item"
        )

        # He types "Buy latte coffee" into a text box
        inputbox.send_keys("Buy latte coffee")

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy latte coffee" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table("1: Buy latte coffee")

        # There is still a text box inviting her to add another item. he
        # enters "Drink latte coffee to energize my morning".
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Drink latte coffee to energize my morning")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table("1: Buy latte coffee")
        self.wait_for_row_in_list_table(
            "2: Drink latte coffee to energize my morning"
        )

        # The user wonders whether the site will remember her list. Then he sees
        # that the site has generated a unique URL -- there is some
        # explanatory text to that effect.
        self.fail("Finish the test!")

        # He visits that URL - her to-do list is still there.

        # Satisfied, he goes back to sleep

