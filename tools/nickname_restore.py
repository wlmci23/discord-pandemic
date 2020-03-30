import argparse
import discord
import sys
import json

class MyClient(discord.Client):
    async def on_ready(self):
        with open(args.input, "r") as input_file:
            data = json.loads(input_file.read())

        guild = self.get_guild(args.guild_id)
        for member_id in data:
            member = guild.get_member(int(member_id))
            if member != None and member.display_name != data[member_id]:
                await member.edit(nick=data[member_id])

        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("guild_id", help="ID of the guild that owns the desired emojis", type=int)
    parser.add_argument("token", help="Bot Token to access Discord API", type=str)
    parser.add_argument("input", help="File that stores the nickname backup", type=str)
    args = parser.parse_args()

    client = MyClient()
    client.run(args.token)
