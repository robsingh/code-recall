from flask import Flask, request, jsonify
from add_problem import adding_problem
from due_today import show_due_today
from review import mark_reviewed

app = Flask(__name__)

@app.route("/problems",methods=["POST"])
def app_problem_route():
    data = request.get_json()

    # access title, problem and solution
    title = data.get('title')
    problem = data.get('problem')
    solution = data.get('solution')

    if not title or not problem or not solution:
        return jsonify({"error":"Invalid request parameters"}), 400
    
    adding_problem(title, problem, solution)
    return jsonify({"status": "success"}),200


@app.route("/problems/due", methods=["GET"])
def app_due_route():
    count, records = show_due_today()
    problems_list = []
    for record in records:
        problem_dict = {
            "title": record[0],
            "solution": record[1],
            "current_stage": record[2],
            "next_review_date": record[3]
        }
        problems_list.append(problem_dict)
    return jsonify({"count":count, "due":problems_list})
  

@app.route("/problems/<title>/review", methods=["PUT"])
def app_mark_reviewed(title):
    result = mark_reviewed(title)
    if result["success"]:
        return jsonify({"status":"success", "new_stage": result["new_stage"], "next_review_date": result["next_review_date"]}),200
    else:
        return jsonify({"status": "failure"}),400


if __name__ == "__main__":
    app.run(debug=True)