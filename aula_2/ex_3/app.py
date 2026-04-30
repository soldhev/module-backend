from flask import Flask
app = Flask(__name__)
@app.route("/")
dev home():


n1 = 10
n2 = 20
total = n1 + n2

total_formatado = f"{total.2f}"

return render_template(
    "index.html",
    n1=n1,
    n2=n2,
    total=total,
    total_formatado=total_formatado
    )if __name__  == "__main__":
                      app.run(debub=True)
