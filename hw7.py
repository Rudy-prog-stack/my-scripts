import sqlite3

DB_NAME = "store.db"


def init_db():
    """Создает базу данных и таблицу products, если они еще не существуют."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()

def create_product(name: str, price: float, quantity: int):
    """Добавляет новый товар в базу данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity),
    )

    conn.commit()
    conn.close()
    print(f"✅ Товар '{name}' успешно добавлен!")

def read_products():
    """Выводит все товары из базы данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price, quantity FROM products")
    products = cursor.fetchall()

    conn.close()

    if not products:
        print("📁 База данных пуста.")
        return

    print("\n📦 Список товаров в базе данных:")
    print("-" * 50)
    for prod in products:
        print(
            f"ID: {prod[0]} | Название: {prod[1]} | Цена: {prod[2]} руб. | Количество: {prod[3]} шт."
        )
    print("-" * 50)

def update_product(product_id: int, new_price: float):
    """Обновляет цену товара по его id."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if product:
        cursor.execute(
            "UPDATE products SET price = ? WHERE id = ?", (new_price, product_id)
        )
        conn.commit()
        print(
            f"🔄 Цена товара '{product[0]}' (ID: {product_id}) изменена на {new_price} руб."
        )
    else:
        print(f"❌ Товар с ID {product_id} не найден.")

    conn.close()

def delete_product(product_id: int):
    """Удаляет товар по его id."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if product:
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        print(f"🗑️ Товар '{product[0]}' (ID: {product_id}) успешно удален.")
    else:
        print(f"❌ Товар с ID {product_id} не найден.")

    conn.close()

if __name__ == "__main__":
    init_db()

    create_product("Ноутбук", 75000.0, 5)
    create_product("Мышь беспроводная", 1500.0, 20)
    create_product("Клавиатура", 3200.0, 15)

    read_products()

    update_product(1, 72990.0)

    read_products()

    delete_product(2)

    read_products()