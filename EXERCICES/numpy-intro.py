import numpy as np

# Question 1A: Créez une matrice de dimension (5X5) aux valeurs entières aléatoires.
def question_1a():
    return np.random.randint(0, 10, (5, 5)) # 5x5 matrix with values between 0 and 10

print(f"Question 1A: {question_1a()}")

# Question 2A: Créez une fonction qui retourne la somme des différences entre deux vecteurs.
def question_1b(v1, v2):
    return np.sum(np.abs(v1 - v2))

print(f"Question 2A: {question_1b(np.array([1, 2, 3]), np.array([4, 5, 6]))}")

# Question 3A: Affichez le résultat de cette fonction pour toutes les paires de vecteurs de dimension (1X5) possibles dans la matrice de la première question.
def question_1c(mat):
    for i in range(mat.shape[0]): # for each row (1x5 vector)
        for j in range(mat.shape[0]): # for each row (1x5 vector)
            print(f"Question 3A: {question_1b(mat[i], mat[j])}")

mat = question_1a()
question_1c(mat)