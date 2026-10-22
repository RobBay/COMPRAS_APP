cat << 'EOF' > app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola! Tu servidor de Flask está funcionando correctamente. 🚀"

if __name__ == "__main__":
    app.run(debug=True)
EOF