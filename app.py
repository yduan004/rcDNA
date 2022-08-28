from flask import Flask, render_template, request, redirect, url_for
from src.verify import validated
from src.rc import reverseComplement

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        dnaseq = request.form['dnaseq']
        seqs = validated(dnaseq)
        rcseqs = reverseComplement(seqs) 
        holder = ';'.join(dnaseq.split('\r\n'))
        return render_template('index.html', seqs=rcseqs, holder=holder)
    else:
        return render_template('index.html', seqs=None, holder='ATGCGAA')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, debug=True)
