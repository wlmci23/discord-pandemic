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
            if command[1] == "reload":
                config = config_file.update_config()

        if message.author.display_name == nick:
            async for history_message in message.channel.history(limit=6):
                if history_message.author.display_name == nick:
                    await history_message.author.edit(nick=nick)

config = config_file.update_config()
client = MyClient()
client.run(config['token'])
