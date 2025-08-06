from flask import Flask, request, jsonify
from cache.factory import get_cache_backend

app = Flask(__name__)
cache = get_cache_backend()

@app.route('/set', methods=['POST'])
def set_cache():
    data = request.json
    key = data.get("key")
    value = data.get("value")
    expire = data.get("expire", 3600)
    cache.set(key, value, expire)
    return jsonify({"message": f"{key} set successfully"})

@app.route('/get/<key>', methods=['GET'])
def get_cache(key):
    value = cache.get(key)
    if value is None:
        return jsonify({"message": "Key not found"}), 404
    return jsonify({"key": key, "value": value.decode() if isinstance(value, bytes) else value})

@app.route('/delete/<key>', methods=['DELETE'])
def delete_cache(key):
    cache.delete(key)
    return jsonify({"message": f"{key} deleted successfully"})

@app.route('/clear', methods=['POST'])
def clear_cache():
    cache.clear()
    return jsonify({"message": "Cache cleared successfully"})

if __name__ == '__main__':
    app.run(debug=True)
