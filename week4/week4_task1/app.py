import os
from flask import Flask, jsonify

app = Flask(__name__)

# Config defined in code (IaC concept)
SERVICE_NAME = os.getenv("SERVICE_NAME", "IaC-Service")
ENVIRONMENT = os.getenv("ENV", "production")

@app.route('/')
def home():
    return jsonify({
        "task": "Infra as Code",
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT,
        "status": "Infrastructure provisioned via code"
    })

if __name__ == '__main__':
    app.run()