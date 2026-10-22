import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(10) NOT NULL,
    genre VARCHAR(10) NOT NULL,
    users_id INTEGER NOT NULL,
    FOREIGN KEY (users_id) REFERENCES users
    )
''')
connect.commit()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    rating INTEGER CHECK (rating >= 1 AND rating <= 10)
) 
''')
connect.commit()
cursor.execute('''
INSERT INTO users (name) VALUES
('Алексей'),
('Мария'),
('Иван'),
('Елена'),
('Дмитрий')
''')
connect.commit()
cursor.execute('''
INSERT INTO movies (title, genre) VALUES
('Интерстеллар', 'Научная фантастика'),
('Начало', 'Фантастика'),
('Темный рыцарь', 'Боевик'),
('Зеленая миля', 'Драма'),
('Клаустрофобы', 'Триллер')
''')
connect.commit()
cursor.execute('''
INSERT INTO reviews (user_id, movie_id, rating) VALUES
(1, 1, 10), 
(1, 2, 9),  
(2, 1, 9),  
(2, 3, 10), 
(3, 2, 8), 
(3, 4, 10), 
(4, 1, 8),  
(4, 3, 7),  
(4, 4, 9),  
(5, 2, 5),  
(5, 4, 9)  
''')
connect.commit()
cursor.execute('''SELECT 
    u.name AS user_name, 
    m.title AS movie_title, 
    r.rating
FROM reviews r
JOIN users u ON r.user_id = u.id
JOIN movies m ON r.movie_id = m.id
''')
connect.commit()
cursor.execute('''SELECT 
    ROUND(AVG(rating), 2) AS average_rating,
    MAX(rating) AS max_rating,
    MIN(rating) AS min_rating
FROM reviews
''')
connect.commit()
