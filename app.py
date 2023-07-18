from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, mysql

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
    
@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    # store this in the DB
    # send an email
    # display an acknowledgement
    add_application_to_db(id, data)
    return render_template('application_submitted.html',
                           application=data,
                           job=job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)