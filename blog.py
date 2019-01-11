import uuid
import datetime
from models.post import Post
from database import Database


class Blog(object):
    # creates author, title description and id
    def __init__(self,author, title,description, id= None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = input("Enter post title: ") #creates the title for a new post taking user input
        content = input("Enter post content: ") # Takes user input for content
        date = input("Enter post date, or leave blank for today(in format DDMMYYYY): ") #Asks user for post date
        if date == "":
            date = datetime.datetime.utcnow() #uses current date if user did not enter date
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y") #converts string to a datetime object
        #creates a post object by using the information from the user
        post = Post(blog_id = self.id,
                    title = title,
                    content = content,
                    author = self.author,
                    date = date)
        #save the post to mongodb database
        post.save_to_mongo()

    def get_posts(self):
        #method to retreive posts based on the id
            return Post.from_blog(self.id)

    def save_to_mongo(self):
        #method used to save a post to the database
            Database.insert(collection = 'blogs',
                            data = self.json())

    def json(self):
        #json file that stores the author, title, description, and id
            return{
                'author': self.author,
                'title':self.title,
                'description': self.description,
                'id':self.id

            }
    @classmethod
    def from_mongo(cls ,id):
        #method used to find the post by using the id
            blog_data = Database.find_one(collection = 'blogs',
                                          query = {'id': id})
            return cls(author = blog_data['author'],
                        title = blog_data['title'],
                        description = blog_data['description'],
                        id = blog_data['id'])

