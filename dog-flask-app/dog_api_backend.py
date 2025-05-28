from flask import Flask, jsonify, request
import urllib.request
import json

app = Flask(__name__)

# Hello World endpoint
@app.route('/hello', methods=['GET'])
def get_hello():
    return "hello world!"

@app.route('/breeds', methods=['GET'])
def get_breeds():
    try:
        with urllib.request.urlopen('https://dogapi.dog/api/v2/breeds') as response:
            data = response.read()
            breeds = json.loads(data)

        return json.dumps(breeds), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/breeds/<breed_id>', methods=['GET'])
def get_breed_byID(breed_id):
    try:
        with urllib.request.urlopen(f'https://dogapi.dog/api/v2/breeds/{breed_id}') as response:
            data = response.read()
            breeds = json.loads(data)

        return json.dumps(breeds), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/facts', methods=['GET'])
def get_facts():
    try:
        with urllib.request.urlopen('https://dogapi.dog/api/v2/facts') as response:
            data = response.read()
            facts = json.loads(data)

        return json.dumps(facts), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/groups', methods=['GET'])
def get_groups():
    try:
        with urllib.request.urlopen('https://dogapi.dog/api/v2/groups') as response:
            data = response.read()
            groups = json.loads(data)

        return json.dumps(groups), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/groups/<group_id>', methods=['GET'])
def get_groups_byID(group_id):
    try:
        with urllib.request.urlopen(f'https://dogapi.dog/api/v2/groups/{group_id}') as response:
            data = response.read()
            group = json.loads(data)

        return json.dumps(group), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/group-details/<group_id>', methods=['GET'])
def get_groupDetails_byGroupID(group_id):
    try:
        with urllib.request.urlopen(f'https://dogapi.dog/api/v2/groups/{group_id}') as response:
            data = response.read()
            group_detail = json.loads(data.decode('utf-8').replace('data', 'group_details'))

        return json.dumps(group_detail), 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

@app.route('/group-details/<group_id>/breed/<breed_id>', methods=['GET'])
def get_breed_byGroupID_byBreedID(group_id, breed_id):
    try:
        with urllib.request.urlopen(f'https://dogapi.dog/api/v2/groups/{group_id}') as response:
            data = response.read()
            data = json.loads(data)
            group_breeds = data.get('data', {}).get('relationships', {}).get('breeds', {}).get('data', [])
            print(group_breeds)

        group_breeds = [breed for breed in group_breeds if breed.get('id') == breed_id]
        
        if not group_breeds:
            return json.dumps({'error': 'Breed not found in the specified group'}), 404, {'Content-Type': 'application/json'}
        group_breeds = group_breeds[0]  # Assuming we want the first match
        
        group_breeds = {
            'id': group_breeds.get('id'),
            'type': group_breeds.get('type'),
            'status': group_breeds.get('status', 'OK!'),
        }

        return json.dumps(group_breeds), 200, {'Content-Type': 'application/json' , 'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    app.run(debug=True, port=5000)