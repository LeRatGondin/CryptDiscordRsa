import datetime
import requests
import base64
import discord
from colorama import Fore
import pyXor
import aioconsole
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from discord.ext import (
    commands,
)

token = "TokenIci"

CryptBot = discord.Client()
CryptBot = commands.Bot(
    description='CryptBot',
    command_prefix='-',
    self_bot=True,
)

CryptBot.remove_command('help')


@CryptBot.event
async def on_message_edit(before, after):
    await CryptBot.process_commands(after)


@CryptBot.event
async def on_message(message):
    if message.content.startswith("@Enc:"):
        if message.author.id != CryptBot.user.id:
            time = datetime.datetime.now().strftime("%H:%M")
            with open('RsaEncryptedKey/private.pem', 'r') as fk:
                priv = fk.read()
                key = RSA.importKey(pyXor.XorDecode(MdpRsa, priv))
                cipher = PKCS1_OAEP.new(key)
                mes = base64.b64decode(message.content[4:])
                x = cipher.decrypt(mes)
                mes = x.decode('ascii')
                print(
                    f'{Fore.CYAN}[{time} - {message.author}] : {Fore.RESET}{mes}')

    await CryptBot.process_commands(message)


@CryptBot.command()
async def help(ctx):
    message = """> ```ansi
> Help
> ``````ansi
> Crypt[34mBot``````ansi
> -createkey               » Crée une clé Rsa (mot de passe requis dans la console)
> -exportkey               » Envoie une commande permettant à l'autre utilisateur de l'enregistrer
> -importkey [key]         » Sert a importer la clé publique de l'autre utilisateur
> -rsastart [ping]         » Permet de commencer une discussion privée (mot de passe requis dans la console)
> 
> [36m[Crypt[34mBot[36m]```"""
    await ctx.send(message)


@CryptBot.command()
async def createkey(ctx):
    await ctx.message.delete()
    key = RSA.generate(4096)
    private = key.exportKey('PEM')
    public = key.publickey().exportKey('PEM')
    mdp = str(await aioconsole.ainput("Entrez un mot de passe : "))
    mdp2 = str(await aioconsole.ainput("Réentrez le mot de passe : "))
    while mdp != mdp2:
        print("Une erreur a été detectée veuillez réessayer")
        mdp = str(await aioconsole.ainput("Entrez un mot de passe : "))
        mdp2 = str(await aioconsole.ainput("Réentrez un mot de passe : "))
    private_encoded = pyXor.XorEncode(mdp, private.decode())
    with open('RsaEncryptedKey/private.pem', 'w') as private_rsa:
        private_rsa.write(private_encoded)
        private_rsa.close()
    with open('RsaEncryptedKey/public.pem', 'w') as public_rsa:
        public_rsa.write(public.decode())
        public_rsa.close()



@CryptBot.command()
async def exportkey(ctx):
    key = open('RsaEncryptedKey/public.pem').read()
    await ctx.send(f'\nLa commande pour importer votre clé est : \n```\n-importkey {key}```')


@CryptBot.command()
async def importkey(ctx, *, key):
    await ctx.message.delete()
    if RSA.importKey(key):
        with open('RsaEncryptedKey/public_client.pem', 'w') as kf:
            kf.write(key)
            kf.close()
    else:
        print('La clé est invalide')


@CryptBot.command()
async def rsastart(ctx, user: discord.User):
    await ctx.message.delete()

    def encode_rsa(message, key_path):
        key = RSA.importKey(open(key_path).read())
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(message)
        return ciphertext

    async def Encode(user):
        while True:
            original = await aioconsole.ainput("Entrez votre message : ")
            while original == None:
                original = await aioconsole.ainput("Entrez votre message : ")
            mes = encode_rsa(original.encode(
                'ascii', 'replace'), 'RsaEncryptedKey/public_client.pem')
            mes = base64.b64encode(mes).decode('ascii')
            user = CryptBot.get_user(user.id)
            await user.send(f'@Enc:{mes}', delete_after=1)

    async def Decode(user):
        global MdpRsa
        MdpRsa = str(await aioconsole.ainput("Entrez votre mot de passe : "))
        while MdpRsa == None:
            MdpRsa = await aioconsole.ainput("Entrez votre mot de passe : ")
        global UserRsa
        UserRsa = user
    await Decode(user)
    await Encode(user)


@CryptBot.event
async def on_connect():
    print("Ready to encrypt some messages")


def Init():
    def verif_token(token_verif): return requests.get(
        "https://discord.com/api/users/@me/guilds", headers={"authorization": token_verif}).reason == "OK"
    if verif_token(token):
        CryptBot.run(token, reconnect=True)
    else:
        print(
            f"{Fore.RED}[ERREUR] {Fore.YELLOW}Un token invalide a été entré"+Fore.RESET)
        input()


Init()
