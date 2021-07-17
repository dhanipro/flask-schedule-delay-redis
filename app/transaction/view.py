from . import transaction as bp
from ..model import Product, Transaction
from app import db
from flask import current_app
from datetime import timedelta

@bp.route('/order/<int:product_id>', methods=['GET'])
def order(product_id):
    product = Product.query.get_or_404(product_id)
    transaction = Transaction(
        amount = 1000000,
        status_transaksi = 'pending',
        product = product

    )
    db.session.add(transaction)
    db.session.commit()

    # kirim ke task/worker untuk dicek dalam 15 detik
    current_app.task_queue.enqueue_in(
            timedelta(seconds=15),
            'app.task.cek_billing',
            transaction.id
        )
    return {'success': 'Order berhasil, status akan expired dalam 15 detik'}

@bp.route("/get-order/<int:transaction_id>", methods=['GET'])
def get_order(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    return {'message': f'Status transaksi {transaction.status_transaksi}'}