/* Companies table */
CREATE TABLE companies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

/* Warehouses table */ 
CREATE TABLE warehouses (
  id SERIAL PRIMARY KEY,
  company_id INT NOT NULL REFERENCES companies(id),
  name VARCHAR(255) NOT NULL
);

/* Products table */
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  sku VARCHAR(100) UNIQUE NOT NULL,
  price DECIMAL(10, 2),
  type VARCHAR(50) DEFAULT 'single',       /* or'bundle' */
 );

/* Inventory table (product + warehouse stock) */
CREATE TABLE inventory (
  product_id INT REFERENCES products(id),
  warehouse_id INT REFERENCES warehouses(id),
  quantity INT DEFAULT 0,
  PRIMARY KEY (product_id, warehouse_id)
);

/* Inventory Logs table (to track stock changes) */
CREATE TABLE inventory_logs (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id),
  warehouse_id INT REFERENCES warehouses(id),
  change_amount INT,
  reason VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

/* Suppliers table */
CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_email VARCHAR(255)
);

/* Product mapping table */
CREATE TABLE product_suppliers (
  product_id INT REFERENCES products(id),
  supplier_id INT REFERENCES suppliers(id),
  PRIMARY KEY (product_id, supplier_id)
);

/* Product Bundles (self-referencing products) */
CREATE TABLE product_bundles (
  bundle_id INT REFERENCES products(id),
  component_id INT REFERENCES products(id),
  quantity INT DEFAULT 1,
  PRIMARY KEY (bundle_id, component_id)
);
