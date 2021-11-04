class NewsSource:
    """
    Movie class to define news object
    """

    def __init__(self, id, name, url, category):
        self.name = name
        self.id = id
        self.url = url
        self.category = category


class Articles:
    """
    article class to define article object
    """

    def __init__(self, author,title, description, url, urlToImage, publishedAt, content,id):
        self.author=author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.id=id
