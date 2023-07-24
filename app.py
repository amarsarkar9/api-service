from flask import render_template, request, jsonify, Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
    return "welcome"
    # return render_template("/index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

# import pymongo

# client = pymongo.MongoClient("mongodb+srv://amarsarkar:qwertyuiop@cluster0.f0ztixh.mongodb.net/test")
# database=client["amar"]
# col=database["sample"]
# doc=col.insert_one({"name":"amar", "_id":"1"})
# col.delete_one({"name":"amar"})
# database.drop_collection(col)
