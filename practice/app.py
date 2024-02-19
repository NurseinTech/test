from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources import(
    UserRegistrationResource, 
    UserLoginResource, 
    RoomResource, 
    AdminRoomResource, 
    HostelResource,
    AdminHostelResource,
    ReviewResource
)

from models import db

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

migrate = Migrate(app, db)
jwt = JWTManager(app)

db.init_app(app)
api = Api(app)


api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(ReviewResource,'/reviews','/reviews/<int:review_id>')
api.add_resource(RoomResource, '/rooms','/rooms/<int:room_id>')
api.add_resource(AdminRoomResource, '/rooms/<int:room_id>')
api.add_resource(HostelResource, '/hostel','/hostel/<int:hostel_id>')
api.add_resource(AdminHostelResource, '/hostel/<int:hostel_id>')
if _name_ == '_main_':
    app.run(port=5555)