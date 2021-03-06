import requests
import ClickUpVariables
from flask import Flask, request, render_template, session, url_for,make_response

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    headers = {"Authorization": ClickUpVariables.apikey,"Content-Type": "application/json"}
    url = "https://api.clickup.com/api/v2/list/" + ClickUpVariables.listID + "/task"

    if request.method == "POST":
        # for x in request.form:
        #     print (x + " : " + request.form[x])

        if "kingTaskDesc" in request.form:
            retries = 0
            addTaskKing = request.form["kingTaskDesc"]
            if addTaskKing == "":
                return render_template("tasksHome.html")
            values = {
            "name": addTaskKing,
            "assignees": [32644579],
            "status": "KING",
            "priority": 3
            }
            response = requests.post(url,json=values,headers=headers)
            while response.status_code != 200:
                retries +=1
                print ("Try #" + str(retries))
                response = requests.post(url,json=values,headers=headers)
                if retries == 3:
                    submitSuccessful = "PLEASE TRY AGAIN"
                    return render_template("tasksHome.html",data=submitSuccessful)
            submitSuccessful = "Task submitted successfully"

        if "princessTaskDesc" in request.form:
            retries = 0
            addTaskPrincess = request.form["princessTaskDesc"]
            if addTaskPrincess == "":
                return render_template("tasksHome.html")
            values = {
                "name": addTaskPrincess,
                "assignees": [32644580],
                "status": "PRINCESS",
                "priority": 3
              }
            response = requests.post(url,json=values,headers=headers)
            while response.status_code != 200:
                retries +=1
                print ("Try #" + str(retries))
                response = requests.post(url,json=values,headers=headers)
                if retries == 3:
                    submitSuccessful = "PLEASE TRY AGAIN"
                    return render_template("tasksHome.html",data=submitSuccessful)
            submitSuccessful = "Task submitted successfully"
        return render_template("tasksHome.html",data=submitSuccessful)

    if request.method == "GET":
        return render_template("tasksHome.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
