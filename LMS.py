from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

class LibraryManagementSystem:
    def __init__(self):
        self.users = {"admin": "admin123"}
        self.members = {}
        self.books = {}
        self.issued_books = {}
        self.fines = {}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return {"message": "Login successful", "user": username}
        return {"error": "Invalid credentials"}

    def add_user(self, username, password, role="user"):
        if username not in self.users:
            self.users[username] = password
            self.members[username] = {"role": role, "issued_books": []}
            return {"message": f"User '{username}' added successfully."}
        return {"error": "User already exists."}

    def add_book(self, book_id, title, author, copies):
        self.books[book_id] = {"title": title, "author": author, "copies": copies}
        return {"message": f"Book '{title}' added successfully."}

    def issue_book(self, book_id, user):
        if user not in self.members:
            return {"error": "User not registered."}
        if book_id in self.books and self.books[book_id]['copies'] > 0:
            self.books[book_id]['copies'] -= 1
            self.members[user]['issued_books'].append(book_id)
            self.issued_books[user] = book_id
            return {"message": f"Book '{self.books[book_id]['title']}' issued to {user}."}
        return {"error": "Book not available."}

    def return_book(self, user):
        if user in self.issued_books:
            book_id = self.issued_books.pop(user)
            self.books[book_id]['copies'] += 1
            self.members[user]['issued_books'].remove(book_id)
            return {"message": f"Book '{self.books[book_id]['title']}' returned successfully."}
        return {"error": "No book to return."}

    def search_book(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book['title'].lower()]
        return {"books": results} if results else {"message": "No books found."}

    def generate_report(self):
        return {
            "Total Books": len(self.books),
            "Issued Books": len(self.issued_books),
            "Registered Users": len(self.members),
            "Pending Fines": sum(self.fines.values())
        }

library = LibraryManagementSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    return jsonify(library.login(data['username'], data['password']))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.form
    return jsonify(library.add_user(data['username'], data['password']))

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.form
    return jsonify(library.add_book(data['book_id'], data['title'], data['author'], data['copies']))

@app.route('/issue_book', methods=['POST'])
def issue_book():
    data = request.form
    return jsonify(library.issue_book(data['book_id'], data['user']))

@app.route('/return_book', methods=['POST'])
def return_book():
    data = request.form
    return jsonify(library.return_book(data['user']))

@app.route('/search_book', methods=['GET'])
def search_book():
    keyword = request.args.get('keyword', '')
    return jsonify(library.search_book(keyword))

@app.route('/generate_report', methods=['GET'])
def generate_report():
    return jsonify(library.generate_report())

if __name__ == '__main__':
    app.run(debug=True)
