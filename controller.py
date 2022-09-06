from flask import Flask, render_template, request
from model import addComment, addContact

app = Flask(__name__)
app.secret_key = "Profile"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/interest')
def interest():
    return render_template('interest.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/contact', methods = ['GET','POST'])
def contact():
    queryNama = ""
    queryNomor = ""
    queryEmail = ""
    queryPesan = ""
    addedContact = ""
    if request.method == "POST" :
        queryNama = request.form['nama']
        queryNomor = request.form['telpon']
        queryEmail = request.form['email']
        queryPesan = request.form['pesan']
        addedContact = addContact(queryNama, queryNomor, queryEmail, queryPesan)

    return render_template ('contact.html' ,result = addedContact)

@app.route('/gallery')
def gallery() :
    return render_template("gallery.html")

if __name__ == '__main__' :
    app.run(debug = True)