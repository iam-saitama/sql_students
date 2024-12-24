#  Создайте базу данных SQLite3 с именем "mydatabase.db".
# - Создайте таблицу "students" со следующими столбцами:
# - id (целое число, первичный ключ)
# - name (текстовое значение)
# - age (целое число)
# - grade (текстовое значение)
# - Вставьте несколько записей в таблицу "students" с информацией о различных студентах (несколько имен, возрастов и оценок).

import sqlite3

connection = sqlite3.connect('mydatabase.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (user_id INTEGER AUTO_INCREMENT PRIMARY KEY, name TEXT, age INTEGER, grade TEXT);')
sql.execute('INSERT OR REPLACE INTO students VALUES (1, "Pavel", 20, "4");')
sql.execute('INSERT OR REPLACE INTO students VALUES (2, "Misha", 19, "5");')
sql.execute('INSERT OR REPLACE INTO students VALUES (3, "Anna", 21, "3");')
sql.execute('INSERT OR REPLACE INTO students VALUES (4, "Maria", 20, "5");')
sql.execute('INSERT OR REPLACE INTO students VALUES (5, "Kirill", 18, "4");')
connection.commit()

def get_all_st():
    return sql.execute('SELECT * FROM students;').fetchall()


# Напишите функцию "get_student_by_name", которая принимает имя студента в качестве аргумента
# и возвращает информацию о студенте (имя, возраст, оценку) из таблицы "students".

def get_student_by_name(name):
    sql.execute('SELECT * FROM students WHERE name=?;', (name,))
    info = sql.fetchone()
    if info:
        return f'Имя: {info[1]}, Возраст: {info[2]}, Оценка: {info[3]}'
    else:
        print('Студент не найден!')


#- Напишите функцию "update_student_grade", которая принимает имя студента и новую оценку в качестве аргументов
# и обновляет запись в таблице "students" с соответствующим именем, устанавливая новую оценку.

def update_student_grade(name, new_grade):
    sql.execute('UPDATE students SET grade=? WHERE name=?;', (name, new_grade))
    connection.commit()
    print('Оценка обновлена!')


#- Напишите функцию "delete_student", которая принимает имя студента в качестве аргумента
# и удаляет запись о студенте из таблицы "students".

def delete_student(name):
    sql.execute('DELETE FROM students WHERE name=?;', (name,))
    connection.commit()
    print('Студент удален!')


# Пример использования

print(get_student_by_name('Pavel'))
print(update_student_grade('Anna', '4'))
print(delete_student('Maria'))
print(get_all_st())