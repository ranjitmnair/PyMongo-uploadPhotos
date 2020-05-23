from flask import *
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost:27017/Users"
mongo=PyMongo(app)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/create" enctype="multipart/form-data">
        <input type ="file" name="post">
        <input type="submit">
        </form>
    '''

@app.route('/create',methods=['POST'])
def create():
    if 'post' in request.files:
        post=request.files['post']
        mongo.save_file(post.filename,post)
        mongo.db.users.insert({'postid':post.filename})

    return 'Uploaded'

@app.route('/post/<name>')
def file(name):
    return mongo.send_file(name)