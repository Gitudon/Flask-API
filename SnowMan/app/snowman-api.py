from flask import Flask,request,jsonify
import json

app=Flask(__name__)
app.json.ensure_ascii = False

@app.route("/",methods=["GET"])
def main():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SnowMan API</title>
    </head>
    <body>
        <h1>Hello! This is SnowMan API!!</h1>
        <p>There are three endpoints available:</p>
        <ul>
            <li><code>/nickname</code></li>
            <li><code>/color</code></li>
            <li><code>/birthday</code></li>
        </ul>
        <p>You can use these endpoints to get information about SnowMan.</p>
        <p><strong>Example:</strong></p>
        <p><code>[hostname]:5002/[endpoint]?name=[name]</code></p>
        <p>The name must be a full-name of kanji with no space between the first name and the last name.</p>
        <p>Also, you can use the following endpoint to get all of the information:</p>
        <p><strong>Example:</strong></p>
        <p><code>[hostname]:5002/all</code></p>
        <p><code>[hostname]:5002/all?name=[name]</code></p>
    </body>
    </html>
    """

@app.route("/nickname",methods=["GET"])
def get_nickname():
    query=request.args.get("name",None,type=str)
    if not query:
        return "Please provide a name to get the nickname."
    with open("database.json","r",encoding="utf-8") as f:
        data=json.load(f)
        if query not in data:
            return "The name you provided is not in the database."
        nickname=data[query]["nickname"]
        return jsonify({query: {"nickname": nickname}})

@app.route("/birthday",methods=["GET"])
def get_birthday():
    query=request.args.get("name",None,type=str)
    if not query:
        return "Please provide a name to get the birthday."
    with open("database.json","r",encoding="utf-8") as f:
        data=json.load(f)
        if query not in data:
            return "The name you provided is not in the database."
        birthday=data[query]["birthday"]
        return jsonify({query: {"birthday": birthday}})

@app.route("/color",methods=["GET"])
def get_color():
    query=request.args.get("name",None,type=str)
    if not query:
        return "Please provide a name to get the color."
    with open("database.json","r",encoding="utf-8") as f:
        data=json.load(f)
        if query not in data:
            return "The name you provided is not in the database."
        color=data[query]["color"]
        return jsonify({query: {"color": color}})

@app.route("/all",methods=["GET"])
def get_all():
    query=request.args.get("name",None,type=str)
    with open("database.json","r",encoding="utf-8") as f:
        data=json.load(f)
        if not query:
            return jsonify(data)
        if query not in data:
            return "The name you provided is not in the database."
        return jsonify({query: data[query]})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5002)