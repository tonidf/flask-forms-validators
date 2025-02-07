from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from forms import Persona, PersonaMacro


app = Flask(__name__)

@app.route('/')
def index():
    return 'Esto funciona'

@app.route('/formulario-simple', methods=['GET','POST'])
def formulario_simple():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        telefono = request.form.get('telefono')
        email = request.form.get('email')

        print(username, password, email, telefono)

        return 'Datos procesados correctamente'
    else:
        return render_template('formulario-simple.html')
    

@app.route('/formulario-simple-objeto', methods=['GET','POST'])
def formulario_simple_objeto():
    form = Persona()

    if form.validate() and request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        telefono = request.form.get('telefono')
        email = request.form.get('email')

        print(username, password, email, telefono)

        return 'datos procesados'
    
    else:
        return render_template('formulario-simple-objeto.html', form=form)
    
@app.route('/formulario-simple-objeto-macro', methods=['GET','POST'])
def formulario_simple_objeto_macro():
    form = PersonaMacro()

    if form.validate() and request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        telefono = request.form.get('telefono')
        email = request.form.get('email')

        print(username, password, email, telefono)

        return 'datos procesados'
    
    else:
        return render_template('formulario-simple-objeto-macro.html', form=form)


def status_404(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == '__main__':

    app.config.from_object(config['development'])
    app.run()

