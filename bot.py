import discord
from discord.ext import commands
import asyncio

intents = discord.Intents().all()
client = commands.Bot(command_prefix = "!jp ",  intents=intents, case_insensitive=True)

@client.event
async def on_ready():
    print("Bot is running!")

@client.event
async def on_guild_join(guild):
    category = client.get_channel(1071585841639604384)
    BEST_CHANNEL = await category.create_text_channel('japleaderboards')
    await BEST_CHANNEL.set_permissions(BEST_CHANNEL.guild.default_role, view_channel=False, add_reactions=False, send_messages=False)
    role = guild.get_role(1072450130965438594)
    await BEST_CHANNEL.set_permissions(role, view_channel=True, add_reactions=True, send_messages=False)

@client.command()
async def startgame(ctx):
    category = client.get_channel(1071585841639604384)
    user = str(ctx.author.display_name)
    guild = ctx.guild
    cn = user + "s test room"
    new_channel = await category.create_text_channel(name=cn)
    channel_id = new_channel.id
    await ctx.send(f"<#{channel_id}> and wait for about **__5__** seconds")
    await new_channel.set_permissions(new_channel.guild.default_role, view_channel=False, add_reactions=False)
    await new_channel.set_permissions(ctx.author, view_channel=True, send_messages=False)
    await asyncio.sleep(5)
    if ctx.message.author.id == ctx.author.id:
        await ctx.message.delete()
    def check(message):
        return message.author == client.user
    await ctx.channel.purge(limit=1, check=check)
    import random
    
    hiragana = {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
        "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
        "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
        "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
        "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
        "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
        "や": "ya", "ゆ": "yu", "よ": "yo",
        "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
        "わ": "wa", "を": "wo", "ん": "n"}
    Dakuten_Hira = {
        "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
        "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
        "だ": "da", "ぢ": ["di", "ji"], "づ": ["zu", "du"], "で": "de", "ど": "do",
        "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
        "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"}
    Combination_Hira = {
        "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
        "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
        "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
        "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",
        "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
        "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
        "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo",
        "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",
        "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
        "ぢゃ": ["da", "ja"], "ぢゅ": ["du", "ju"], "ぢょ": ["do", "jo"],
        "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
        "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo",}
    katakana = {
        "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
        "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
        "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
        "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
        "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
        "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
        "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
        "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
        "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
        "ワ": "wa", "ヲ": "wo", "ン": "n",}
    Dakuten_Kata = {
        "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
        "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
        "ダ": "da", "ヂ": ["di", "ji"], "ヅ": ["zu", "du"], "デ": "de", "ド": "do",
        "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
        "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",}
    Combination_Kata = {
        "キャ": "kya", "キュ": "kyu", "キョ": "kyo",
        "シャ": "sha", "シュ": "shu", "ショ": "sho",
        "チャ": "cha", "チュ": "chu", "チョ": "cho",
        "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
        "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo",
        "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
        "リャ": "rya", "リュ": "ryu", "リョ": "ryo",
        "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
        "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
        "ヂャ": ["da", "ja"], "ヂュ": ["du", "ju"], "ヂョ": ["do", "jo"],
        "ビャ": "bya", "ビュ": "byu", "ビョ": "byo",
        "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo",}
    Days = {
        "月ようび": ["getsuyoubi", "monday"],
        "火ようび": ["kayoubi", "tuesday"],
        "水ようび": ["suiyoubi", "wednesday"],
        "木ようび": ["mokuyoubi", "thursday"],
        "金ようび": ["kinyoubi", "friday"],
        "土ようび": ["doyoubi", "saturday"],
        "日ようび": ["nichiyoubi", "sunday"]}
    Kanji = {
        "学校": ["school", "gakkou"],
        "年生": ["year", "grade", "nensei"],
        "先生": ["teacher", "teach", "sensei"],
        "時": ["time", "hour", "ji"],
        "半": ["half", "30minutes", "30 minutes", "han"],
        "分": ["fun", "pun", "minutes", "minute"], 
        "十六": ["jyuroku", "juroku", "16", "１６"],
        "学生": ["gakusei", "gaksei", "student"]}
    game = {}
    tests = [
        ("Hiragana", hiragana),
        ("Dakuten/Handakuten Hiragana", Dakuten_Hira),
        ("Combination Hiragana", Combination_Hira),
        ("Katakana", katakana),
        ("Dakuten/Handakuten Katakana", Dakuten_Kata),
        ("Combination Katakana", Combination_Kata),
        ("Days of the week", Days),
        ("Kanji", Kanji)]
    selected = ''

    for test, data in tests:
        embed = discord.Embed(title="Choose whether to take the test or not and be patient while it changes or add reactions!", color=discord.Color.blue())
        embed.add_field(name='Would you like to test yourself in ' + test, value="Yes: ✅ | No: ❌", inline=False)
        message = await new_channel.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
        def reaction_check(reaction, user):
            return user != client.user and reaction.message.id == message.id and reaction.emoji in ['✅', '❌']

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
        except asyncio.TimeoutError:
            await new_channel.send("Timed out. Please try again.")
        else:
            if reaction.emoji == '✅':
                game.update(data)
                selected = selected + ", " + test
            elif reaction.emoji == '❌':
                await new_channel.send(f'{test} not selected!')
        await message.channel.purge(limit=2)

    await new_channel.send(f'You are going to be tested in {selected}')
    await new_channel.send('Test will start in 3 seconds, PS: do not send any other messages other than the answer!')
    await asyncio.sleep(3)
    await new_channel.set_permissions(ctx.author, send_messages=True, view_channel=True)

    keys = list(game.keys())
    random.shuffle(keys)
    q = len(game) - (len(game)-1)
    score = 0
    
    await new_channel.send(f'``` There are {len(game)} total Questions! ```')

    for key in keys:
        answer = game[key]
        await new_channel.send(f''' Question {q}!
        What is **{key}**?
        Answer: ''')
        def check(msg):
            return msg.author == ctx.author and msg.channel == new_channel
    
        user_msg = await client.wait_for('message', check=check)
        user_answer = user_msg.content.strip().lower()
        await new_channel.send(f'Your answer was **__*{user_answer.upper()}*__** and it is...')

        if user_answer in answer:
            await new_channel.send('Correct!')
            score += 1
        else:
            await new_channel.send(f"Incorrect! The correct answer is __{str(answer).upper()}__.")
        q = q + 1
    await new_channel.send(f"Your final score is ***{score}*** out of __{len(game)}__.")
    await new_channel.set_permissions(ctx.author, send_messages=False, view_channel=True)
    await new_channel.send('This channel will be deleted in 10 seconds!')
    await asyncio.sleep(10)
    await new_channel.delete()

    import datetime
    current_time = datetime.datetime.now()
    ctime = current_time.strftime("%Y-%m-%d %H:%M:%S")
    leaderboard = discord.utils.get(guild.channels, name='japleaderboards')
    await leaderboard.send(f"<@{ctx.author.id}>'s score was __**{score}**__ out of **__{len(game)}__**! recorded at __{ctime}__")
    await leaderboard.send(f'They took the tests: __**{selected}**__')
    await leaderboard.send('** **')
    private_scoring = await client.fetch_channel('1093505787218907286')
    await private_scoring.send(f"<@{ctx.author.id}>'s score was __**{score}**__ out of **__{len(game)}__**! recorded at __{ctime}__")
    await private_scoring.send(f'They took the tests: __**{selected}**__')
    await private_scoring.send('** **')



client.run('MTA5MzQ1MDkwMzQwNDY4MzI2NA.GNQ1Ek.q0k_fyaCmdRsTAFlZkAr1nVWDB-qwS47YQW4MY')