from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def helloworld():
    try:
        # Test rapide de la connexion MongoDB
        dbmongo.cx.admin.command('ping')
        return "Hello World! Connexion MongoDB réussie !"
    except Exception as e:
        return f"Erreur de connexion à MongoDB : {e}"

#connect and create a db named as mydb
app.config["MONGO_URI"] = "mongodb://db:27017/mydb"
           
#initializing the client for mongodb
dbmongo = PyMongo(app)

#creating the user collection(
user_collection = dbmongo.db.users

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
