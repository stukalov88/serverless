from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Serverless! 🚀\n"

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "status": "received",
        "you_sent": data,
        "length": len(str(data)) if data else 0
    })

if __name__ == '__main__':
    # Render автоматически назначает порт. Если его нет, используем 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
