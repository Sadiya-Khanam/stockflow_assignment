from flask import jsonify
from datetime import timedelta, datetime
from app import app, db
from models import Warehouse, Inventory, Product, Supplier, ProductSupplier, Sale

# API to get low stock alerts for a company
@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    # Calculate date 30 days ago from today
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    alerts = []

    # Get all warehouses for the given company
    warehouses = Warehouse.query.filter_by(company_id=company_id).all()

    for warehouse in warehouses:
        # Get inventory items with product info for this warehouse
        inventory_items = db.session.query(Inventory, Product)\
            .join(Product, Inventory.product_id == Product.id)\
            .filter(Inventory.warehouse_id == warehouse.id).all()

        for inventory, product in inventory_items:
            # If quantity is fine, no alert needed
            if inventory.quantity > product.threshold:
                continue

            # Get sales in last 30 days for this product in this warehouse
            recent_sales = Sale.query.filter(
                Sale.product_id == product.id,
                Sale.warehouse_id == warehouse.id,
                Sale.sold_at >= thirty_days_ago
            ).all()

            if not recent_sales:
                continue  # No recent activity, so skip alert

            # Estimate how many days until stock runs out
            total_sold = sum(sale.quantity for sale in recent_sales)
            avg_daily = total_sold / 30 if total_sold else 1 
            days_until_stockout = int(inventory.quantity / avg_daily)

            # Get first supplier linked to this product
            supplier = db.session.query(Supplier)\
                .join(ProductSupplier)\
                .filter(ProductSupplier.product_id == product.id)\
                .first()

            # Add this product to the alerts list
            alerts.append({
                "product_id": product.id,
                "product_name": product.name,
                "sku": product.sku,
                "warehouse_id": warehouse.id,
                "warehouse_name": warehouse.name,
                "current_stock": inventory.quantity,
                "threshold": product.threshold,
                "days_until_stockout": days_until_stockout,
                "supplier": {
                    "id": supplier.id if supplier else None,
                    "name": supplier.name if supplier else None,
                    "contact_email": supplier.contact_email if supplier else None
                }
            })

    # Return all alerts in JSON format
    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })
