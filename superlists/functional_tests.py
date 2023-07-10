from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # A user check a new to-do list site webpage
        self.browser.get("http://localhost:8000/")

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

        table = self.browser.find_element(By.ID, "id_list_table")

        # Note: use find_elements(...) to return an list of items
        rows = table.find_elements(By.TAG_NAME, "tr")

        self.assertIn("1: Buy latte coffee", [row.text for row in rows])

        # There is still a text box inviting her to add another item. he
        # enters "Drink latte coffee to energize my morning".
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Drink latte coffee to energize my morning")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1: Buy latte coffee", [row.text for row in rows])
        self.assertIn(
            "2: Drink latte coffee to energize my morning",
            [row.text for row in rows],
        )

        # The user wonders whether the site will remember her list. Then he sees
        # that the site has generated a unique URL -- there is some
        # explanatory text to that effect.
        self.fail("Finish the test!")

        # He visits that URL - her to-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings="ignore")
