from flask import Flask, request, jsonify
import requests
import json

students = {"s1":"fausto",
            "s2":"anna", 
            "s3":"rakshanda",
            "s4":"elston", 
            }


headers = {"Content-Type": "application/json"}

r = requests.post("http://127.0.0.1:5000/", params=students, headers=headers)
json_resp = json.loads(r.text) 
json_resp



headers = {"Content-Type": "application/json"}

r = requests.delete("http://127.0.0.1:5000/", params=student, headers=headers)
json_resp = json.loads(r.text) 
json_resp

app = Flask(__name__)

d = {}

@app.route('/', methods=['GET'])
def get_student():
    return jsonify(d)

@app.route('/', methods=['POST'])
def create_student():
    added = {}
    for k,v in request.args.items():
        if not k in d.keys():
            added[k] = v
            d[k] = v
    return jsonify({"added": added, "current": d})

@app.route('/', methods=['DELETE'])
def delete_student():
    deleted = {}
    for k,v in request.args.items():
        try:
            d.pop(k)
            deleted[k] = v
        except:
            continue
    return jsonify({"deleted": deleted, "current": d})
                
if __name__ == '__main__':
    app.run(debug=True)