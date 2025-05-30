from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connector import get_all_students, add_student, update_student, delete_student

app = Flask(__name__)
CORS(app)

@app.route('/api/students', methods=['GET'])
def students():
    try:
        students = get_all_students()
        return jsonify(students)
    except Exception as e:
        print(f"Error fetching students: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/students', methods=['POST'])
def add():
    try:
        data = request.json
        add_student(data['name'], data['age'], data['department'])
        return jsonify({'status': 'Student added'})
    except Exception as e:
        print(f"Error adding student: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/students/<int:id>', methods=['PUT'])
def edit(id):
    try:
        data = request.json
        update_student(id, data['name'], data['age'], data['department'])
        return jsonify({'status': 'Student updated'})
    except Exception as e:
        print(f"Error updating student: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        delete_student(id)
        return jsonify({'status': 'Student deleted'})
    except Exception as e:
        print(f"Error deleting student: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
