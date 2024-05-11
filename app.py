from flask import Flask, render_template, request

## __ are for magic words reserved for special variables with meaning
# __name__ is to tell the program who is accessing
app = Flask(__name__)

# Get from frontend, post to frontend
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    # frontend q, backend r (wrong naming convention)s
    # Refer to pypi chapter 8 for the right convention
    r = request.form.get("q")
    return(render_template("main.html",r=r))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))
    
@app.route("/dbs_price",methods=["GET","POST"])
def dbs_price():
    q = float(request.form.get("q")) # convert to float, use 
    return(render_template("dbs_price.html", r=(q*-50.601)+90.2))
    
if __name__ == "__main__":
    app.run()
