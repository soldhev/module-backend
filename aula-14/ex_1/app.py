from flaks import flask, render_template, request, send_file
from funcionario import Funcionario
from reportlab.platypus import SimpleDocTemplate,paragraph, Spacer
from reportlab.lib.styles import getSampleletStyleSheet
from reportlab.lib.pagesizes import A4

app = flask (__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.methods =="POST":
        nome = request.form.get("nome")
        valorhora = request.form.get("valorhora")
        horas = request.form.get("horas")
        va = request.form.get("va")
        vt = request.form.get("vt")
        
        funcionario = Funcionario(
            nome,
            valorhora,
            horas,
            va,
            vt
        )
        # GERA O PDF automaticamente
        gerar_pdf(funcionario)
        
        return render_template("resultado.html", f=funcionario)
    return render_template("index.html")