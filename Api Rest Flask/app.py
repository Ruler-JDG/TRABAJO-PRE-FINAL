from flask import Flask, jsonify, request
import json
import uuid

app = Flask(__name__)
DB_FILE = "giftcards.json"

def read_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/giftcards", methods=["GET"])
def get_giftcards():
    return jsonify(read_db())

@app.route("/giftcards", methods=["POST"])
def create_giftcard():
    data = request.json
    new_giftcard = {
        "id": str(uuid.uuid4()),
        "codigo": data.get("codigo"),
        "monto": data.get("monto"),
        "estado": data.get("estado", "activo")
    }
    db = read_db()
    db.append(new_giftcard)
    write_db(db)
    return jsonify(new_giftcard), 201

@app.route("/giftcards/<id>", methods=["GET"])
def get_giftcard(id):
    db = read_db()
    item = next((g for g in db if g["id"] == id), None)
    return jsonify(item) if item else ({"error": "No encontrado"}, 404)

@app.route("/giftcards/<id>", methods=["PUT"])
def update_giftcard(id):
    db = read_db()
    item = next((g for g in db if g["id"] == id), None)

    if not item:
        return {"error": "No encontrado"}, 404

    data = request.json
    item["codigo"] = data.get("codigo", item["codigo"])
    item["monto"] = data.get("monto", item["monto"])
    item["estado"] = data.get("estado", item["estado"])

    write_db(db)
    return jsonify(item)

@app.route("/giftcards/<id>", methods=["DELETE"])
def delete_giftcard(id):
    db = read_db()
    new_db = [g for g in db if g["id"] != id]

    if len(new_db) == len(db):
        return {"error": "No encontrado"}, 404

    write_db(new_db)
    return {"message": "Eliminado correctamente"}

if __name__ == "__main__":
    app.run(debug=True)
