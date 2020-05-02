import discord
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print('로그인 성공! {0.user}'.format(client))
    print("ready")
    game = discord.Game("!!!명령어")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    if message.content.startswith("!!!흐름끊기"):
        await message.channel.send("---킹---름---끊---기---")
    if message.content.startswith("니코니코니"):
        await message.channel.send("네다^^")
    if message.content.startswith("야"):
        await message.channel.send("뭐")
    if message.content.startswith("!!!저리가세요"):
        await message.channel.send("꺼지세요")
    if message.content.startswith("너 말고"):
        await message.channel.send("그럼 누구")
    if message.content.startswith("ㅋ"):
        await message.channel.send("?")
    if message.content.startswith("ㅋ"):
        await message.channel.send("ㅂㄷㅂㄷ")
    if message.content.startswith("ㅁㄹ"):
        await message.channel.send(".........")
    if message.content.startswith("!!!명령어"):
        await message.channel.send("https://discord.gg/umswshd")
    if message.content.startswith("나비보벳따우"):
        await message.channel.send("봇보베띠")
    if message.content.startswith("인생"):
        await message.channel.send("쓰다")
    if message.content.startswith("인정?"):
        await message.channel.send("어 인정")
    if message.content.startswith("디온봇 돈내놔"):
        await message.channel.send("저리 가")
    if message.content.startswith("마인드스톤"):
        await message.channel.send("구독과 좋아요")
    if message.content.startswith("!!!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00f00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("꺄르륵"):
        await message.channel.send("깔깔")
    if message.content.startswith("그냥 불러봤어"):
        await message.channel.send(".. ㅇ")
    if message.content.startswith("디온봇 바보"):
        await message.channel.send("흥 너랑 안놀아")
    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("ㅂㅇ")
    if message.content.startswith("ㅅㄱ"):
        await message.channel.send("......")
    if message.content.startswith("디온봇 멍청이"):
        await message.channel.send("멍멍!")
    if message.content.startswith("!!!초대"):
        await message.channel.send("https://discordapp.com/api/oauth2/authorize?client_id=702454264240406549&permissions=8&scope=bot")

    if message.content == '!!!디온 현황':
        embed = discord.Embed(color=0xff00, title="디온", description="공부 중", timestamp=message.created_at)
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

    @client.event
    async def on_message(message):
        if message.content == '!!!꿀꿀':
            embed = discord.Embed(color=00, title="꿀꾸리", description="귀여운 꿀", timestamp=message.created_at)
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        if message.content == '!!!디온 현황':
            embed = discord.Embed(color=0xff00, title="디온", description="공부 중", timestamp=message.created_at)
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
