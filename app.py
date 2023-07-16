from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

    
@app.route("/")
def hello_world():
    jobs_list = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs_list,
                           company_name="Jovian")
    
@app.route("/api/jobs")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)

# <> indicate a dynamic route. In this case, to switch between jobs.

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if job:
        return render_template('jobpage.html',
                                job=job)
    return "Error job not found", 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)