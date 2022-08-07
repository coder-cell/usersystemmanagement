
from flask import Flask, jsonify, abort
from waitress import serve


class UserRecord:
    def toJSON(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "since": self.since
        }


class UserController:
    def __new__(self):
        if not hasattr(self, "instance"):
            self.instance = super().__new__(self)

    def __init__(self):
        self._repo = UserRepositoryImpl()

    def find(self, name: str):
        try:
            user: User = self._repo.fetch(Name(name))
            record: UserRecord = UserRecord()
            record.name = user.name.getValue()
            record.phone = user.phone.getValue()
            record.since = user.since
            return record
        except UserNotFoundException as e:
            return None


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1 style='color:blue'> Welcome to User Management System! </h1>"


@app.route('/user/<name>')
def get(name):
    controller = UserController()
    record = controller.find(name)
    if record is None:
        abort(404)
    else:
        resp = jsonify(record.toJSON())
        resp.status_code = 200
        return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
