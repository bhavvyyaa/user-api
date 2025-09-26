from flask import Flask, jsonify, request
app = Flask(__name__)
users = [{"id": 1, "username": "alice", "email": "alice@example.com"},
         {"id": 2, "username": "bob", "email": "bob@example.com"},
]
next_user_id = 3
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None )
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/users', methods=['POST'])
def create_user():
    global next_user_id
    new_user_data = request.json
    if not new_user_data or 'username' not in new_user_data or 'email' not in new_user_data:
        return jsonify({"error": "Invalid username/email"}), 400
    new_user = {
        "id": next_user_id,
        "username": new_user_data['username'],
        "email": new_user_data['email']
    }
    users.append(new_user)
    next_user_id += 1
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    update_data = request.json()
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), -1)
    if user_index == -1:
        return jsonify({"error":f"User with ID {user_id} not found"}), 404
    user_to_update = users[user_index]
    if 'username' in update_data:
        user_to_update['username'] = update_data['username']
    if 'email' in update_data:
        user_to_update['email'] = update_data['email']
    return jsonify(user_to_update), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), -1)
    if user_index == -1:
        return jsonify({"error":f"User with ID {user_id} not found"}), 404
    users.pop(user_index)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)