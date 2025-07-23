## Problems in code:

. It didn’t check if required fields like name,sku, etc are missing

. There was no check if SKU is already used (SKU should be unique)

. It saved the product first, then inventory — if inventory fails, product still gets saved

. No error handling — if database error happens, app might crash

. Price was not handled using Decimal, which can cause rounding issues

## What I changed:

. Added a check for all required fields

. Checked if the SKU already exists in the database

. Used Decimal() to safely store price values

. Added both product and inventory, then used one final commit()

. Wrapped DB operations in a try-except block to handle errors and do rollback() if needed

## Why I did these changes:

. To avoid saving partial data in case of failure

. To make the API safe and handle wrong input better

. So that user gets proper error messages instead of app crash

