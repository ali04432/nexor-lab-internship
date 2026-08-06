from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "task": "Zero Downtime Deployments",
        "version": "1.0.0",
        "status": "Running smoothly without downtime"
    })

# Health Check Route for zero-downtime cutover
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "code": 200}), 200

if __name__ == '__main__':
    app.run()