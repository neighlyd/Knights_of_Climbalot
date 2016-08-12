from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):

    # Testbot Prime opens up a Chrome page and waits for it to load.
    def setUp(self):
        Chrome = webdriver.Chrome('/Users/callius/sites/testing_drivers/chromedriver')
        self.browser = Chrome
        self.browser.implicitly_wait(3)

    # Testbot Prime closes the Chrome page that it had opened.
    def tearDown(self):
        self.browser.quit()

    # Testbot Prime looks to see what the full URL is for where it has landed.
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    # Testbot Prime checks to see if Django is giving it the index.html page if it goes to the url that Django refers to as 'index'
    def test_use_main_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index/index.html')

    # Testbot Prime checks to see if Django is giving it the base.html page if it goes to the url that Django refers to as 'index'
    def test_use_base_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'base.html')

    # Testbot Prime goes to the url that Django calls 'index' and checks to see if the phrase "Knights of Climbalot" is in that page's title.
    def test_home_title(self):
        self.browser.get(self.get_full_url("index"))
        self.assertIn("Knights of Climbalot", self.browser.title)

    # Testbot Prime goes to the base url of the site and then checks to see if there are Robots and Humans text files there.
    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)
