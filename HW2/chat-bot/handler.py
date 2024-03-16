import json
import os
import re
from time import gmtime, strftime
import subprocess
import requests


def handle(req):
    print(req)
    #Get the data from user side
    data  = json.loads(req)

    #Build the result for the query from a user
    result = {}
    if 'question' in data:
        query = data['question']
        if re.search(r'name', query):
            result = "chatbot"
        elif re.search(r'time', query):
            result = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        else:
            result = {"error": "Invalid request payload"}

    elif 'figlet' in data:
        query = data['figlet']
        url = f'http://45.79.114.201:8080/function/figlet'
        response = requests.post(url, data=query)
        result = reponse.text
        print(response.text)
    
    else:
        print("$")
        result = {"error": "Invalid request payload"}

    #Return
    return json.dumps(result)



if __name__ == "__main__":
    
    req = '{"question": "name"}'
    result = handle(req)
    print(json.loads(result), "\n")

    req = '{"question": "time"}'
    result = handle(req)
    print(json.loads(result), "\n")

    req = '{"figlet": "Great!"}'
    result = handle(req)
    print(json.loads(result))
    
    
    
    
