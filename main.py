def normaliser_caracteres(phrase: str) -> str:
    """
    Normalise chaque caractere accentue de la phrase.
    Argument:
    phrase -- la chaine a traiter
    Retourne:
    La chaine normalisee
    """
    phrase_normalisee = ""
    for lettre in phrase:
        if lettre == "ô":
            lettre = "o"
        elif lettre == "ç":
            lettre = "c"
        elif lettre in ["é", "è", "ê", "ë"]:
            lettre = "e"
        elif lettre in ["à", "â"]:
            lettre = "a"
        elif lettre == "ù":
            lettre = "u"
        phrase_normalisee += lettre
    return phrase_normalisee

def supprimer_espaces(phrase: str) -> str:
    """
    Supprime tous les espaces et tirets d'une chaine de caracteres.
    Argument:
    phrase -- la chaine à traiter
    Retourne:
    La chaine sans espaces ni tirets.
    """
    caracteres_a_supprimer = [" ", "-", "'", "!", "?", ",", ":"]
    for char in caracteres_a_supprimer:
        phrase = phrase.replace(char, "")

    return phrase

def ispalindrome(phrase: str) -> bool:
    """
    Vérifie si la chaîne de caractères passée en paramètre est un palindrome.

    Argument:
    phrase -- la chaîne à vérifier
    """
    phrase = phrase.lower()
    phrase = supprimer_espaces(phrase)
    phrase = normaliser_caracteres(phrase)
    premier = 0
    dernier = len(phrase) - 1
    while premier < dernier:
        if phrase[premier] != phrase[dernier]:
            return False
        premier += 1
        dernier -= 1
    return True

def main() -> None:
    """ Fonction principal testant des cas basiques"""
    # Appels à la fonction secondaire
    for s in ["radar", "RaDAr", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
