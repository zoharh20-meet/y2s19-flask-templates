from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favfood = ["Choclate", "Avocado", "Sushi"]
    return render_template(
	"index.html",
	food="Avocado"
	favfood= favfood)





if __name__ == '__main__':
   app.run(debug = True)
