# Cooccurrences et Synonymes

### 1. Apprentissage Machine
- L'apprentissage machine et l'intelligence artificielle reposent sur la **capacité de prédire**.
- Le cerveau humain fonctionne en accédant à la mémoire pour **prédire** une solution.
- Face à une situation nouvelle, nous devons **généraliser** en extrayant des **patrons (patterns)** de notre mémoire.
- Exemple :
  - Un individu n'a jamais vu un lion en colère.
  - Il peut associer cela à un chien menaçant et choisir de fuir.
  - Il ne l'associe pas à une mouche menaçante (qu'il pourrait écraser).
- **Intelligence artificielle = généralisation + prédiction**

### 2. Information Structurée
- Les informations perçues sont **structurées**.
- Exemples :
  - "Pomme verte" → **miam** (bonne à manger)
  - "Jambon vert" → **danger** (probablement périmé)
- **Contexte** = clé pour comprendre la signification d’un mot.

### 3. Entraînement
- La syntaxe et la grammaire influencent la recherche de synonymes.
- Exemple :
  - "Je mange une pomme."
  - "J'écris du code."
  - "Pomme" et "code" ont une fonction grammaticale similaire.
- **Mais la syntaxe seule ne suffit pas !** La **sémantique** (la manière dont nous comprenons le contenu d’un mot ou d’une phrase en fonction du contexte) est essentielle.
- Exemple :
  - "Mon amour, je t’aime !"
  - "Ma chérie, je t’aime !"
  - "Amour" et "chérie" ont une sémantique similaire.

### 4. Hypothèse de la Sémantique
- **Hypothèse principale :**
  - Des mots ayant le même **contexte** (les mêmes mots environnants) ont une **sémantique similaire**.
- On ne cherche pas la signification exacte d’un mot, mais **les mots ayant une signification proche**.

### 5. Matrice de Cooccurrences
- **Indexation des mots** : chaque mot unique a un identifiant numérique.
- **Matrice de cooccurrences** :
  - Tableau qui compte combien de fois un mot apparaît avec un autre.
  - Exemple : Combien de fois "je" et "amour" apparaissent ensemble ?
- Une matrice **symétrique** : si un mot voit un autre, l'inverse est vrai aussi.
- **Vecteur de cooccurrences = patron généralisé**

### 6. Prédiction
- Comparer les vecteurs de cooccurrences pour voir **quels mots sont similaires**.
- **Score de similarité** :
  - On peut comparer les vecteurs avec des opérations mathématiques.
  - L’objectif est d’attribuer une valeur à la similarité (exemple : chien vs mouche).
  - Quelle fonction de score est la plus pertinente ? Comparer les résultats !

### 7. Fenêtres de Contexte
- Problème : certaines phrases sont longues, d’autres courtes.
- **Solution : Définir une fenêtre de mots** autour du mot central.
- Exemple : fenêtre de taille 7 autour de "orange" :
  - "J’ai mangé une pomme | du Québec, une orange de la Floride | et un hamburger de chez McDo."
  - Mots cooccurrents de "orange" : "du", "Québec", "une", "de", "la", "Floride".
- **Expérimenter différentes tailles de fenêtres !**

### 8. Nettoyage des Données
- **Majuscules/minuscules** : mettre tout en **minuscule** pour éviter les doublons ("Orange" vs "orange").
- **Stop-words** :
  - Certains mots très courants comme "le", "tu", "qui" peuvent fausser les résultats.
  - Ils sont **écartés des prédictions**, mais **gardés dans la matrice**.
  - Exemple : "ma" n'est pas un bon synonyme de "chérie" même si leurs scores sont similaires.