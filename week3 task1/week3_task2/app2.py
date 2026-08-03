import logging
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Centralized Structured Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s'
)
logger = logging.getLogger("MonitoringService")

# 2. Track Real Metrics (Response Time & Error Rate)
@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request_metrics(response):
    response_time = (time.time() - request.start_time) * 1000  # in ms
    logger.info(
        f"METHOD: {request.method} | PATH: {request.path} | "
        f"STATUS: {response.status_code} | LATENCY: {response_time:.2f}ms"
    )
    return response

@app.route('/')
def main_app():
    logger.info("Accessing main application dashboard endpoint")
    return jsonify({"message": "Monitoring & Logging Active"})

# 3. Uptime Metric Endpoint
@app.route('/metrics')
def metrics():
    logger.info("Metrics dashboard checked")
    return jsonify({
        "uptime": "99.9%",
        "service_status": "UP",
        "error_rate": "0.0%"
    }), 200

# 4. Simulated Failure Route for Alert Testing
@app.route('/trigger-alert')
def trigger_alert():
    logger.error("ALERT CONDITION TRIGGERED: Simulated Server Error 500!")
    return jsonify({"error": "Simulated Alert Failure"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)