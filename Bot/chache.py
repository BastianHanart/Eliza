import os

CACHE_DIR = "cache"
MAX_HISTORY = 5
os.makedirs(CACHE_DIR, exist_ok=True)

def create_message_cache (message, ID):

    # Ouvrir dossier
    chemin = os.path.join(CACHE_DIR, str(ID))
    os.makedirs(chemin, exist_ok=True)

    # Parcourir le dossier cache et regarder les nom des fichier
    fichiers = os.listdir(chemin)
    for k in range(1, MAX_HISTORY + 1):
        filename = f"message_{k}.txt"
        filepath = os.path.join(chemin, filename)

        # Si le fichier existe par le créer et écrire le message dedans
        if filename not in fichiers:
            with open(filepath, "w") as f:
                f.write(message)
            return
        
    # Si il y a déja le max de message on supprime le premier
    os.remove(os.path.join(chemin, "message_1.txt"))

    # On renomme les fichier en les décalant de 1
    for j in range(2, MAX_HISTORY+1):
        os.rename(os.path.join(chemin, f"message_{j}.txt"), os.path.join(chemin, f"message_{j-1}.txt"))

    # Puis on écrit le message actuel en l'appelant message_10
    with open(os.path.join(chemin, f"message_{MAX_HISTORY}.txt"), "w") as fichier:
        fichier.write(message)
        return

def load_messages(ID):
    messages = []
    chemin = os.path.join(CACHE_DIR, str(ID))

    for k in range(1, MAX_HISTORY + 1):
        filepath = os.path.join(chemin, f"message_{k}.txt")

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                messages.append(f.read())

    return messages