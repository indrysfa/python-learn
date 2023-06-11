from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create an instance of the Flask application
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# instatiate db object
db = SQLAlchemy(app)
# instatiate marshmallow object
ma = Marshmallow(app)


# create database
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id


# create Member schema
class MemberSchema(ma.Schema):
    class Meta:
        fields = ("name", "email", "status", "date_created")


# create instance of schemas
member_schema = MemberSchema(many=False)
members_schema = MemberSchema(many=True)


# route
@app.route("/")
def home():
    return "Home"


@app.route("/member", methods=["POST"])
def create_member():
    try:
        name = request.json["name"]
        email = request.json["email"]

        new_member = Member(name=name, email=email)

        db.session.add(new_member)
        db.session.commit()

        return member_schema.jsonify(new_member)

    except Exception as e:
        return jsonify({"Error": "invalid request."})


@app.route("/user/<user_id>", methods=["GET"])
def get_user(id):
    user_data = {"user_id": id, "name": "Joe", "email": "mail@gmail.com"}
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route("/user/create", methods=["POST"])
def create_user():
    try:
        data = request.get_json()

        return jsonify(data), 201

    except Exception as e:
        return jsonify({"Error": "Invalid request."})


# @app.route("/user/<int:id>", methods=["PUT"])
# def update_user(id):
#     user_data = {"user_id": id, "name": "Joe", "email": "mail@gmail.com"}
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
