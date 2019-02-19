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

    def __init__(self,author,title, image,description,publishedAt,content):
        # self.name =name
        self.author =author
        self.title = title
        self.urlImage ="https://www.thehindu.com/sci-tech/technology/dx56fs/article26303250.ece/ALTERNATES/LANDSCAPE_615/19bgm-video-controller-3366571920"
        self.description =description
        self.publishedAt=publishedAt
        self.content = content





        