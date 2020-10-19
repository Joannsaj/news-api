import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('source','author','title','description','url','urlToImage','publishedAt','content')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))