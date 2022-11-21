from flask import Flask,jsonify
from flask_smorest import Api
from db1 import db   
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
import models
import secrets

app=Flask(__name__)

from Resources.item import blp as ItemBlueprint
from Resources.store import blp as StoreBlueprint  
from Resources.tag import blp as TagBlueprint 
from Resources.user import blp as UserBlueprint 


def create_app(db_url=None):
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)

    api=Api(app)

    app.config["JWT_SECRET_KEY"]="257480245991062563636476392718995619324"
    jwt=JWTManager(app)
    
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header,jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header,jwt_payload):
        return (jsonify({"message":"the token has been revoked","error":"token_revoked"}),401)

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header,jwt_payload):  
        return (jsonify({"description":"The token is not fresh","error":"fresh_token_required"}),401)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity==1:
            return {"is_admin":True}
        return {"is_admin":False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header,jwt_payload):
        return (jsonify({"message":"The token has expired","error":"token_expired"}),401)

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (jsonify({"message":"signature verification failed","error":"invalid_token"}),401)

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (jsonify({"description":"request does not contain access token","error":"authorization_required"}),401)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)      


    return app   


