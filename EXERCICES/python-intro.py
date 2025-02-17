import math
import sys
from time import perf_counter

## CALCULATRICE
## Question 1A: 4x^2 + 17x - 1 = 0
def solve_quadratic(a,b,c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0: ## If the discriminant is positive, there are two real roots.
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return round(root1, 2), round(root2, 2)
    elif discriminant == 0: ## If the discriminant is zero, there is one real root.
        root = -b / (2*a)
        return round(root, 2)
    else:
        return "unsolvable"

a = 4
b = 17
c = -1
print(f"Question 1A: {solve_quadratic(a,b,c)}")

## Question 2A: -5.6x^2 + 31.1x + 9 = 2
a = -5.6
b = 31.1
c = 9-2
print(f"Question 2A: {solve_quadratic(a,b,c)}")

## Question 3A: 8x^2 - 1265.789x = 0
a = 8
b = -1265.789
c = 0
print(f"Question 3A: {solve_quadratic(a,b,c)}")

## Question 4A: L'aire d'un cercle ayant pour diamètre 3.64m (indice: utilisez math.pi)
def solve_circle_area(r):
    return math.pi * r**2

r = 3.64
print(f"Question 4A: {round(solve_circle_area(r), 2)} m^2")

## Question 5A: L'aire extérieur d’un prisme rectangulaire aux dimensions suivantes: 4.5cm, 7cm, 12.75cm.
def solve_prism_area(h,l,w):
    return 2 * (h*l + h*w + l*w)

h = 4.5
w = 7
l = 12.75
print(f"Question 5A: {solve_prism_area(h,l,w)} cm^2")

## Question 6A: Volume d'un tipi ayant un rayon de 2.176 m et une hauteur de 3.5m.
def solve_cone_volume(r,h):
    return round(math.pi * r**2 * (h/3), 2)

r = 2.176
h = 3.5
print(f"Question 6A: {solve_cone_volume(r,h)} m^3")

## NOTES
## "Aujourd'hui" <- fonctionne
## 'Aujourd\'hui' <- fonctionne
## "Bonjour les "amis"" <- ne fonctionne pas
## Utiliser les backslash "\" avant les guillemets pour utiliser des guillemets dans des guillemets
## "Bonjour les \"amies\"" <- fonctionne

## CHAINES
## Question 1B: Trouvez comment inverser une chaîne.
def invert_chain(chain):
    return chain[::-1]

chain1 = "Hello"
print(f"Question 1B: {invert_chain(chain1)}")

# c1 = 'Hello'
# c2 = ''
# for i in range(len(c1)):
#     c2 += c[len(c1) - i - 1]

## Question 2B: Si on a des variables dont on veut insérer les valeurs dans une chaîne formatée, python nous permet de le faire, comment?
def insert_variable(chain):
    sentence = 'Allô {name}!'
    sentence = sentence.format(name = chain)
    return sentence

chain = "Alexia"
print(f"Question 2B: {insert_variable(chain)}")

## Question 3B: Comment isoleriez-vous la chaîne « les » à partir de la chaîne « Allo les amis ! » à l’aide d’indexes?
chain = "Allô les amis !"
slice = chain[5:8]

print(f"Question 3B: {slice}")

## LISTES
## Question 1C: Construisez un tableau de zéros de 2 X 5 avec des listes, au moins de deux manières différentes.
# Utilisation de la compréhension de listes
tab1 = [[0 for _ in range(5)] for _ in range(2)]
print(f"Question 1.1C: {tab1}")

# Création manuelle avec des boucles
tab2 = []
for _ in range(2):
    tab2.append([0] * 5)
print(f"Question 1.2C: {tab2}")

## Question 2C: Dans quel contexte utiliserait-on l[:] = [] plutôt que l = []?
## Réponse: Si on souhaite vider une liste existante tout en conservant sa référence
# Exemple avec l = []
l1 = [1, 2, 3]
l2 = l1  # l2 pointe vers la même liste que l1
l1 = []  # On remplace l1 par une nouvelle liste vide

print(f"Question 2.1C: {l2}")  # Résultat : [1, 2, 3] (l2 n'est pas affecté)

# Exemple avec l[:] = []
l1 = [1, 2, 3]
l2 = l1  # l2 pointe vers la même liste que l1
l1[:] = []  # On vide la liste référencée par l1 et l2

print(f"Question 2.2C: {l2}")  # Résultat : [] (l2 est affecté)

## DICTIONNAIRES
## Question 1D: Créez un dictionnaire qui a comme clé chaque élément de la liste suivante et comme valeur, son index (position dans la liste): -[74, ‘toto’, 87, ‘allo’, -6, 999]
d = {}
d = {value: index for index, value in enumerate([74, 'toto', 87, 'allo', -6, 999])}
## Autre méthode
# l = [74, 'toto', 87, 'allo', -6, 999]
# d = {l[index]index for index in range(len(l))}
print(f"Question 1D: {d}")

## Question 2D: Initialisez un dictionnaire à partir d'une liste de taille quelconque contenant des tuples de taille 2.
l = [(1,2),(3,4),(5,6)]
d = dict(l) # Conversion de la liste en dictionnaire
print(f"Question 2D: {d}")

## STRUCTURES DE CONTRÔLE
## Question 1E: Trouvez le nombre de paires de lapins en utilisant Fibonacci.
def fibonacci_lapins(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_lapins(n-1) + fibonacci_lapins(n-2)

## Question 2E: Trouvez combien il y a de paires de lapins en 18 mois à l'aide d’une boucle.
def itteratif_lapins(n):
    if n == 0 or n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

mois = 18
print(f"Question 2E: {itteratif_lapins(mois)}")

## FONCTIONS
## Question 1F: Créez une fonction fib() récursive.
## Voir la fonction fibonacci_lapins(n) de la question 1E, elle est déjà récursive.
def fibiter(n): # Itérative
    fn = fn1 = fn2 = 1
    while n >= 2:
        fn = fn1 + fn2
        fn1, fn2 = fn, fn1
        n -= 1
    return fn

def fibrec(n): # Récursive
    if n == 0 or n == 1:
        return 1
    return fibrec(n-1) + fibrec(n-2)

def fibdyn(n): # Dynamique
    def _fibdyn(n, sol_part):
        if n not in sol_part:
            sol_part[n] = _fibdyn(n-1, sol_part) + _fibdyn(n-2, sol_part)
        return sol_part[n]
    return _fibdyn(n, {0:1, 1:1})

def afficher(f, n):
    t = perf_counter()
    fn = f(n)
    t = perf_counter() - t

    print(f"Question 1F: {f.__name__}{{n}} = {fn} en {t:.6f} secondes")

def main():
    n = 18

    afficher(fibiter, n)
    afficher(fibrec, n)
    afficher(fibdyn, n)

    return 0

if __name__ == "__main__":
    main()

## Question 2F: Avec le fichier LesTroisMousquetaires.txt, vous allez:
## Compter le nombre de lignes, compter le nombre de caractères, compter le nombre de mots, compter le nombre de séquences de caractères s, où s est fournie en argument.
def analyse_texte(file_path, s):
    with open(file_path, 'r', encoding='utf-8') as file:
        lignes = file.read()
    
    nb_chars = len(lignes)
    nb_lignes = len(lignes.splitlines())
    nb_mots = len(lignes.split())
    nb_sequence = lignes.count(s)

    return nb_lignes, nb_chars, nb_mots, nb_sequence

file_path = "EXERCICES/FILES/LesTroisMousquetairesUTF8.txt"
num_chars, num_lines, num_words, num_sequence = analyse_texte(file_path, "s")

print(f"Question 2F: {num_chars} caractères, {num_lines} lignes, {num_words} mots, {num_sequence} sequences")