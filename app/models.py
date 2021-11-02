class NewsSource:
    """
    Movie class to define news object
    """

    def __init__(self, id, name, url):
        self.name = name
        self.id = id
        self.url = url


class Articles:
    """
    article class to define article object
    """

    def __init__(self, title, description, url, urlToImage, publishedAt, content):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
