
---

````markdown
# 🎯 Puissance 4 – IA vs Humain

Bienvenue dans **Puissance 4**, une implémentation console où un joueur humain affronte une **intelligence artificielle** 🧠 dans une grille de **6 lignes x 12 colonnes**. Le jeu repose sur l'algorithme **Minimax avec élagage alpha-bêta** et une évaluation heuristique du plateau.

---

## 🚀 Lancer le jeu

Assurez-vous d’avoir **Python 3** installé.

Lancez simplement le script :

```bash
python puissance4.py
````

🗨️ Le jeu vous demandera qui commence :
Tapez `H` pour **Humain** ou `IA` pour **l'Intelligence Artificielle**.

---

## 🎮 Fonctionnalités

* ✅ Grille dynamique 6x12
* 🤖 IA avec stratégie anticipative :

  * Coup gagnant immédiat
  * Blocage des menaces adverses
  * Analyse jusqu'à 4 coups à l'avance
* 🧠 Évaluation heuristique du plateau
* 🏁 Détection automatique de victoire :

  * Lignes
  * Colonnes
  * Diagonales ↘️↖️
* ⏱️ Bonus selon la rapidité moyenne des décisions

---

## 🔍 Aperçu du plateau

Le plateau est affiché en console comme suit :

```
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
-------------------------
 0 1 2 3 4 5 6 7 8 9 0 1
```

* `X` représente le joueur **+1**
* `O` représente le joueur **-1**

---

## 🧠 IA & Stratégie

### 🔄 Algorithme utilisé :

* **Minimax** (recherche adversariale)
* **Élagage alpha-bêta** pour optimiser les performances

### 📈 Heuristique :

* +100000 si 4 pions alignés
* +10000 pour 3 pions + 1 case vide
* +10 pour 2 pions + 2 cases vides
* -80 si l’adversaire a 3 pions + 1 case vide

### 💡 Comportement :

* Joue immédiatement s’il peut gagner
* Bloque un coup gagnant de l’adversaire
* Sinon, évalue les meilleurs coups selon la profondeur

---

## 🏆 Système de points

En cas de victoire :

* Base : **3 points**
* +1 point pour le joueur le plus **rapide** (calcul de la moyenne de réaction)
* Match nul possible si la grille est pleine sans alignement gagnant

---

## 📁 Organisation du code

| Fonction          | Rôle                            |
| ----------------- | ------------------------------- |
| `play()`          | Boucle principale du jeu        |
| `print_board()`   | Affichage du plateau            |
| `result()`        | Applique un coup                |
| `terminal_test()` | Vérifie la fin du jeu           |
| `best_move()`     | Choix du coup IA                |
| `heuristic()`     | Score d’un plateau non terminal |
| `actions()`       | Liste des colonnes jouables     |

---

## 🛠️ Améliorations possibles

* Interface graphique avec `pygame` ou `tkinter`
* Amélioration de l’heuristique (prise en compte du centre, menace double, etc.)
* Paramétrage de la taille de la grille et de la profondeur IA

---

## 📚 Pour aller plus loin

Ce projet est un bon point de départ pour :

* Comprendre le fonctionnement de l’IA dans les jeux à deux joueurs
* Appliquer les concepts de Minimax et d’élagage alpha-bêta
* Travailler sur la modélisation et la détection de patterns dans un plateau de jeu

---

🤝 Bon jeu et bonne chance contre l’IA !

```

---

```
