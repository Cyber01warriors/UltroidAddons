#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `Get some Random Content.`

• `{i}random dog`
• `{i}random duck`
• `{i}random cat`
• `{i}random fox`
• `{i}random funfact`
"""

from . import async_searcher, ultroid_bot, eor, HNDLR

# These Api's are Collected From
# ---- https://github.com/public-apis/public-apis

API_LIST = {"cat":"https://aws.random.cat/meow", "dog":"https://random.dog/woof.json",
"duck":"https://random-d.uk/api/random","fox":"https://randomfox.ca/floof/",
"funfact":"https://asli-fun-fact-api.herokuapp.com/",
}

@ultroid_cmd(pattern="random ?(.*)")
async def random_magic(event):
   match = event.pattern_match.group(1)
   if not (match or (match not in API_LIST.keys())):
       return await eor(event, f"`Input Missing or Wrong..`\n`{HNDLR}help random`")
   text, file = None, None
   try:
       req = await async_searcher(API_LIST[match], re_json=True)
   except Exception as er:
       return await eor(event, str(er))
   if match == "cat":
       file = req["file"]
   elif match in ["dog", "duck"]:
       file = req["url"]
   elif match == "fox":
       file = req["link"]
   elif match == "funfact":
       text = req["data"]["fact"]
   await event.reply(text, file=file)
