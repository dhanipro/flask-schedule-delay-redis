from app import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    transactions = db.relationship('Transaction', backref='product', lazy='dynamic')

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric)
    status_transaksi = db.Column(db.String(20), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)