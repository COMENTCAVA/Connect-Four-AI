import math
import random
import time

def construct(s):
    for i in range(0, 6):
        a = []
        for j in range(0, 12):
            a.append(0)
        s.append(a)


s = []
construct(s)
start_time = {+1: [], -1: []}

# colum = colonne dans laquelle on joue
# player = identifiant du joueur (1 ou -1 = le plus simple)
def result(s, column, player):
    if s[0][column] != 0:
        # la colonne est déjà remplie.
        return None
    else:
        i = 0
        while i < len(s) - 1 and s[i + 1][column] == 0:
            i = i + 1

        copy = [row.copy() for row in s]
        copy[i][column] = player
        return copy


# Cette fonction vise à dans une liste ordonnée
# verifier si 4 elements similaires sont à côté
# Etat: terminé
def sameInARow(l):
    times = 0
    last = None
    for element in l:
        if last == None:
            last = element
        elif last == element:
            times += 1
            if times == 3:
                return element
        else:
            last = element
            times = 0
    return None

def moyenne(n):
    if not n:
        return float('inf')
    return sum(n) / len(n)

def terminal_test(s):
    point = 0
    # on teste d'abord les lignes
    for i in range(len(s)):
        el = []
        for j in range(len(s[i])):
            el.append(s[i][j])
        same = sameInARow(el)
        if same != None and same != 0:
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1*same]):
                point+=1
            return [True, same, point]

    # on teste ensuite les colonnes
    n_rows = len(s)
    n_cols = len(s[0])
    for column in range(n_cols):
        col = []
        for line in range(n_rows):
            col.append(s[line][column])
        same = sameInARow(col)
        if same not in (None, 0):
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1 * same]):
                point += 1
            return [True, same, point]

    # on démarre sur la première ligne puis sur la première colonne
    for start_col in range(n_cols):
        diag = []
        r, c = 0, start_col
        while r < n_rows and c < n_cols:
            diag.append(s[r][c])
            r += 1;
            c += 1
        same = sameInARow(diag)
        if same not in (None, 0):
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1 * same]):
                point += 1
            return [True, same, point]

    for start_row in range(1, n_rows):
        diag = []
        r, c = start_row, 0
        while r < n_rows and c < n_cols:
            diag.append(s[r][c])
            r += 1;
            c += 1
        same = sameInARow(diag)
        if same not in (None, 0):
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1 * same]):
                point += 1
            return [True, same, point]

    # on démarre sur la première ligne puis sur la dernière colonne
    for start_col in range(n_cols):
        diag = []
        r, c = 0, start_col
        while r < n_rows and c >= 0:
            diag.append(s[r][c])
            r += 1;
            c -= 1
        same = sameInARow(diag)
        if same not in (None, 0):
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1 * same]):
                point += 1
            return [True, same, point]

    for start_row in range(1, n_rows):
        diag = []
        r, c = start_row, n_cols - 1
        while r < n_rows and c >= 0:
            diag.append(s[r][c])
            r += 1;
            c -= 1
        same = sameInARow(diag)
        if same not in (None, 0):
            point = 3
            if moyenne(start_time[same]) < moyenne(start_time[-1 * same]):
                point += 1
            return [True, same, point]

    if start_time[1]!=None and start_time[-1]!=None:
        if len(start_time[1])>0 and len(start_time[-1])>0:
            if moyenne(start_time[1]) < moyenne(start_time[-1]):
                point = 1
            else:
                point = -1

    return [False, 0, point]

def actions(s):
    actions = [col for col in range(len(s[0])) if s[0][col] == 0]
    random.shuffle(actions)
    return actions

def utility(s, player):
    term, winner, _ = terminal_test(s)
    if not term:
        return None
    if winner == player:   return +1
    if winner == 0:        return  0
    return -1

def Terminal_Test(board):
    termine, _, _ = terminal_test(board)
    return termine

def IA_Decision(board, max_depth=4):
    return best_move(board, player=+1, max_depth=max_depth)

def heuristic(s, player):
    def score_line(line, player):
        score = 0
        for i in range(len(line) - 3):
            window = line[i:i+4]
            if window.count(player) == 4:
                score += 100000
            elif window.count(player) == 3 and window.count(0) == 1:
                score += 10000
            elif window.count(player) == 2 and window.count(0) == 2:
                score += 10
            if window.count(-player) == 3 and window.count(0) == 1:
                score -= 80
        return score

    total_score = 0
    for row in s:
        total_score += score_line(row, player)
    for col in zip(*s):
        total_score += score_line(list(col), player)

    for r in range(6 - 3):
        for c in range(12 - 3):
            diag = [s[r+i][c+i] for i in range(4)]
            total_score += score_line(diag, player)

    for r in range(6 - 3):
        for c in range(3, 12):
            diag = [s[r+i][c-i] for i in range(4)]
            total_score += score_line(diag, player)

    return total_score



def max_value(s, player, depth, alpha, beta):
    term, _, pts = terminal_test(s)
    if term:
        return utility(s, player)
    if depth == 0:
        return heuristic(s, player)
    v = -math.inf
    for col in actions(s):
        child = result(s, col, player)
        v = max(v, min_value(child, -player, depth-1, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(s, player, depth, alpha, beta):
    term, _, pts = terminal_test(s)
    if term:
        return utility(s, player)
    if depth == 0:
        return heuristic(s, player)
    v = math.inf
    for col in actions(s):
        child = result(s, col, player)
        v = min(v, max_value(child, -player, depth-1, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def best_move(s, player, max_depth=6):
    #On verifie toutes les actions (profondeur 1)
    #Si l'IA peut gagner elle va gagner tout de suite
    for col in actions(s):
        child = result(s, col, player)
        term, winner, pts = terminal_test(child)
        if term and winner == player:
            return col

    #On bloque un coup (profondeur 1)
    #Si l'autre peut gagner on bloque son coup (méthode de sureté)
    for col in actions(s):
        child = result(s, col, -player)
        term, winner, pts = terminal_test(child)
        if term and winner == -player:
            return col

    #Verification en profondeur de base
    #Pire valeur pour démarrer
    best_score = -math.inf
    best_col   = None
    for col in actions(s):
        child = result(s, col, player)
        score = min_value(child, -player, max_depth-1, -math.inf, math.inf)
        if score > best_score:
            best_score = score
            best_col   = col
    return best_col



def print_board(board):
    symbols = {0: " ", 1: "X", -1: "O"}
    print()
    for row in board:
        print("".join(f"|{symbols[cell]}" for cell in row) + "|")
    print("-" * (len(board[0]) * 2 + 1))
    print(" " + "".join(f"{i%10} " for i in range(len(board[0]))))
    print()

def play():
    # initialisation du plateau
    board = [row.copy() for row in s]
    # qui commence ? on force H ou IA
    while True:
        h = input("Qui commence à jouer ? (H/IA) : ").strip().upper()
        if h in ("H", "IA"):
            break
        print("Réponse invalide, tapez H ou IA.")
    print(f"C'est donc {h} qui commence à jouer !\nBonne chance !\n")

    # on définit qui est +1 et qui est -1
    if h == "H":
        human_player = +1
        ai_player    = -1
    else:
        human_player = -1
        ai_player    = +1

    # on démarre toujours le tour +1 en premier
    player = +1
    print_board(board)
    while True:
        # choix de la colonne
        if player == human_player:
            # tour de l'humain
            ss=time.time()
            col_conv = input("Votre colonne ? ")
            while not col_conv.isdigit():
                col_conv = input("Votre colonne ? ")
            col = int(col_conv)
            while not (0 <= col < len(board[0])) or board[0][col] != 0:
                col = int(input("Colonne invalide ou pleine, rechoisissez : "))
            start_time[player].append(time.time() - ss)
        else:
            # tour de l'IA
            ss = time.time()
            col = best_move(board, player, max_depth=4)
            print("IA joue en colonne", col)
            start_time[player].append(time.time() - ss)

        # on applique le coup
        board = result(board, col, player)
        print_board(board)

        # on vérifie tout de suite la fin de partie
        term, winner, pt = terminal_test(board)
        if term:
            if winner == human_player:
                print("L'humain a gagné +" + str(pt) + " points")
            elif winner == ai_player:
                print("L'IA a gagné +" + str(pt) + " points")
            else:
                print("Match nul +" + str(pt) + " points")
            break

        # on alterne
        if player == human_player:
            time.sleep(2)
        player = -player

play()