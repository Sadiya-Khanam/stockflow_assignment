## Issue 1

The code didn’t check if all important fields like name, sku, price, etc. are present in the request.

Impact: If any field is missing, it can break the app or give weird errors.

Fix: I added a check to make sure all required fields are there. If not, it shows a proper error message.

## Issue 2

It didn’t check if the SKU is already used.

Impact: SKU is supposed to be unique. If same SKU is used again, database will throw error or wrong data can go in.

Fix: I added a check to see if the SKU already exists in the database. If it does, we return an error.

## Issue 3

Product was getting saved first, and inventory was saved after that.

Impact: If inventory fails to save, product is already added. So incomplete data goes in the DB.

Fix: I used flush() to get product ID but didn’t commit immediately. After adding both product and inventory, I did one commit().

## Issue 4

There was no error handling.

Impact: If something goes wrong (like database issue), app might crash and user won’t understand what happened.

Fix: I added a try-except block to catch errors. If anything fails, it rolls back the DB and shows an error message.

## Issue 5

Price was stored using float directly.

Impact: Float can cause rounding mistakes with prices.

Fix: I used Decimal() to store price safely without rounding errors.


