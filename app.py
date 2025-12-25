from flask import Flask
import os, platform, datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #2c3e50;">🚀 DevOps Build Successful!</h1>
            <p><b>Container Image:</b> ghcr.io/tritmeri/my-app:latest</p>
            <p><b>Deployed on:</b> {platform.system()} ({platform.node()})</p>
            <p><b>Current Time:</b> {now}</p>
            <div style="background: #ecf0f1; padding: 20px; border-radius: 10px; display: inline-block;">
                Status: <span style="color: green;">● Healthy</span>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
