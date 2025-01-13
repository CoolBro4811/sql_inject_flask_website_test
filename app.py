from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

DATABASE = 'vulnerable.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # col by name
    return conn

@app.route('/')
def index():
    return render_template_string('''
    <html>
        <body>
            <h1>Welcome to My Super Secure Login Page!</h1>
            <p>Alright, here's the deal! I have a super top-secret password. It's so secret that even I have to write it down! 🤫</p>
            <p>My password is a whopping <strong>1000 characters long</strong> and it is impenetrable. You will <em>NEVER</em> guess it! 😎💻</p>
            <p>If you think you're clever enough to crack it, prove it below! Enter your <strong>Username</strong> and <strong>Password</strong> to try and access the super-secure area.</p>
            <form action="/login" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" placeholder="Type your username here..."><br><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" placeholder="Enter your secret password..."><br><br>
                <input type="submit" value="Submit">
            </form>
            <p>Good luck, you'll need it!</p>
        </body>
    </html>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # vulnerable SQL query
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    
    ## TO FIX SQL INJECTION - simply run this instead lol
    # cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"Logged in as {user['username']}"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)

