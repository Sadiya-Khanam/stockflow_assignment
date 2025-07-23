#  StockFlow Assignment

This is a take-home assignment for a B2B SaaS inventory system called StockFlow.

The project is divided into 3 parts:

##  Part 1: Code Review & Debugging

In this part, I reviewed a buggy Flask API that adds new products.  I fixed the issues like: 

.  Missing field checks

.  Unique SKU check

. Decimal price handling

. Inventory logic

##  Part 2: Database Design

Here I designed the database schema using SQL.

.  Companies have warehouses 

.  Products can be in multiple warehouses  

.  Inventory updates are tracked  

.  Products can be bundles  

.  Products come from suppliers

##  Part 3: Low Stock API

I built a GET API to show low-stock alerts for a company.

.  Only alerts for products with recent sales (last 30 days)

.  Alerts only when stock is below threshold

.  Shows supplier info

.  Handles multiple warehouses

