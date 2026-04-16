import discord
from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import os
from chache import create_message_cache, load_messages

# On load le fichier de config avec le token du bot
load_dotenv(dotenv_path="config")

# Mise en place du bot discord de base
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

# Lorsque le bot est lancé, le notifier
@client.event
async def on_ready():
    print("Le bot est prêt !")
    try:
        synchro = await client.tree.sync()
        print(f"Commandes connectées : {len(synchro)}")
    except Exception as exception:
        print(exception)



async def requete(prompt):
    async with aiohttp.ClientSession() as question:
        try:
            # Requête
            async with question.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "animalbot",
                    "prompt": prompt,
                    "stream": False
                }
            ) as reponse:
                
                # Réponse
                data = await reponse.json()
                return(data["response"])

        except Exception as exception:
            print(exception)
            return "Une erreur est survenue."

@client.tree.command(name="help", description="Afficher l'aide du bot")
async def help_command(interaction: discord.Interaction):


    embed = discord.Embed(
        title="Aide - VETBot",
        description="**Merci d'utiliser VetBot, le Bot numéro 1 pour avoir toutes les informations nécessaires, sur nos amis les animaux !!!**\n" \
        "Voici les commandes disponibles :",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="/info",
        value="Vous souhaitez obtenir des informations sur un animal en particulier ? Cette commande est faite pour cela !\nEx : `/info chien`",
        inline=False
    )

    embed.add_field(
        name="/diagnostic",
        value="Ne pas comprendre ce qui arrive à notre animal adoré peut vraiment être quelque chose de très stressant ! Grâce au diagnostic, obtenez un avis général sur l'état de ton animal ! \nEx : `/diagnostic mon chien est fatigué`",
        inline=False
    )

    embed.add_field(
        name="/delete",
        value="Vous souhaitez enlever certains messages de votre fils, cette fonction le permet !\nEx : `/delete 10`",
        inline=False
    )

    embed.add_field(
        name=""" /!\ Important /!\ """,
        value=(
            "• VETBot ne remplace PAS un vétérinaire\n"
            "• Aucun traitement ou diagnostic médical précis n'est donné\n"
            "• En cas de doute, consulte un professionnel"
        ),
        inline=False
    )

    embed.set_footer(text="VETBot - Prends soin de ton animal")

    await interaction.response.send_message(embed=embed)


### Commande /delete qui permet de supprimer des messages ###
@client.tree.command(name="delete", description="Supprimer n-messages du channel")
async def delete(interaction: discord.Interaction, nombre: int):
    
    # Vérifier la validité du nombre chosis
    if nombre <= 0:
        await interaction.response.send_message("Chosissez un nombre valide de message à supprimer" , ephemeral=True)
        return
    
    # Empèche discord de crash si ne répond pas rapidement
    await interaction.response.defer(ephemeral=True)

    # Si tout est good on vient supprimer 
    await interaction.channel.purge(limit=nombre)
    await interaction.followup.send(f"{nombre} messages supprimés.", ephemeral=True)


### Commande /info qui permet d'avoir des infos sur un animal ###
@client.tree.command(name="info", description="Avoir des infos sur un animal")
async def info(interaction: discord.Interaction, nom: str):

    await interaction.response.defer()
    
    # prompt à envoyer au bot 
    prompt = f"""
        Tu es VETBot.

        Présente les informations de l'animal pour un embed Discord avec une belle mise en page.

        Tu dois OBLIGATOIREMENT faire un choix entre 2 cas :

        CAS 1 = Si {nom} n'est pas un nom d'animal domestique ou sauvage, une race d'animal domestique ou sauvage, ou une espèce d'animaux domestique ou sauvage, (donc un humain mort ou encore en vie ne compte pas), réponds UNIQUEMENT : "Désolé je suis un expert du monde des animaux, je ne peux vous donner des informations sur {nom}" Rien de plus, pas d'explications

        CAS 2 = Sinon Répond normalement:

            Contraintes :
            - Utilise du Markdown Discord (**gras**, sauts de ligne)
            - Structure claire et lisible
            - Pas de JSON, pas de format clé:valeur
            - Pas de texte inutile

            Format attendu (style linteraction.channel.idibre mais propre) :

            **Nom :**
            ...

            ***Taille :***
            ...

            ***Poids :***
            ...

            ***Description :***
            ...

        Animal : {nom}
    """
    try:
        message_envoye = await requete(prompt)
        # Si désolé dans la Réponse, alors ne pas faire de carte et envoyé le message telle quelle car ça veut dire qu'on ne parle pas d'animaux
        if "Désolé" in message_envoye:
            await interaction.followup.send(content=message_envoye)
        
        # Sinon on fait une carte avec nom taille poids description
        else :

            embed = discord.Embed(
                description=message_envoye,
                color=discord.Color.green()
            )
            await interaction.followup.send(content=None, embed=embed)
            
    except Exception as e:
        print("Erreur:", e)
        await interaction.followup.send("Erreur lors de la génération de votre réponse ...")



### Commande /diagnostique pour faire un diagnostique sur un aniomal ###
@client.tree.command(name="diagnostic", description="Faire un diagnostique sur un animal")
async def diagnostic(interaction: discord.Interaction, message: str):

    await interaction.response.defer()


    memoire = load_messages(interaction.channel.id)
        
    # prompt à envoyer au bot 
    prompt = f"""
    Tu es VETBot.

    Voici ta mémoire des anciens actuels. Utilise là si elle peut t'aider à répondre au message actuel {memoire}.

    Tu dois OBLIGATOIREMENT faire un choix entre 2 cas, Bien sûr tu ne DOIS en AUCUN CAS ANONCER à l'utilisateur quels choix tu as pris, tes étapes de cheminement, ni ton chemin de reflexion !:

    - CAS 1 = Si la demande de l'individu n'est pas un diagnostique de l'état d'un animal, une demande de conseil sur son animal, ou simplement une inquiétude sur l'animal, répond UNIQUEMENT : "Désolé je suis un expert du monde des animaux, je ne peux vous donner des informations sur votre demande" Tu n'ajoutes rien de plus, aucune autre explication n'est nécessaire !

    - CAS 2 = Si la demande concerne un animal (conseil, inquiétude, boiterie, etc.) :

        Rédige une réponse fluide et amicale (sans titres, sans "1." ou "2.", et sans mentionner les mots 'ANALYSE' ou 'ORIENTATION').
        1. ANALYSE : Propose des explications logiques et pédagogiques sur ce qui peut causer ce comportement (sans affirmer).
        2. RASSURANCE : Utilise un ton calme. Valorise le fait que le propriétaire soit attentif à son animal.
        3. ORIENTATION : Si cela semble sérieux, conseille une consultation vétérinaire comme une étape de sécurité normale.

        STRICTES RESTRICTIONS :
        - RÉPONSE DIRECTE : Ne mentionne jamais "Cas 1" ou "Cas 2". Ne montre pas ton cheminement.
        - INTERDICTION de s'excuser. Ne dis JAMAIS "Je suis désolé".
        - INTERDICTION de donner un nom de médicament ou une dose.
        - INTERDICTION de dire "Je ne peux pas faire de diagnostic" (propose des pistes à la place).

    Message : {message}
    """

    try:
        message_envoye = await requete(prompt)
        create_message_cache(message, interaction.channel.id)
        await interaction.followup.send(content=message_envoye)

    except Exception as e:
        print("Erreur:", e)
        await interaction.followup.send("Erreur lors de la génération de votre réponse ...")

client.run(os.getenv("TOKEN"))