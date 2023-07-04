from selenium import webdriver
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
        self.assertIn("To-Do",self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away
        # He types "Buy latte coffee" into a text box

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy latte coffee" as an item in a to-do list

        # There is still a text box inviting her to add another item. he
        # enters "Drink latte coffee to energize my morning".

        # The page updates again, and now shows both items on her list

        # The user wonders whether the site will remember her list. Then he sees
        # that the site has generated a unique URL -- there is some
        # explanatory text to that effect.

        # He visits that URL - her to-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings='ignore')
