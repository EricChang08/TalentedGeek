from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


# Use unit test class to test my CV page
class cvTest(unittest.TestCase):
    # Control the web driver using Chrome
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(5)

    # Testing Process
    def test_function(self):
        self.browser.get('http://127.0.0.1:8000/cv/edit')

        # TODO: implement following test tasks

        ###### PART 1: STATIC SECTION
        # 1, Test if the web title is correct

        # 2, Test if sub-titles are correct

        # 3, Test if summary part is correctly displayed

        # 4, Test if skill part is correctly displayed

        ###### PART 2: DYNAMIC SECTION
        # 1, Test if login feature works

        # 2, Test if addProject feature works

        # 3, Test if addEducation feature works

        # 4, Test if addInterest feature works

        # 5, Test if deleteProject feature works

        # 6, Test if deleteEducation feature works

        # 7, Test if deleteInterest feature works


if __name__ == '__main__':
    unittest.main(warnings='ignore')