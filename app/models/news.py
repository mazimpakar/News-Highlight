class Source:
    '''
    Source class to define Source  Objects
    '''
    def __init__(self,news_id,name,url,description):
        self.news_id = news_id
        self.name = name
        self.url = url
        self.description= description
        # self.language= language
class News:
    '''
    News class to define News  Objects
    '''

    def __init__(self,author,title, image,description,url,publishedAt,content):
        # self.name =name
        self.author =author
        self.title = title
        self.image =image
        self.description =description
        self.url=url
        self.publishedAt=publishedAt
        self.content = content





        