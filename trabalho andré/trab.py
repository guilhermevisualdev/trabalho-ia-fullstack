from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("trab.html")

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.json
    febre = data.get("febre", False)
    tosse = data.get("tosse", False)
    dor_cabeca = data.get("dor_cabeca", False)
    falta_ar = data.get("falta_ar", False)
    corpo = data.get("corpo", False)
    garganta = data.get("garganta", False)

    if febre and tosse and falta_ar:
        return jsonify({"resposta": "⚠️ Possível quadro gripal grave ou COVID-19. Procure atendimento médico imediatamente."})
    elif febre and dor_cabeca and corpo:
        return jsonify({"resposta": "Pode ser virose ou dengue. Mantenha hidratação e procure um posto de saúde para exame."})
    elif garganta and febre:
        return jsonify({"resposta": "Pode ser infecção de garganta. Se persistir, consulte um médico para avaliação."})
    elif tosse and garganta:
        return jsonify({"resposta": "Pode ser resfriado comum. Repouso e hidratação são recomendados."})
    elif febre and tosse:
        return jsonify({"resposta": "Leve resfriado."})
    elif febre and corpo:
        return jsonify({"resposta": "Pode ser dengue. Mantenha hidratação e procure um posto de saúde para exame."})
    elif falta_ar and tosse:
        return jsonify({"resposta": "Pode ser bronquite. Procure um pneumologista."})
    elif falta_ar and garganta:
        return jsonify({"resposta": "Pode ser alergia por conta do clima seco e frio."})
    else:
        return jsonify({"resposta": "✅ Nenhum sintoma crítico detectado. Continue se cuidando e monitorando sua saúde."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
