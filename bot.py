from textgenrnn import textgenrnn
import discord
from discord.ext import commands

textgen = textgenrnn("textgenrnn_weights.hdf5")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("p"))

# The user input is used as the prefix for generating responses, because I have no idea how to do this properly
def generate(prefix):
    return discord.utils.escape_mentions(textgen.generate(temperature=1.0, return_as_list=True, prefix=prefix+" : ")[0]).split(":")[1]

@bot.command()
async def gen(ctx, *, prompt=""):
    num=1
    if prompt.isdigit():
        num = int(prompt)
        if num>5:
            await ctx.send("Error: 5 responses at most please.")
            return
        prompt=""
    for i in range(num):
        async with ctx.channel.typing():
            result = await bot.loop.run_in_executor(None, generate, prompt)
            if len(result.strip()) == 0:
                result = "(No output)"
            await ctx.send(result)

bot.run("token")
