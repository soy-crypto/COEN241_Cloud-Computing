import json
import os
import requests
import re
from time import gmtime, strftime
import subprocess


def handle(req):
    print(req)
    #Get the data from user side
    data  = json.loads(req)

    #Build the result for the query from a user
    result = {}
    if 'question' in data:
        print("!")
        query = data['question']
        if re.search(r'name', query):
            result = {"name" : "chatbot"}
        elif re.search(r'time', query):
            result = {"time" : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}
        else:
            result = {"error": "Invalid request payload"}
        print("!!!")

    elif 'figlet' in data:
        print("@")
        query = data['figlet']
        response = subprocess.Popen(f'echo {query} | faas-cli invoke figlet', shell=True)
        result = {"figlet" : json.loads(response.json())}
        #subprocess.check_output

        '''
        payload = {'q': query}
        url = f"http://127.0.0.1:8080/function/figlet"
        response = requests.get(url, params=payload)
        if response.status_code != 200:
            return json.dumps({"error": "Error fetching weather data"})

        print(json.loads(response.json()))
        result = {"figlet" : json.loads(response.json())}
        '''
    
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

    req = '{"figlet": "Hi"}'
    result = handle(req)
    print(json.loads(result))

