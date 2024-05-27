from flask import Flask, render_template,  request
import ast , sys
sys.path.append("C:/Users/MISA/Desktop/Workspace/S6/Python/Codage")
import Programmes.SardinasPaterson.SardinasPaterson as sardina
import Machinelearning.Language as Language
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def prediction():
    style ={True:'color:lime;',False:'color:#ff3d3d'}
    label={True:"C'est un code",False:"Ce n'est pas un code"}
    topredictVar= request.form.get("prediction")
    print(topredictVar)
    topredictVal = ast.literal_eval(topredictVar)
    predicted = Language.Language(None,topredictVal).predict()[0] == 1
    sardinaPrediction = sardina.SardinasPaterson.estCeUnCode(topredictVal)
    return render_template('index.html',
                           prediction = predicted , predictionstyle =style.get(predicted),
                           sardinaresp =sardinaPrediction, 
                           sardinarespstyle =style.get(sardinaPrediction),
                           labelStyle=label,
                           labelStylesardinaresp=label.get(sardinaPrediction),
                           labelStyleprediction =label.get(predicted))

if __name__ == '__main__':
    app.run(debug=True)
