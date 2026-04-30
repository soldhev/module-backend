from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # working with array
    # creating a dicionary dados
frutas1 = {
    1: "Laranja",
    2: "Maça",
    3: "Uva"
}

frutas2 =["Laranja", "Maça", "Uva"] 

frutas3 = {
    0: "Laranja",
    1: "Maça",
    7: "Uva"
}
frutas3[8]= "Abacaxi"

frutas4 =["Abacaxi", "Melao", "Banana"]

frases = []

#loop for array
for fruta in frutas4:
    frases.append(f"Voce gosta de {fruta}")
    
    
    
    return render_template(
    "index.html",
    frutas1=frutas1
    frutas2=frutas2
    frutas3=frutas3
    frases=frases
    
)    
  
if __name__ =="__main__":
    app.run(debug=True)
