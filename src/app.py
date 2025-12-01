"""Flask web application for warehouse management"""
from flask import Flask, render_template, request, redirect, url_for, flash
from varasto import Varasto

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'


# In-memory storage for warehouses
class WarehouseManager:  # pylint: disable=too-few-public-methods
    """Manages warehouse storage"""
    def __init__(self):
        self.warehouses = {}
        self.counter = 0

    def add_warehouse(self, name, tilavuus, alku_saldo):
        """Add new warehouse"""
        warehouse = Varasto(tilavuus, alku_saldo)
        self.counter += 1
        self.warehouses[self.counter] = {
            'id': self.counter,
            'name': name,
            'varasto': warehouse
        }
        return self.counter


manager = WarehouseManager()


@app.route('/')
def index():
    """Display list of all warehouses"""
    return render_template('index.html', warehouses=manager.warehouses)


@app.route('/create', methods=['GET', 'POST'])
def create_warehouse():
    """Create a new warehouse"""
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            tilavuus = float(request.form.get('tilavuus', 0))
            alku_saldo = float(request.form.get('alku_saldo', 0))
            manager.add_warehouse(name, tilavuus, alku_saldo)
            flash(f'Varasto "{name}" luotu onnistuneesti!', 'success')
            return redirect(url_for('index'))
        except ValueError as error:
            flash(f'Virhe: {error}', 'error')

    return render_template('create_warehouse.html')


@app.route('/warehouse/<int:warehouse_id>')
def warehouse_detail(warehouse_id):
    """Display warehouse details"""
    if warehouse_id not in manager.warehouses:
        flash('Varastoa ei löytynyt', 'error')
        return redirect(url_for('index'))

    warehouse = manager.warehouses[warehouse_id]
    return render_template('warehouse_detail.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/add', methods=['GET', 'POST'])
def add_stock(warehouse_id):
    """Add stock to warehouse"""
    if warehouse_id not in manager.warehouses:
        flash('Varastoa ei löytynyt', 'error')
        return redirect(url_for('index'))

    warehouse_data = manager.warehouses[warehouse_id]

    if request.method == 'POST':
        maara = float(request.form.get('maara', 0))
        warehouse_data['varasto'].lisaa_varastoon(maara)
        flash(f'Lisättiin {maara} yksikköä varastoon', 'success')
        return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))

    return render_template('add_stock.html', warehouse=warehouse_data)


@app.route('/warehouse/<int:warehouse_id>/remove', methods=['GET', 'POST'])
def remove_stock(warehouse_id):
    """Remove stock from warehouse"""
    if warehouse_id not in manager.warehouses:
        flash('Varastoa ei löytynyt', 'error')
        return redirect(url_for('index'))

    warehouse_data = manager.warehouses[warehouse_id]

    if request.method == 'POST':
        maara = float(request.form.get('maara', 0))
        saatu = warehouse_data['varasto'].ota_varastosta(maara)
        flash(f'Otettiin {saatu} yksikköä varastosta', 'success')
        return redirect(url_for('warehouse_detail', warehouse_id=warehouse_id))

    return render_template('remove_stock.html', warehouse=warehouse_data)


@app.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    """Delete a warehouse"""
    if warehouse_id in manager.warehouses:
        name = manager.warehouses[warehouse_id]['name']
        del manager.warehouses[warehouse_id]
        flash(f'Varasto "{name}" poistettu', 'success')
    else:
        flash('Varastoa ei löytynyt', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
