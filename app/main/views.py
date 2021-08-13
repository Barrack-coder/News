
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_source, get_news_sources


#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_news_sources()  
	title = "News Articles"          

	return render_template('index.html',sources = sources)

@main.route('/source/<source>')
def articles(source):
	'''
	view root page function that returns the index the page and its data
	'''
	article = get_news_source(source)  
	title = "News Articles"          

	return render_template('articles.html',articles = articles) 