from flask import render_template
from app import app
from .requests import get_news,get_news
# @app.route('/news/<int:news_id>')
# def news(news_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     return render_template('news.html',id = news_id)
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     title = 'Home - Welcome to The News Review Website Online'
#     return render_template('index.html', title = title)

from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    mass_media_news = get_news('mass media')
    newspapers_news = get_news('newspapers')
    print(popular_news,mass_media_news,newspapers_news)
    title = 'Home - Welcome to The News Review Online'
    return render_template('index.html', title = title,popular = popular_news,mass_media = mass_media_news,newspapers = newspapers_news)




@app.route('/news/<news_name>')
def news(news_name):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(name)
    title = f'{news.title}'
    return render_template('index.html', name = name, author = author,title = title,description = description, full_article = full_article,publishedAt = publishedAt ) 
    

    
    


