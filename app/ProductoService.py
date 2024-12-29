from .Producto import Producto
from . import db

def get_all_productos():
    return Producto.query.all()

def get_producto_by_id(id):
    return Producto.query.get(id)

def create_producto(data):
    nuevo_producto = Producto(**data)
    db.session.add(nuevo_producto)
    db.session.commit()
    return nuevo_producto

def update_producto(id, data):
    producto = Producto.query.get(id)
    if producto:
        for key, value in data.items():
            setattr(producto, key, value)
        db.session.commit()
    return producto

def delete_producto(id):
    producto = Producto.query.get(id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
    return producto