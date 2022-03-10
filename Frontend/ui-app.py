'''
Created on 
Course work: 
@author: 
Source:
    
'''
# Import necessary modules


from flask import Flask, redirect, request, url_for, render_template


app = Flask(__name__)

#constants



@app.route("/",methods=["POST", "GET"])
def start():
    
    if request.method == "POST":
        return redirect(url_for("round_1"))
    return render_template("frontpage.html")


# @app.route('/round1',methods=["GET","POST"])
# def startpy():


#     utils = ch_client.process_get('/round1')

#     return render_template('index.html', utils = utils)



@app.route('/round1',methods=["GET","POST"])
def round_1():
    if request.method == "POST":
        yes = 0
        for i in range(11):
            if(request.form["choice-radio%d"%(i)] == "yes"):
                yes += 1
        if(yes>5):
            return redirect(url_for("round_2"))
    return render_template('index.html')

@app.route('/round2', methods=["GET","POST"])
def round_2():
    

    return render_template("round2.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)