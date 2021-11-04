class NewsSource:
    """
    Movie class to define news object
    """

    def __init__(self,name,category,url,id):
        self.name = name
        self.id = id
        self.url = url
        self.category = category
       
        


class Articles:
    """
    article class to define article object
    """

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = urlToImage
        self.publishedAt = publishedAt
        self.content = content
      
