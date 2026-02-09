from flask import Flask, jsonify

app = Flask(__name__)

def get_version():
    # Returns flask-app version from the first line of README.md
    try:
        with open("README.md", "r") as f:
            line = f.readline()
            for part in line.split():
                if part.startswith("v"):
                    return part
    except FileNotFoundError:
        return "unknown"
    
@app.route("/")
def home():
    version = get_version()
    return f"""
    <html>
      <head>
        <title>Welcome to Flask-App</title>
        <!-- jQuery first -->
        <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        <!-- Notify.js -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/notify/0.4.2/notify.min.js"></script>
      </head>
      <body>
        <h1>Flask-App</h1>
        <p>Version: {version}</p>

        <script>
          $(function() {{
            $.notify("App is running! Version: {version}", "success");
          }});
        </script>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200