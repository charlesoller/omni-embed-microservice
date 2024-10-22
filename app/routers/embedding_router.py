from flask import Blueprint, jsonify, request, current_app
from app.services.embedding_service import EmbeddingService
from werkzeug.exceptions import BadRequest

embed = Blueprint('embed', __name__)

@embed.route('/')
def hello():
    return "Hello, Embedding!"

@embed.route('/', methods=['POST'])
def create_embedding():
    model = current_app.config.get("MODEL")
    embedding_service = EmbeddingService(model)

    try:
        if not request.is_json:
            return jsonify({"error": "Invalid JSON request"}), 400
        
        data = request.json.get('data')

        if data is None:
            return jsonify({"error": "'data' field is required"}), 400

        try:
            embedding = embedding_service.create_embedding(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500 

        return jsonify({"embedding": embedding}), 201

    except BadRequest as e:
        return jsonify({"error": "Bad request: " + str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

