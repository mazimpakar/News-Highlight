import unittest
from models import article
Article= article.Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_article = Article(12345,'article for news',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'This movie is the best thing since sliced bread')


    def tearDown(self):
        Article.clear_article()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.news_id,12345)
        self.assertEquals(self.new_article.title,'Article for news')
        self.assertEquals(self.new_article.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_article.article,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_article.description,'Description for news')
        self.assertEquals(self.new_article.publishedAt,'publishedAt')





    def test_save_article(self):
        self.new_article.save_article()
        self.assertTrue(len(Article.all_article)>0)

if __name__ == '__main__':
    unittest.main()


