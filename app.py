from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_products, get_product, add_to_cart, get_cart_items, remove_from_cart, get_search_results

app = Flask(__name__)
app.secret_key = '1234'
@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = get_product(product_id)
    if product is None:
        return "Product not found", 404
    return render_template('product.html', product=product)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart_route():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    add_to_cart(product_id, int(quantity))
    return redirect(url_for('index'))


@app.route('/remove_from_cart',methods=['POST'])
def remove_from_cart_route():
    product_id=request.form.get('product_id')
    remove_from_cart(product_id)
    return redirect(url_for('cart'))


@app.route('/search')
def search_results():
    query = request.args.get('query')
    products = get_search_results(query)
    return render_template('search_results.html', products=products, query=query)

@app.route('/product/<int:product_id>/buy_now',methods=['GET','POST'])
def buy_now(product_id):
    if request.method == 'POST':
        quantity = int(request.form.get('quantity',1))
        add_to_cart(product_id,quantity)
        flash('Item added successfully!','success')
        return redirect(url_for('cart'))
    
    product = get_product(product_id)
    if product is None:
        return "Product not found",404
    
    return render_template('buy_now.html',product=product)

@app.route('/cart')
def cart():
    cart_items = get_cart_items()
    print(f"Cart items: {cart_items}") 
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)

