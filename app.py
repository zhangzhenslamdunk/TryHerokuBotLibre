#!/usr/bin/env python
# for bot libre
import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS

# Flask app should start in global layout
app = Flask(__name__)


def options (self):
    return {'Allow' : 'PUT' }, 200, \
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods' : 'PUT,GET' }



@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

#    print("Request:")
#    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):

    speech = 'this is the first message sent from Heroku for Bot Libre.'
    
#    # read from web data
#    url = urllib.request.urlopen("http://zhangzhenslamdunk.github.io/sentence.txt") 
#    s = url.read()
#    s = s.decode('utf-8')
#    
#    # read text file from local folder
#    infile = open('sentence.txt')
#    s = infile.read()
    
#    speech = s
    
    
    print("Response:")
    print(speech)
    return {
        "fulfillmentText": speech,
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
