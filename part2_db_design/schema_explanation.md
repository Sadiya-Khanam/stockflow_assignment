##  Database Design Explanation

. companies - to store company info

. warehouses - each warehouse belongs to a company

. products - has details like name, SKU, price, and type (single/bundle)

. inventory - shows quantity of a product in a warehouse

. inventory_logs - tracks inventory changes with reason and date

. suppliers - stores supplier info like name and email

. product_suppliers - links products and their suppliers (many-to-many)

. product_bundles - allows one product to be made of other products (for combos or kits)

## Missing Questions 

. Can one product have multiple suppliers or just one?

. When a bundle is sold, should all component stocks reduce automatically?

. Do we want to allow negative stock or stop it?

. Should we store who changed inventory (like admin/user ID)?

. Do we need to track sales inside this system or not?

## Design Choices 

. Used foreign keys to keep relationships between tables clear

. Composite primary key in inventory table (product + warehouse combo)

. Added unique constraint on SKU (since it must be unique)

. Made product type field to handle both simple and bundled products

. Used inventory_logs for tracking changes (audit/history helpful)

. The product_bundles table connects one product with other products.It helps us make combo packs using normal items.

. Kept all names short and meaningful for easier reading