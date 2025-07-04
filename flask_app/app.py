from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to check if the password meets the minimum length requirement
def is_valid_password(password):
    return len(password) >= 8  # Only length check

# Function to check if password is in the common passwords list
def is_common_password(password):
    try:
        with open("xato-net-10-million-passwords-1000.txt", "r") as f:
            common_passwords = f.read().splitlines()
            if password in common_passwords:
                return True
    except FileNotFoundError:
        return False
    return False

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    
    if request.method == 'POST':
        password = request.form.get('password')

        # Check if password meets the minimum length requirement
        if not is_valid_password(password):
            message = "Password must be at least 8 characters long."
        
        # Check if password is in common passwords list
        elif is_common_password(password):
            message = "This password is too common. Please choose a different one."
        
        # If password is valid, redirect to welcome page with the password
        else:
            return redirect(url_for('welcome', password=password))

    return render_template('index.html', message=message)

# Welcome route (after successful password validation)
@app.route('/welcome')
def welcome():
    password = request.args.get('password')  # Get the password passed as a query parameter
    return render_template('welcome.html', password=password)

# Logout route
@app.route('/logout')
def logout():
    return redirect(url_for('home'))  # Redirect to the homepage

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
