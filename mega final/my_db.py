import sqlite3

db_name = 'db.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()

    do('''
        CREATE TABLE menu (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        description VARCHAR,
        imgUrl VARCHAR,
        cost VARCHAR
       )''')
    
    do('''
        CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username VARCHAR,
        email VARCHAR,
        password VARCHAR,
        role VARCHAR,
        basket VARCHAR       
       )''')
    
    close()

# create()
def add_menu(title, description,cost, imgUrl):
    open()
    cursor.execute('''INSERT INTO menu (title, description,cost, imgUrl) VALUES (?,?,?,?)''', [title, description,cost,imgUrl])
    conn.commit()
    close()

def add_users(username,email,password,role,basket):
    open()
    cursor.execute('''INSERT INTO users (username,email,password,role,basket) VALUES (?,?,?,?,?)''', [username,email,password,role,basket])
    conn.commit()
    close()

def show(table):
    open()
    cursor.execute(f'SELECT * FROM {table}')
    print(cursor.fetchall())
    close()

def get_all_menu():
    open()
    cursor.execute(f'SELECT * FROM menu')
    return cursor.fetchall()

def get_menu_by_id(id):
    open()
    cursor.execute(f'SELECT * FROM menu WHERE menu.id == ?', [id])
    return cursor.fetchall()

def drop_table(table):
    open()
    do(f'DROP TABLE IF EXISTS {table}')

def delete_menu_by_id(id):
    open()
    cursor.execute('''DELETE FROM menu WHERE id == (?)''', (id,))
    conn.commit()
    close()

def fill_db():
    data = [
        {
            "id": '1',
            'title': 'Квадрік',
            'description': "соус бешамель, сир моцарела, сир дорблю, груша, волоський горіх, пармезан",
            'cost': "345 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/kvafrik2.webp"
        },
        {
            "id": '2',
            'title': 'Анджеліо',
            'description': "соус кисло-солодкий, сир моцарела, курка, баварські ковбаски, корнішон, цибуля   ",
            'cost': "305 грн",
            'image': "https://la.ua/wp-content/uploads/2022/04/dzhavelinajavelina-1.webp"
        },
        {
            "id": '3',
            'title': 'Піца La Logik',
            'description': "соус томатний, сир моцарела, шинка, баварські ковбаски, ковбаса салямі, прошуто  ",
            'cost': "295 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/la-pyecz.webp"
        },
        {
            "id": '4',
            'title': 'Цезаро',
            'description': "соус бешамель, сир моцарела, хрусткий салат, куряче м'ясо, перепелині яйця, помідори, соус Цезар (містить часник), пармезан",
            'cost': "395 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/czezario.webp"
        },
        {
            "id": '5',
            'title': 'Салямі',
            'description': "соус томатний, сир моцарела, ковбаса салямі",
            'cost': "255 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/salami.webp"
        },
        {
            "id": '6',
            'title': 'Гавайська',
            'description': "соус бешамель, сир моцарела, філе куряче, кукурудза, ананас, пармезан",
            'cost': "265 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/gavajska.webp"
        },
        {
            "id": '7',
            'title': 'Пепероні',
            'description': "соус кисло-солодкий, сир моцарела, пепероні, пармезан, рукола",
            'cost': "265 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/peperoni.webp"
        }, {
            "id": '8',
            'title': 'Демонінйо',
            'description': "соус томатний, сир моцарела, перець чилі, пепероні",
            'cost': "240 грн",
            'image': "https://la.ua/wp-content/uploads/2021/08/diabola.webp"
        },
    
    ]

    for i in data:
        add_menu(i["title"],i["description"],i["cost"],i["image"]) 

#delete_menu_by_id(4)
drop_table("menu")
#create()
#add_users("121221","2144","1488")
#add_menu("121221","2144","1122","https://la.ua/wp-content/uploads/2021/08/kvafrik2.webp")
#show('users')
#show('menu')
drop_table("users")
create()
fill_db()