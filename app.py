from flask import Flask, render_template, request, redirect
from src.verify import validated
from src.rc import reverseComplement

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        dnaseq = request.form['dnaseq']
        seqs = validated(dnaseq)
        rcseqs = reverseComplement(seqs) 
        return render_template('index.html', seqs=rcseqs)
    else:
        return render_template('index.html', seqs=None)

if __name__ == "__main__":
    app.run(debug=True)