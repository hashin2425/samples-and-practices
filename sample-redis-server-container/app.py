from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
redis_client = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)


@app.route("/")
def hello():
    return "Hello! This is the Flask server."


@app.route("/set/<key>/<value>")
def set_value(key, value):
    redis_client.set(key, value)
    return jsonify({"message": f"Set {key} to {value}"})


@app.route("/get/<key>")
def get_value(key):
    value = redis_client.get(key)
    if value:
        return jsonify({key: value.decode("utf-8")})
    return jsonify({"message": "Key not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
