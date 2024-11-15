from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import File
from utils.encryption import generate_download_link
from utils.auth_decorator import role_required

client_user_bp = Blueprint('client_user', __name__)

@client_user_bp.route('/files', methods=['GET'])
@jwt_required()
@role_required('client')
def list_files():
    files = File.query.all()
    return jsonify([{"id": file.id, "filename": file.filename} for file in files]), 200

@client_user_bp.route('/download/<int:file_id>', methods=['GET'])
@jwt_required()
@role_required('client')
def download_file(file_id):
    file = File.query.get(file_id)
    if not file:
        return jsonify({"message": "File not found"}), 404

    download_link = generate_download_link(file.filename)
    return jsonify({"download_link": download_link}), 200
