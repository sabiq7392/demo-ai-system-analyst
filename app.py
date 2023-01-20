from flask import Flask, request, abort
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


TYPE_AI = ["SECURITY_ANALYST", "SURVEY"]
LANGUAGE = ["INDONESIAN", "ENGLISH"]

@app.route("/", methods=["GET", "POST"])
def index():
  if (request.method == "GET"):
    return "Hello World"
  
  if (request.method == "POST"):
    # if (request.form["type_ai"] not in TYPE_AI):
    #   return abort(400, "type_ai value is wrong")
    
    # if (request.form["language"] not in LANGUAGE):
    #   return abort(400, "language value is wrong")
    
    # if (not isinstance(request.form["text"], str)):
    #   return abort(400, "text value is wrong")
    
    data = {
      "type_ai": request.form["type_ai"],
      "language": request.form["language"],
      "text": request.form["text"]
    }
    
    return data["text"][::-1]


if __name__ == "__main__":
  app.run(debug=True)
