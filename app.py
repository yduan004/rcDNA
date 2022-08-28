from flask import Flask, render_template, request, redirect, url_for, flash
from src.verify import validated
from src.rc import reverseComplement
import os

app = Flask(__name__)
app.config["ALLOWED_FILE_EXTENSIONS"] = ['TXT', 'FASTQ']
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.secret_key = 'super secret key'
    

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].upper() in app.config["ALLOWED_FILE_EXTENSIONS"]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['dnaseq']:
            dnaseq = request.form['dnaseq']
            seqs = validated(dnaseq, '\r\n')
            holder = ';'.join(dnaseq.split('\r\n'))
        else:
            f = request.files['seqfile']
            if f.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if not allowed_file(f.filename):
                flash('The file extesion can only be "txt" or "fastq"')
                return redirect(request.url)
            dnaseq = f.read().decode('utf-8')
            seqs = validated(dnaseq, '\n')
            holder = 'ATGCGAA'
        rcseqs = reverseComplement(seqs)
        return render_template('index.html', seqs=rcseqs, holder=holder)
    else:
        return render_template('index.html', seqs=None, holder='ATGCGAA')

if __name__ == "__main__":
    app.run(port=1234)
