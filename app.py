from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    repo_status = None
    if request.method == "POST":
        repo_name = request.form["repo_name"]
        response = requests.get(f"https://api.github.com/repos/{repo_name}")
        if response.status_code == 200:
            repo_status = "Repository is available!"
        else:
            repo_status = "Repository not found!"
    return render_template("index.html", repo_status=repo_status)

if __name__ == "__main__":
    # Hardcoded port value
    app.run(host="0.0.0.0", port=5000, debug=False)
