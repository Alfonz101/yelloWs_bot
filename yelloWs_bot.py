from discord.ext import commands
import uuid
from PIL import Image

# Code stolen from several sources, however it took me a good while to get everything to work properly lmao

client = commands.Bot(command_prefix='.')
TOKEN = "" # DON'T FORGET TO ENTER 


@client.event
async def on_ready():
    print("We are good to go!")


@client.command()
async def save(ctx):                   # Use '.save' along with desired attachment to save image
    try:                               # Expecting an attachment, mainly images, GIFs are also saved as a '.png', but
        ctx.message.attachments[0]     # only the first frame, videos and '.exe' display an error. Other file types
    except IndexError:                 # haven't been tested, probably same outcome as with videos etc..
        print("Error: No attachment!")
        await ctx.send("No attachments detected! Links do not work!")   # No attachment will result in an error message.
    else:
        username = ctx.message.author
        image_name = str(username) + "_" + str(uuid.uuid4()) + '.png'  # Saved images names begin with the senders
        await ctx.message.attachments[0].save(image_name)              # username and ID. (more organization?)
        print("Image saved: " + image_name)
        await ctx.send("Image saved!")

        # Enter the default saving path here. Must be in following format: r"C:\\xxx\\xxx\\xxx\\" + image_name
        file = r"C:\\Users\\rober\\PycharmProjects\\discord_to_printer\\" + image_name
        image = Image.open(file)
        # Enter your desired saving path here. Must be in the same aforementioned format.
        image.save(r"C:\\Users\\rober\\Documents\\Python\\pics\\" + image_name)


client.run(TOKEN)
