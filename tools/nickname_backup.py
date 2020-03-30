import argparse
import discord
import sys
import json

class MyClient(discord.Client):
    async def on_ready(self):
        data = {}

        guild = self.get_guild(args.guild_id)
        for member in guild.members:
            data[member.id] = member.display_name

        with open(args.output, "w") as output_file:
            output_file.write(json.dumps(data))

        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("guild_id", help="ID of the guild that owns the desired emojis", type=int)
    parser.add_argument("token", help="Bot Token to access Discord API", type=str)
    parser.add_argument("output", help="File to store the nickname backup", type=str)
    args = parser.parse_args()

    client = MyClient()
    client.run(args.token)
