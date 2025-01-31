from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
    
@app.route('/stats')
def get_stats():
  chick = 0
  fish = 0
  veg = 0
  compSciM = 0
  compSciS = 0
  InfoM = 0
  InfoS = 0
  for student in data:
    if student['pref'] == 'Chicken':
      chick += 1
    if student['pref'] == 'Fish':
      fish += 1
    if student['pref'] == 'Vegetable':
      veg += 1
    if student['programme'] == 'Computer Science (Major)':
      compSciM += 1
    if student['programme'] == 'Computer Science (Special)':
      compSciS += 1
    if student['programme'] == 'Information Technology (Major)':
      InfoM += 1
    if student['programme'] == 'Information Technology (Special)':
      InfoS += 1
  
  stat = {
        "Chicken":chick,
        "Computer Science (Major)":compSciM,
        "Computer Science (Special)":compSciS,
        "Fish":fish,
        "Information Technology (Major)":InfoM,
        "Information Technology (Special)":InfoS,
        "Vegetable":veg
  }
  return stat

app.run(host='0.0.0.0', port=8080, debug=True)
