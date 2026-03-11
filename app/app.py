from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<html>
    <head>
        <title>DevOps Project</title>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 200px;
            }
            h1 {
                font-size: 40px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 DevOps CI/CD Kubernetes Project Running 🟢🚀🟢🚀🟢🚀</h1>
        <p>Powered by Docker + Kubernetes + ArgoCD</p>
    </body>
    </html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
