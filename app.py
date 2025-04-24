from flask import Flask, jsonify
import os

app = Flask(__name__)

 #Simulación de productos
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 2500},
    {"id": 2, "nombre": "Smartphone", "precio": 1200},
    {"id": 3, "nombre": "Auriculares", "precio": 250},
]


@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
