from flask import Flask,render_template

#app=Flask(__name__,template_folder='template') if default folder is not used then.... updated in git

####one change done in desktop and push to git

app=Flask(__name__)

var1=[
    {
    'name':'Avinash',
    'job' : 'DBA'
    },
    {
        'name':'Priya',
        'job':'Housewife'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=var1)

@app.route("/about/")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
