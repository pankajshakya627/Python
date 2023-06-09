from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'POST':
        new_book = {
            "id": len(books) + 1,
            "title": request.form['title'],
            "author": request.form['author']
        }
        books.append(new_book)
        return redirect(url_for('index'))  # Redirect to homepage after adding a book
    else:
        return render_template('index.html', books=books)

@app.route('/books/<int:book_id>', methods=['POST', 'GET'])
def delete_book(book_id):
    if request.method == 'POST':
        for book in books:
            if book['id'] == book_id:
                books.remove(book)
                return redirect(url_for('index'))  # Redirect to homepage after deleting a book
        return jsonify({"message": "Book not found"}), 404
    else:
        return jsonify({"message": "Invalid request"}), 400


@app.route('/books/<int:book_id>', methods=['POST', 'GET'])
def book_details(book_id):
    if request.method == 'POST':
        for book in books:
            if book['id'] == book_id:
                book['title'] = request.form['title']
                book['author'] = request.form['author']
                return redirect(url_for('index'))  # Redirect to homepage after updating a book
        return jsonify({"message": "Book not found"}), 404
    else:
        for book in books:
            if book['id'] == book_id:
                return render_template('edit_book.html', book=book)
        return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    if request.method == 'POST':
        new_title = request.form['title']
        new_author = request.form['author']
        for book in books:
            if book['id'] == book_id:
                book['title'] = new_title
                book['author'] = new_author
                return redirect(url_for('index'))  # Redirect to homepage after updating a book
        return jsonify({"message": "Book not found"}), 404
    else:
        for book in books:
            if book['id'] == book_id:
                return render_template('edit_book.html', book=book)
        return jsonify({"message": "Book not found"}), 404



@app.route('/')
def index():
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
