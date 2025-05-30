from flask import Flask, render_template

app = Flask(__name__)

# Static data just like Node version
portfolio_data = {
    "name": "Rosan A",
    "tagline": "Aspiring DevOps Engineer",
    "skills": [
        "Database Migration",
        "3-Tier App Deployment",
        "End-to-End CI/CD",
        "Network Provisioning (IaC - Terraform)"
    ],
    "projects": [
        {
            "title": "Database Migration",
            "description": "Migrated legacy databases to AWS RDS with zero downtime."
        },
        {
            "title": "3-Tier Application Deployment",
            "description": "Deployed scalable 3-tier apps on AWS using EC2, ELB, and RDS."
        },
        {
            "title": "End-to-End CI/CD",
            "description": "Automated build, test, and deployment pipelines using Jenkins and GitHub Actions."
        },
        {
            "title": "Network Provisioning with IaC",
            "description": "Provisioned secure VPCs and subnets using Terraform."
        }
    ],
    "contact": {
        "email": "rosan.a@example.com",
        "github": "https://github.com/rosan-a",
        "linkedin": "https://linkedin.com/in/rosan-a"
    }
}

@app.route('/')
def index():
    return render_template('about.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
