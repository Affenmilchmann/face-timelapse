from flask import (
    render_template,
    request,
    flash,
    redirect
)
from werkzeug.utils import secure_filename
from pathlib import Path

from app import app
from src.render_queue import RenderItem

ALLOWED_EXTENSIONS = {'zip'}
def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render', methods=['GET', 'POST'])
def render():
    if request.method == 'GET':
        return render_template('render.html')
    elif request.method == 'POST':
        if 'file' not in request.files:
            flash("No file given", category='error')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No file given", category='error')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash(f"Only {ALLOWED_EXTENSIONS} files supported", category='error')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            filename = Path(app.config['UPLOAD_DIR']).joinpath(filename)
            file.save(filename)
            return filename

@app.route('/howtouse')
def howtouse():
    return render_template('base.html')