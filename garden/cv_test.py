from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from forms import *


# Use unit test class to test my CV page
class cvTest(unittest.TestCase):

    # Control the web driver using Chrome
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(5)

    # Testing Process
    def test_function(self):
        self.browser.get('http://127.0.0.1:8000/cv/edit?type')

        # TODO: implement following test tasks

        ###### PART 1: STATIC SECTION
        # 1, Test if the web title is correct
        self.assertEqual('Talented GEEK\'s CV Editer', self.browser.title)

        # 2, Test if sub-titles are correct
        self.assertEqual('SKILLS',
                         self.browser.find_element_by_id('skillTitle').text)
        self.assertEqual('PROJECT EXPERIENCE',
                         self.browser.find_element_by_id('projectTitle').text)
        self.assertEqual('EDUCATION EXPERIENCE',
                         self.browser.find_element_by_id('eduTitle').text)
        self.assertEqual('INTERESTS',
                         self.browser.find_element_by_id('interestTitle').text)

        # 3, Test if summary part is correctly displayed
        self.assertEqual('ZHOUHAN ZHANG',
                         self.browser.find_element_by_id('name').text)

        summary = self.browser.find_element_by_id('summaryField')
        sumContent = self.browser.find_elements_by_tag_name('li')
        self.assertEqual(
            'Computer Science BSc. Major with British 1st (predicted) Degree',
            sumContent[0].text)
        self.assertEqual('Ability to Speak Chinese and English',
                         sumContent[1].text)
        self.assertEqual(
            'Skilled Programming Ability and Talented Business Taste',
            sumContent[2].text)
        self.assertEqual(
            'Full of Ardor in the Field of Internet and Artificial Intelligence',
            sumContent[3].text)

        # 4, Test if skill part is correctly displayed
        self.assertEqual("Software Prototype Drawing",
                         self.browser.find_element_by_id('titleA').text)
        self.assertEqual(
            "high",
            self.browser.find_element_by_class_name('degreeA').text)
        self.assertEqual("UML Diagram Drawing",
                         self.browser.find_element_by_id('titleB').text)
        self.assertEqual(
            "medium",
            self.browser.find_element_by_class_name('degreeB').text)
        self.assertEqual("Market Demands Analysis",
                         self.browser.find_element_by_id('titleC').text)
        self.assertEqual(
            "medium",
            self.browser.find_element_by_class_name('degreeC').text)
        self.assertEqual("Data Analysis",
                         self.browser.find_element_by_id('titleD').text)
        self.assertEqual(
            "medium",
            self.browser.find_element_by_class_name('degreeD').text)
        self.assertEqual("web Development",
                         self.browser.find_element_by_id('titleE').text)
        self.assertEqual(
            "low",
            self.browser.find_element_by_class_name('degreeE').text)
        self.assertEqual("Agile Project Management",
                         self.browser.find_element_by_id('titleF').text)
        self.assertEqual(
            "low",
            self.browser.find_element_by_class_name('degreeF').text)

        ###### PART 2: DYNAMIC SECTION
        # 1, Test if single project block is correctly displayed (pick the 1st to test)
        self.assertEqual(
            "2020 (Mach)",
            self.browser.find_element_by_class_name('proTime').text)
        self.assertEqual(
            "Mathematical Contest in Modeling (MCM Competition)",
            self.browser.find_element_by_class_name('proTitle').text)
        self.assertEqual(
            "Build a mathematical model after Analyzing more than 30,000 pieces of Amazon Customer Review Data to predict one particular good's sale volume",
            self.browser.find_element_by_class_name('proDesp').text)
        self.assertEqual(
            "· Data Cleaning",
            self.browser.find_element_by_class_name('proRol1').text)
        self.assertEqual(
            "· Data Visualization",
            self.browser.find_element_by_class_name('proRol2').text)

        # 2, Test if single education block is correctly displayed (pick the 1st to test)
        self.assertEqual(
            "2019.09   to   Present:",
            self.browser.find_element_by_class_name('eduTime').text)
        self.assertEqual(
            "University of Birmingham, UK",
            self.browser.find_element_by_class_name('eduUni').text)
        self.assertEqual(
            "BSc. Computer Science",
            self.browser.find_element_by_class_name('eduMajor').text)
        self.assertEqual(
            "1st degree (predict)",
            self.browser.find_element_by_class_name('eduPerform').text)
        self.assertEqual(
            "Mathematical Modelling and Decision Making, System Programming in C/C++, Neural Computation, Computer Vision and Imaging, Machine Learning and Intelligent Data Analysis",
            self.browser.find_element_by_class_name('eduModule').text)

        # 3, Test if single interest block is correctly displayed (pick the 1st to test)
        self.assertEqual(
            "Travel and Photographing",
            self.browser.find_element_by_class_name('intTitle').text)
        self.assertEqual(
            "--- I love having trips to a new place. I have been to Russia, Serbia and Norway so far. Meanwhile, I take a series of beautiful photos in these place, which contains my many important memories.",
            self.browser.find_element_by_class_name('intDesp').text)

        # 4, Test if addProject feature works
        ## jump to the new add page after clicking "add" buttom, same in 5,6
        self.browser.find_element_by_class_name('proAdd').click()
        self.assertEqual("http://127.0.0.1:8000/cv/edit/project",
                         self.browser.current_url)
        ## test if the form works
        form_data = {
            'time': 'testTime',
            'title': 'testTitle',
            'description': 'testDescription',
            'role1': 'testRole1',
            'role2': 'testRole1'
        }
        #form = addProject(data=form_data)
        #self.assertTrue(form.is_valid)
        ## jump back to CV Editor page and continue
        self.browser.get('http://127.0.0.1:8000/cv/edit?type')

        # 5, Test if addEducation feature works
        self.browser.find_element_by_class_name('eduAdd').click()
        self.assertEqual("http://127.0.0.1:8000/cv/edit/education",
                         self.browser.current_url)
        ## test if the form works
        form_data = {
            'start': 'testStart',
            'end': 'testEnd',
            'uni': 'testUni',
            'major': 'testMajor',
            'perform': 'testPerform',
            'module': 'testModule'
        }
        #form = addEducation(data=form_data)
        #self.assertTrue(form.is_valid)
        self.browser.get('http://127.0.0.1:8000/cv/edit?type')

        # 6, Test if addInterest feature works
        self.browser.find_element_by_class_name('intAdd').click()
        self.assertEqual("http://127.0.0.1:8000/cv/edit/interest",
                         self.browser.current_url)
        ## test if the form works
        form_data = {'title': 'testTitle', 'description': 'testDescription'}
        #form = addInterest(data=form_data)
        #self.assertTrue(form.is_valid)
        self.browser.get('http://127.0.0.1:8000/cv/edit?type')


if __name__ == '__main__':
    unittest.main(warnings='ignore')