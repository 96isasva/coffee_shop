import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute('drop table if exists {0}'.format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def  insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql ="insert into Product (Name, Price) values (?,?) "
        cursor.execute(sql,values)
        db.commit()

def delete_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where name=?"
        cursor.execute(sql,data)
        db.commit()

def update_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql.data)
        db.commit()

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute(*select * from Product*)
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Name,Price from Product where ProductID=?",(id,))
        product cursor.fetchnone()
        return product

print("Product Table Menu")
print("1. (Re)Create Product Table")
print("2. Add new product")
print("3. Edit existing product")
print("4. Delete existing product")
print("5. Search for products")
print("6. Exit")
choice = input(int("Please select An option: "))

if choice == 1:
    db_name = "coffee_shop.db"
    sql = """create table Product
             (ProductID integer,
             Name text,
             Price real,
             primary key(ProductID))"""
    create_table(db_name,"Product",sql)

if choice == 2:
    product = (name,price)
    name = input(str("välj namn: "))
    price = input(int("välj pris: "))
    insert_data(product)

if choice == 3:
    data = (new_name,new_price,index)
    new_name = input(str("välj nytt namn: "))
    new_price = input(int("välj nytt pris: "))
    index = input(int("välj index: "))
    update_product(data)

if choice == 4:
    data = (name,)
    name = input(int(str("Välj namn")))
    delete_product(data)
if choice == 5:
