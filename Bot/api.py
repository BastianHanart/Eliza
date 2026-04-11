import aiohttp
import os
from dotenv import load_dotenv
from rapidfuzz import process

ANIMAUX = [
    "chien", "chiens", "dog", "dogs",
    "chat", "chats", "cat", "cats",
    "lion", "lions", "lion", "lions",
    "tigre", "tigres", "tiger", "tigers",
    "éléphant", "éléphants", "elephant", "elephants",
    "girafe", "girafes", "giraffe", "giraffes",
    "zèbre", "zèbres", "zebra", "zebras",
    "loup", "loups", "wolf", "wolves",
    "renard", "renards", "fox", "foxes",
    "lapin", "lapins", "rabbit", "rabbits",
    "hamster", "hamsters", "hamster", "hamsters",
    "cheval", "chevaux", "horse", "horses",
    "vache", "vaches", "cow", "cows",
    "cochon", "cochons", "pig", "pigs",
    "mouton", "moutons", "sheep", "sheep",
    "chèvre", "chèvres", "goat", "goats",
    "âne", "ânes", "donkey", "donkeys",
    "poule", "poules", "chicken", "chickens",
    "coq", "coqs", "rooster", "roosters",
    "canard", "canards", "duck", "ducks",
    "oie", "oies", "goose", "geese",
    "dinde", "dindes", "turkey", "turkeys",
    "pigeon", "pigeons", "pigeon", "pigeons",
    "moineau", "moineaux", "sparrow", "sparrows",
    "aigle", "aigles", "eagle", "eagles",
    "hibou", "hiboux", "owl", "owls",
    "corbeau", "corbeaux", "crow", "crows",
    "perroquet", "perroquets", "parrot", "parrots",
    "colibri", "colibris", "hummingbird", "hummingbirds",
    "souris", "souris", "mouse", "mice",
    "rat", "rats", "rat", "rats",
    "écureuil", "écureuils", "squirrel", "squirrels",
    "castor", "castors", "beaver", "beavers",
    "ours", "ours", "bear", "bears",
    "panda", "pandas", "panda", "pandas",
    "koala", "koalas", "koala", "koalas",
    "kangourou", "kangourous", "kangaroo", "kangaroos",
    "crocodile", "crocodiles", "crocodile", "crocodiles",
    "alligator", "alligators", "alligator", "alligators",
    "serpent", "serpents", "snake", "snakes",
    "vipère", "vipères", "viper", "vipers",
    "boa", "boas", "boa", "boas",
    "lézard", "lézards", "lizard", "lizards",
    "caméléon", "caméléons", "chameleon", "chameleons",
    "grenouille", "grenouilles", "frog", "frogs",
    "crapaud", "crapauds", "toad", "toads",
    "requin", "requins", "shark", "sharks",
    "baleine", "baleines", "whale", "whales",
    "dauphin", "dauphins", "dolphin", "dolphins",
    "phoque", "phoques", "seal", "seals",
    "otarie", "otaries", "sea lion", "sea lions",
    "morue", "morues", "cod", "cod",
    "saumon", "saumons", "salmon", "salmon",
    "thon", "thons", "tuna", "tuna",
    "pieuvre", "pieuvres", "octopus", "octopuses",
    "calmar", "calmars", "squid", "squid",
    "méduse", "méduses", "jellyfish", "jellyfish",
    "étoile de mer", "étoiles de mer", "starfish", "starfish",
    "homard", "homards", "lobster", "lobsters",
    "crabe", "crabes", "crab", "crabs",
    "crevette", "crevettes", "shrimp", "shrimp",
    "escargot", "escargots", "snail", "snails",
    "limace", "limaces", "slug", "slugs",
    "fourmi", "fourmis", "ant", "ants",
    "abeille", "abeilles", "bee", "bees",
    "guêpe", "guêpes", "wasp", "wasps",
    "moustique", "moustiques", "mosquito", "mosquitoes",
    "papillon", "papillons", "butterfly", "butterflies",
    "coccinelle", "coccinelles", "ladybug", "ladybugs",
    "scarabée", "scarabées", "beetle", "beetles",
    "araignée", "araignées", "spider", "spiders",
    "scorpion", "scorpions", "scorpion", "scorpions",
    "termite", "termites", "termite", "termites",
    "mouche", "mouches", "fly", "flies",
    "libellule", "libellules", "dragonfly", "dragonflies",
    "criquet", "criquets", "grasshopper", "grasshoppers",
    "sauterelle", "sauterelles", "grasshopper", "grasshoppers",
    "hérisson", "hérissons", "hedgehog", "hedgehogs",
    "alpaga", "alpagas", "alpaca", "alpacas",
    "lama", "lamas", "llama", "llamas",
    "bison", "bisons", "bison", "bisons",
    "antilope", "antilopes", "antelope", "antelopes",
    "lynx", "lynx", "lynx", "lynx",
    "jaguar", "jaguars", "jaguar", "jaguars",
    "léopard", "léopards", "leopard", "leopards",
    "guépard", "guépards", "cheetah", "cheetahs"
]

def trouver_animal(animal):
    animalchoix = animal.lower().split()
    print(animalchoix)

    for k in animalchoix:
        print(k)
        if k in ANIMAUX:
            print("Yep")
            return k
    print("mauvaise vérif")
    return None

load_dotenv(dotenv_path="config")

async def récupérer_info_animal(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": os.getenv("CLE_API")}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            print("attente d'info d'API")
            if response.status == 200:
                data = await response.json()

                print("Bonne réponse d'API")
                if data:
                    print("Bon élément d'API")
                    return data[0]
            
            print("Aie d'API")
            return None