@bot.command()
async def upload_file(ctx):
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    print(file_request.content)