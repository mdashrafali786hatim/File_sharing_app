from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.ops_user import ops_user_bp
    from routes.client_user import client_user_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(ops_user_bp, url_prefix='/api/ops')
    app.register_blueprint(client_user_bp, url_prefix='/api/client')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
