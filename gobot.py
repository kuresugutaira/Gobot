# インストールした discord.py を読み込む
import discord
# エラーを記録するためのモジュールを読み込む
import logging
import random

# 自分のBotのアクセストークンに置き換える
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# エラーを読み込む
logging.basicConfig(level=logging.INFO)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await client.get_channel("(更新メッセージを送りたいチャンネルのid)").send("更新しました")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/(動物)」で動物が鳴く
    animals=[['/neko','にゃーん'],['/inu','わん'],['/ushi','もー'],
            ['/hitsuji','めええぇぇぇ'],['/buta','ぶーぶー'],['/uma','ヒヒーン'],
            ['/hiyoko','ぴよぴよ'],['/saru','ウキーッ'],['/tori','コケーっ'],
            ['/zou','ぱおーん']]
    for i in range(len(animals)) :
        if message.content == animals[i][0] :
            await message.channel.send(animals[i][1])
            break
    # 「words[0]」で「words[1]」が返される
    words=[['あ','いうえお'],['ほめて','よく頑張ったね!!えらいぞ!']]
    for i in range(len(words)) :
        if message.content == words[i][0] :
            await message.channel.send(words[i][1])
            break
    # 「greeting[0]」で「greeting[1]+(名前)+greeting[2]」が返される
    greeting=[['おはよう','おはようございます','さん'],['こんにちは','こんにちは','さん'],
             ['こんばんは','こんばんは','さん']]
    for i in range(len(greeting)) :
        if message.content == greeting[i][0] :
            msg = greeting[i][1] + message.author.mention + greeting[i][2]
            await message.channel.send(msg)
    # 「em (絵文字の名前)」でその名前の絵文字が返される
    if message.content[0:3] == 'em ' :
        emName = message.content[3:len(message.content)]
        ems = discord.utils.get(client.emojis, name = emName)
        await message.channel.send(ems)
        await message.delete()
    # 「images[0]」でimages[1]のチャンネルの画像をランダムに1枚表示する
    images=[['ピカチュウ','画像を取得する先のチャンネルのidをここにはる'],['コウペンちゃん','画像を取得する先のチャンネルのidをここにはる'],]
    for i in range(len(images)):
        if message.content == images[i][0] :
            msgs = await client.get_channel(images[i][1]).history(limit=100).flatten()
            await message.channel.send(random.choice(msgs).attachments[0].proxy_url)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)