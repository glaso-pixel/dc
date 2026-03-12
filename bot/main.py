# Main Bot File
from bot.cogs.sample_cog import SampleCog

class Bot:
    def start(self):
        print("Bot started!")

if __name__ == '__main__':
    bot = Bot()
    bot.start()
