from flask import request

from app import app


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
    return {"ok": True}
