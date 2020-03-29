
from app import app
from flask import render_template,request,jsonify
from flask import Markup
from random import randint

hardcodedtoken = '98989898'
bingoList = []
refeshTag = '<meta http-equiv="refresh" content="3">'

@app.route('/')
def index():
    return render_template('index.html',bingoList=bingoList,refresh=Markup(refeshTag))

@app.route('/owner')
def admin():
    token = request.args.get('tkn')
    if token is not None and token == hardcodedtoken:
        value = Markup('''
        <script type=text/javascript>

        function getUrlParam(parameter, defaultvalue){
            var urlparameter = defaultvalue;
            if(window.location.href.indexOf(parameter) > -1){
                urlparameter = getUrlVars()[parameter];
                }
            return urlparameter;
        }
        function getUrlVars() {
            var vars = {};
            var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
                vars[key] = value;
            });
            return vars;
        }

        $(function() {$('#new').bind('click', 
        function(e) { e.preventDefault(); 

        var token = getUrlVars('tkn')['tkn']
        fetch('/generate?tkn='+token)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data['digits']);
            window.location.reload();
        });
        });});

        $(function() {$('#clear').bind('click', 
        function(e) { e.preventDefault(); 
        var token = getUrlVars('tkn')['tkn']
        fetch('/clear?tkn='+token)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data['digits']);
            window.location.reload();
        });
        });});

        </script>
        <h1>
        <button id='new' class='button-pos rwd-table center'>GENERATE</button>
        <button id='clear' class='button-pos rwd-table center'>CLEAR</button>
        </h1>
        ''')
        return render_template('index.html',bingoList=bingoList,adminHTML=value)
    return 'invalid'
    

@app.route('/generate', methods=['GET'])
def generate():
    token = request.args.get('tkn')
    if token == hardcodedtoken:
        while True:
            num = randint(1, 90)
            if num not in bingoList and len(bingoList) < 90:
                bingoList.append(num)
                break
            else:
                pass
    else:
        return ''
    return {'digits':bingoList}

@app.route('/clear', methods=['GET'])
def clear():
    token = request.args.get('tkn')
    if token == hardcodedtoken:
        global bingoList
        bingoList = []
    else:
        return ''
    return {'digits':bingoList}