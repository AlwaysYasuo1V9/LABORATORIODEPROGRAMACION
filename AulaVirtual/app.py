from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    materias = ['Matemáticas', 'Historia', 'Biología']  # Ejemplo de datos
    return render_template('index.html', title="Aula Virtual", materias=materias)

if __name__ == '__main__':
    app.run(debug=True)
