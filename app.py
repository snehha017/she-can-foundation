from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def index():
    return render_template("signup.html", show='login')

@app.route("/api/intern")
def intern_data():
    return jsonify({
        "name" : "Sneha Lande",
        "referralCode" : "snehalande2025",
        "donations" : 5000
    })

@app.route('/login', methods=['POST'])
def login():
    return render_template("dashboard.html")

@app.route('/signup', methods=['POST'])
def signup():
    return redirect(url_for('index', show='login', success='Registered Successfully!'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login')
def logout():
    return render_template("signup.html") 

if __name__ == "__main__":
    app.run(debug=True)
