from app import create_app, db

app = create_app()

@app.cli.command('set-database')
def set_database():
    '''Set database & insert data'''
    from app.model import Product
    db.create_all()
    print('Database selesai dibuat...!!!')
    
    # menambahkan produk
    product = Product(
        product_name = 'Macbook Pro',
        price = 15000000
    )
    db.session.add(product)
    db.session.commit()
    print('Menambahkan produk selesai...')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)