import random
import string
import time
from discord_webhook import DiscordWebhook

WEBHOOK = "DISCORD.COM/WEBHOOK/WHATEVERTHELINKWASIDKIFORGOTLMAOTHISISATIMEWASTERDONTACTUALLYRUNTHISANDEXPECTSOMETHINGYOUFUNKYBASEMENTDWELLERYOU"

def generateCode(length):
    # THE MAIN ACT
    letters = string.ascii_lowercase
    letters2 = string.ascii_uppercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters) + random.choice(numbers) + random.choice(letters2) for i in range(length))
    print("Generated code", "is:", "https://discord.gift/" + result_str)

    webhook = DiscordWebhook(url=WEBHOOK, content=result_str)
    response = webhook.execute()



print("HEY THERE VERY EPIC SKID MACHINE WHO HAD NOTHING TO DO ON THE 21st NIGHT OF SEPTEMBER, LEAVE THIS RUNNING FOR 8 OCTILLION YEARS FOR FREE NITRO (for legal reasons this is a joke.)")

while True:
    time.sleep(2)
    generateCode(19)

# for actually regular users, read the WEBHOOK placeholder link

