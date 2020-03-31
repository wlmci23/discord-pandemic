import discord
import config as config_file

nick = "COVID-19 Patient"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        global config
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.guild.id != config['guild_id']:
            return

        if message.channel.id in config['excluded_channels']:
            return

        if message.content.startswith(config['prefix']):
            command = message.content[len(config['prefix']):].split()
            if command[0] == "reload":
                config = config_file.update_config()

        if message.author.display_name == nick:
            infected_count = 0
            async for history_message in message.channel.history(limit=20):
                if infected_count > 5:
                    break
                if history_message.author.display_name != nick:
                    try:
                        await history_message.author.edit(nick=nick)
                        infected_count += 1
                        print("Infected {0}!".format(history_message.author.name))
                    except discord.errors.Forbidden:
                        print("Can't infect {0}!".format(history_message.author.name))

config = config_file.update_config()
client = MyClient()
client.run(config['token'])
