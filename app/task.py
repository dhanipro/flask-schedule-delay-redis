from app import create_app, db
from .model import Transaction

app = create_app()
app.app_context().push()

def cek_billing(id):
    transaksi = Transaction.query.get(id)
    if transaksi:
        if transaksi.status_transaksi == 'pending':
            transaksi.status_transaksi = 'expired'   
    db.session.commit()