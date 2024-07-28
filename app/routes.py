from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/files', methods=['GET'])
def list_files():
    # פה נכניס בהמשך את הקוד להחזרת רשימת הקבצים
    return jsonify(["example1.yaml", "example2.yaml"])