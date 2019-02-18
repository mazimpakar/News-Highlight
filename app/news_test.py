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
        self.new_news = News('Reuters','Lesley Wroughton',"Pompeo meets EU's top diplomat after Pence's Iran accusations - Reuters","https://s2.reutersmedia.net/resources/r/?m=02&d=20190215&t=2&i=1356813496&w=1200&r=LYNXNPEF1E0ID","U.S. Secretary of State Mike Pompeo met with the EU's top diplomat in Brussels on Friday, a day after Vice President Mike Pence accused America's traditional European allies of trying to undermine U.S. sanctions against Iran.""U.S. Secretary of State Mike Pompeo met with the EU's top diplomat in Brussels on Friday, a day after Vice President Mike Pence accused America's traditional European allies of trying to undermine U.S. sanctions against Iran.","2019-02-15T08:15:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()