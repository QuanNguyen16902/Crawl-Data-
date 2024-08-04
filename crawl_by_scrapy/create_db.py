import sqlite3
import json
# Tạo cơ sở dữ liệu SQLite và bảng
conn = sqlite3.connect('vnexpress.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        image_url TEXT,
        link TEXT
    )
''')
# Đọc dữ liệu từ file JSON vừa tạo
with open('output.json', encoding='utf-8') as file:
    data = json.load(file)

# Lưu dữ liệu vào cơ sở dữ liệu
for item in data:
    cursor.execute('''
        INSERT INTO articles (title, description, image_url, link) VALUES (?, ?, ?, ?)
    ''', (item['title'], item['description'], item['image_url'], item['link']))

conn.commit()
conn.close()
