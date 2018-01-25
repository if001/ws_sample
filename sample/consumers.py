from channels import Group

# WS が繋がってきたら sample というグループに参加させる
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("sample").add(message.reply_channel)


# WS が切れたら sample というグループから外させる
def ws_disconnect(message):
    Group("sample").discard(message.reply_channel)
