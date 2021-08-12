from flask.helpers import make_response
from api import app
from flask import request,jsonify
import jwt
import datetime
from functools import wraps
from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')
SECRET_KEY=config['DEFAULT']['SECRET_KEY']


app.config['SECRET KEY'] = SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message':'Token is missing'}),403
        try :
            data = jwt.decode(token,app.config['SECRET KEY'],algorithms=["HS256"]) 
            print('2nd : ',data)  
        except Exception as e:
            print(e)
            return jsonify({'message':'Token is Invalid'}),403  
        return f(*args,**kwargs)

    return decorator


@app.route('/authenticate')
def authentication():
    auth = request.authorization

    if auth and auth.password == 'password' and auth.username == 'username':
        token = jwt.encode({'user':auth.username,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET KEY'])
        return jsonify({'token' : token})
        #return jsonify({'token' : token.decode('UTF-8')})
    return make_response('could not verify !', 401, {'www-authenticate': 'Basic realm = "login required"'})    




