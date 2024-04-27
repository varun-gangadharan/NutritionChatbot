from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates/folder')
    print("Creating app...")
    # Import routes after app creation to avoid circular imports
    from app import routes

    return app
