from flask import Flask, render_template, request, redirect, url_for, flash,
import csv, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jps', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_books():
    books = []
    with open('books.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books

def save_book(book):
    file_exists = os.path.isfile('books.csv')
    with open('books.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'genres', 'authors', 'type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            wrtier.writeheader()
        writer.writerow(book)

def delete_book(filename):
    books = get_books()
    books = [book for book in books if book['filename'] != filename]
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'genres', 'authors', 'type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
    try:
        os.remove(os.path.join(app,config['UPLOAD_FOLDER'], filename))
    except FileNotFoundError:
        pass



if __name__ == '__main__':
    app.run(debug=True)