# Introduction

Tools rent reservation page designed for customers, who needs to rent some tools and wants to reserve them before they'll physically come in our rent garage.



# Getting Started
Application based on Python Django technology.
Requirements:
asgiref==3.5.2
Django==4.1.2
Pillow==9.2.0
sqlparse==0.4.3
Project use local database db.sqlite3 file.

There are two groups of users - manager of this page (admin) and customers.
Admin can manage information in this page, add tool copies, edit them, delete, assign them to customers as rented.
Customers can see all tools for rent, their copies, can make or cancel reservations, can check their reserved or borrowed tools.

To test project with both roles:
Manager (username: admin, password: admin).
Customer (username: Customer_1, password: pass12345)
