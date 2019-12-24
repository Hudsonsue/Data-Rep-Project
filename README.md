# Data-Rep-Project
G00219132 GMIT Data Analytics 

Restaurant website.
Flask Appserver - menusserver.py (note two s!)


Home page (home.html, includes pic slideshow, scrolling text and styling of web buttons etc. Also has links to orders (where customers can order) and a staff login page

Orders page (order.html) with link back to home page. Customer orders saved in orders table, can add, update, delete order items. 

Staff login page stafflogin.html – has a login to validate with pre existing details in the accounts table.

Menu page menu.html - links to menu table and can add, update, delete menu items. 

Database scripts are on file database and tables.sql. Database called datarepresentation with three tables, menu. OrderDAO, MenuDAO and logonDAO were all connected using mysqlworkbench/pymysql connector and login details 
        host="localhost",
        user="root",
        password="root",
        database="datarepresentation"
unfortunately I was unable to get all tables working on python anywhere.

