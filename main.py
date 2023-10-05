from flask import *
import json
import wzq
import webbrowser

app = Flask(__name__)

global board
board = wzq.board()


@app.route('/')
def index_page():
    return render_template('index.html', range=range(15))


@app.route('/wzq/<color>/')
def wzq_page(color):
    global board
    board = wzq.board()
    print(color)
    return render_template('wzq.html', range=range(15), color=color)

# @app.route('/ai/next_step')
# def wzq_ai_next_step():
#     global board
#     player_color = request.args.get('player_color')
#     if player_color == "black":
#         ai_color = 1
#     else:
#         ai_color = -1

#     next = wzq.nextStep(board, ai_color)
#     board = next[0]
#     return next[1], next[2]

@app.route('/wzqai')
def wzq_ai_next_step():
    global board
    player_color = request.args.get('player_color')
    if player_color == "black":
        ai_color = 1
    else:
        ai_color = -1

    next_move = wzq.nextStep(board, ai_color)


    board = next_move[0]
    print(next_move)

    next_move[1][0] = int(next_move[1][0])
    next_move[1][1] = int(next_move[1][1])
    if next_move[2] == -1:
        next_move[2] = 3
    return json.dumps([next_move[1], next_move[2]])

@app.route('/wzq/change/<color>/<row>/<col>/')
def wzq_change(color, row, col):
    global board
    if color == "black":
        color = -1
    else:
        color = 1
    board[int(row)][int(col)] = color
    return "ok"





if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run()

