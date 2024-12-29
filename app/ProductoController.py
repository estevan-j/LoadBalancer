from flask import Blueprint, request, jsonify
from .ProductoService import get_all_productos, get_producto_by_id, create_producto, update_producto, delete_producto

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def get_all():
    productos = get_all_productos()
    return jsonify([prod.to_dict() for prod in productos])

@productos_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    producto = get_producto_by_id(id)
    if producto:
        return jsonify(producto.to_dict())
    return jsonify({'message': 'Producto no encontrado'}), 404

@productos_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    nuevo_producto = create_producto(data)
    return jsonify(nuevo_producto.to_dict()), 201

@productos_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    producto = update_producto(id, data)
    if producto:
        return jsonify(producto.to_dict())
    return jsonify({'message': 'Producto no encontrado'}), 404

@productos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    producto = delete_producto(id)
    if producto:
        return jsonify({'message': 'Producto eliminado'})
    return jsonify({'message': 'Producto no encontrado'}), 404