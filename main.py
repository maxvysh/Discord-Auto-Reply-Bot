import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        if message.author == self.user:
            return

        #Type the user id that you want to send the message to, and type in your message
        if message.author.id == 'type user id':
            await message.channel.send('type your message here')

client = MyClient()
#Type your client token here
client.run('CLIENT TOKEN')