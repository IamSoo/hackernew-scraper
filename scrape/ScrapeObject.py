
class Scrape:
    def __init__(self):
        pass

    def __init__(self,title,uri,author,points,comments,rank):
        self.title = title
        self.uri = uri
        self.author = author
        self.points = points
        self.comments = comments
        self.rank = rank

    def encode_user(self,o):
        if isinstance(o, Scrape):
            return {"title": o.title, "uri": o.uri, "author": o.author, "points": o.points, "comments": o.comments,
                         "rank": int(o.rank)}
        else:
            raise TypeError("Object of type ScraperObject is not serializable")
