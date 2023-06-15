from flask import Flask, request, jsonify
app = Flask(__name__)

tasks = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route("/health-check")
def health_check():
    return "Hello World!"    

@app.route('/todos', methods=['GET'])
def get_all_tasks():
        if request.method == 'GET':
            return jsonify(tasks)
        return jsonify({"message":"Wrong request"}), 400

@app.route('/todos', methods=['POST'])
def add_task():
        if request.method == 'POST':
            response = request.json

            if type(response["done"]) != bool:
                return jsonify({"message":"Wrong property"}), 400
            if response.get("label") is None:
                return jsonify({"message":"Wrong property"}), 400
            
            tasks.append(response)
            return jsonify(tasks)

        return jsonify("Method not allowed"), 405

@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_task(task_id = None):
        if request.method == 'DELETE':

            if len(tasks) == 0:
                return jsonify({"message":"Wrong request"}), 400
            
            if task_id is not None:
                if task_id < len(tasks):
                    for task in tasks:
                        if task == tasks[task_id]:
                            tasks.remove(task)       
                else:
                    return jsonify({"message":"Wrong request"}), 400
                  
            return jsonify({"message":"Passed"}), 200        

        return jsonify("Method not allowed"), 405

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)