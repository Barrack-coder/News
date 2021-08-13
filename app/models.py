class news_Source:
    '''
    news_Source class to define news_Source Objects
    '''

    def __init__(self,newsid,name,description,url,language):
        self.newsid = newsid
        self.name = name
        self.description = description
        self.url = url
        self.language = language
       



class news_Article:
    '''
    news_Article class to define news_Article Objects
    
    '''

    def __init__(self,article_author,title,description,articleurl,imageurl):
        self.article_author = article_author
        self.title = title
        self.description = description
        self.articleurl = articleurl
        self.imageurl = imageurl
