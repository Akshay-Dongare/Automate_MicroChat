from app import app as flask_app
from app import socketio as app


if __name__ == "__main__":
    app.run(app=flask_app, debug=True, host="localhost", port=3000, use_reloader=False)