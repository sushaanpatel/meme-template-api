import pymongo
import dotenv
import os

dotenv.load_dotenv()
password = os.environ.get('PASS')

mongo = pymongo.MongoClient(f'mongodb+srv://root:{password}@memes.2xsyj.mongodb.net/memes?retryWrites=true&w=majority')
templates = mongo['memes']['templates']

def get_all():
    out = []
    for i in templates.find():
        out.append({
            'id': i['pri_id'],
            'title': i['title'],
            'image': i['image'],
            'explanation': i['explanation'],
            'origin': i['origin'],
            'popularity': i['popularity'],
            'tags': i['tags'],
            'examples': i['examples']
        })
    return out

def get_one(name):
    out = []
    for i in templates.find():
        if name.lower() in i['title'].lower():
            out.append({
                'status':'200',
                'id': i['pri_id'],
                'title': i['title'],
                'image': i['image'],
                'explanation': i['explanation'],
                'origin': i['origin'],
                'popularity': i['popularity'],
                'tags': i['tags'],
                'examples': i['examples']
            })
    if out == []:
        return {
            'status':'404',
            'error': 'meme template not found'
        }
    return out