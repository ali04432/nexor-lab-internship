from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Continuous Deployment (CD) Auto-Deploy Successful!"
    })

@app.route('/health')
def health_check():
    # Health verification check required by CD pipeline
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    