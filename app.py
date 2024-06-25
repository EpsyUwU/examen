from flask import Flask, request, jsonify, render_template
from analizador import MyParser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')
    parser = MyParser()
    parser.build_lexer()  # Construir el analizador léxico
    parser.build_parser()  # Construir el analizador sintáctico

    # Análisis léxico
    lexer = parser.lexer
    lexer.input(text)

    formatted_result = []
    tokens = []

    # Obtener todos los tokens
    while True:
        tok = lexer.token()
        if not tok:
            break
        formatted_result.append(f"Linea: {tok.lineno}, Tipo: {tok.type}, Valor: {tok.value}, Posición: {tok.lexpos}")
        tokens.append({'line': tok.lineno, 'type': tok.type, 'value': tok.value, 'pos': tok.lexpos})

    # Inicializar variables para capturar errores sintácticos
    syntax_error = None

    # Análisis sintáctico
    try:
        parse_result = parser.parser.parse(text)
        if parse_result:
            return jsonify({
                'formatted': "\n".join(formatted_result),
                'tokens_list': tokens,
                'parse_result': parse_result,
                'error': syntax_error
            })
        else:
            syntax_error = 'Error de sintaxis en el código.'
            return jsonify({
                'formatted': "\n".join(formatted_result),
                'tokens_list': tokens,
                'parse_result': None,
                'error': syntax_error
            })
    except Exception as e:
        syntax_error = f'Error interno: {str(e)}'
        return jsonify({
            'formatted': "\n".join(formatted_result),
            'tokens_list': tokens,
            'parse_result': None,
            'error': syntax_error
        })


if __name__ == '__main__':
    app.run(debug=True)
