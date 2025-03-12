from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    return jsonify({"message":"Hello World!"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)