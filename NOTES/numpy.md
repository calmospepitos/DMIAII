# NumPy - Numerical Python

## 1. Introduction
- Python est un langage interprété, donc **non compilé**.
- Les boucles et appels récursifs sont **réinterprétés à chaque exécution**.
- Pour le **calcul scientifique**, les listes Python sont insuffisantes car trop lentes.

## 2. Pourquoi utiliser NumPy ?
- Modules optimisés comme **NumPy** et **SciPy** utilisent du **code compilé en C** pour accélérer les calculs.
- **NumPy** permet des opérations mathématiques **rapides et efficaces** sur des matrices et tableaux.

## 3. Premiers pas avec NumPy
### **Importation de NumPy**
```python
import numpy as np
```
- `np` est un alias pour **faciliter l'utilisation des fonctions NumPy**.

### **Création de Vecteurs et Matrices**
- **Vecteur (1D) avec `arange`** :
  ```python
  v = np.arange(5)  # [0, 1, 2, 3, 4]
  ```
- **Matrice avec `reshape`** :
  ```python
  mat = np.arange(9).reshape(3, 3)  # Matrice 3x3
  ```
- **Matrices remplies de 1 ou 0** :
  ```python
  ones = np.ones((3, 3))
  zeros = np.zeros((3, 3))
  ```

## 4. Accéder aux valeurs et dimensions
- **Accès aux éléments** :
  ```python
  a = np.array([[1, 2, 3], [4, 5, 6]])
  print(a[0, 1])  # Accès à l'élément ligne 0, colonne 1
  ```
- **Dimensions d'une matrice** :
  ```python
  print(a.shape)  # Renvoie (2,3)
  ```

## 5. Opérations sur les Matrices
- **Opérations mathématiques sur tous les éléments** :
  ```python
  b = a * 2  # Multiplie chaque élément par 2
  c = a + 3  # Ajoute 3 à chaque élément
  ```
- **Somme de tous les éléments** :
  ```python
  total = np.sum(a)
  ```

## 6. Exercice
1. **Créer une matrice 5x5 avec des valeurs aléatoires** :
   ```python
   mat = np.random.randint(0, 10, (5, 5))
   print(mat)
   ```
2. **Créer une fonction qui retourne la somme des différences entre deux vecteurs** :
   ```python
   def somme_differences(v1, v2):
       return np.sum(np.abs(v1 - v2))
   ```
3. **Comparer toutes les paires de vecteurs de la matrice** :
   ```python
   def comparer_vecteurs(mat):
       for i in range(mat.shape[0]):
           for j in range(i+1, mat.shape[0]):
               print(f"Différence entre ligne {i} et ligne {j}: {somme_differences(mat[i], mat[j])}")
   
   comparer_vecteurs(mat)
   ```