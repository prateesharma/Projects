
import uuid
from database import Database
import datetime

class Post(object):

    def __init__(self,blog_id, title, content, author,date = datetime.datetime.utcnow(),id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id  #uuid4 is random uuid

        #post = Post(blog_id = "123", title = "a title", content = "some content", author = "jose")
        #The date would be todays date and id would be none
    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())
        pass

    def json(self):
        return{
            'id':self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date':self.created_date

        }

    @classmethod
    def from_mongo(cls,id):
        #Post.from_mongo('123') <-- would give us post from dattabase with id 123
        postdata = Database.find_one(collection = 'posts', query={'id': id})  #finds one post that has the id
        return cls(blog_id = post_data['blog_id'],
                   title = post_data['title'],
                   content = post_data['content'],
                   author = post_data['author'],
                   date = post_data['created_data'],
                   id = post_data['id'])

    @staticmethod
    def from_blog(id):
        return Database.find(collection='posts', query = {'blog_id': id})



