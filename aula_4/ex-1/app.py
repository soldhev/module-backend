from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # system for cauculator notes
    # creating a function for cauculate media
    global media
    # define a function que recebe for notes
    def soma (n1, n2, n3, n4):
      global media 
      media = (n1+n2+n3+n4) / 4
    
    soma(9, 6, 5, 3)
    
    media_normal = media
    
    media_formatada = f"{media:2f}"
    
    return render_template(
          "index.html",
          media_normal = media_normal,
          media_formatada = media_formatada
    )
if __name__=="__main__":
    app.run(debug=True)    