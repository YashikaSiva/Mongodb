
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://yashikas_db_user:KXGjhzlQ9smVRoD0@cluster0.d2xagn5.mongodb.net/?appName=Cluster0&retryWrites=true&w=majority")
db = client["College"]
students = db["students"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        roll = int(request.form["roll"])
        name = request.form["name"]
        dept = request.form["dept"]
        action = request.form["action"]

        if action == "Insert":
            students.insert_one({
                "roll": roll, "name": name, "dept": dept
            })

        elif action == "Update":
            students.update_one(
                {"roll": roll},
                {"$set": {"name": name, "dept": dept}}
            )

        elif action == "Delete":
            students.delete_one({"roll": roll})

    data = list(students.find())
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
