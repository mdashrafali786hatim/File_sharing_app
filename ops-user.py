from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, File
from utils.auth_decorator import role_required
import os
from werkzeug.utils import secure_filename
from config import Config

ops_user_bp = Blueprint('ops_user', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@ops_user_bp.route('/upload', methods=['POST'])
@jwt_required()
@role_required('ops')
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(Config.UPLOAD_FOLDER, filename))

        uploader_id = get_jwt_identity()['id']
        new_file = File(filename=filename, uploader_id=uploader_id)
        db.session.add(new_file)
        db.session.commit()

        return jsonify({"message": "File uploaded successfully"}), 201
    return jsonify({"message": "Invalid file type"}), 400
