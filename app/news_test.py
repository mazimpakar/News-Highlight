import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('The Hindu','Nikhil Varma and Divya Kala Bhavani',"So, let’s talk tech de-addiction centres","https://www.thehindu.com/sci-tech/technology/dx56fs/article26303250.ece/ALTERNATES/LANDSCAPE_615/19bgm-video-controller-3366571920","Tech de-addiction centres around the world are giving a whole new meaning to the phrase ‘modern-day epidemics’ — and no, we aren’t talking about a regular old digital detox","2019-02-18T10:54:34Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()