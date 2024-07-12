from solver import return_solution
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/solved", methods=["POST", 'GET'])
def solved():
    try:
        sudoku = request.form.get('sudoku')
        sudoku_unsolved = json.loads(sudoku)
        sudoku = json.loads(sudoku)
        solution = return_solution(sudoku)
    except:
        return redirect('/')
    return render_template('solved.html', sol=list(solution), prev=list(sudoku_unsolved))