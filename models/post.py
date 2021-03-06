from datbase import Database
import uuid
import datetime
class Post(object):
    def __init__(self, blog_id, title, content, author, id, date=datetime.datetime.utcnow()):
        """

        :rtype: object
        """
        self.title=title
        self.content=content
        self.author=author
        self.blog_id=blog_id
        self.created_date=date
        self.id=uuid.uuid4().hex if id is None else id
    def save_to_mongo(self):
        Database.insert(collection="posts",data=self.json())
    def json(self):
        return{
            "id":self.id,
            "blog_id":self.blog_id,
            "title":self.title,
            "author":self.author,
            "created_date":self.created_date,
            "content":self.content
        }
    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection="posts",query={"id":id})
    @staticmethod
    def from_blog(id):
        return [Post for post in Database.find(collectio="posts",query={"blog_id":id})]
