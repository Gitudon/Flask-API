from flask import Flask,request,jsonify
from phonetic_codes import codes,reads

app=Flask(__name__)

@app.route("/",methods=["GET"])
def get_codes():
    query=request.args.get("code",None,type=str)
    if not query:
        return "Hello! This is Phonetic-Code API!!"
    if query not in codes:
        return jsonify({"message":"Invalid query was received!!"}),400
    return jsonify({"code":codes[query],"read":reads[query]}),200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)
