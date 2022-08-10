import wikipedia
from pyrogram import Client,filters
from plugins.Modukes.Wikipedia.wiki_helpers.pluginhelpers import edit_or_reply
from plugins.Modules.Wikipedia.wiki_helpers.basic_helpers import get_text

@Client.on_message(filters.command(["wiki", "Wikipedia"]))
async def wikipediasearch(Client, message):
    event = await edit_or_reply(message, "𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...🔎")
    query = get_text(message)
    if not query:
        await event.edit("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙎𝙮𝙣𝙩𝙖𝙭❌ 𝙨𝙚𝙚 𝙝𝙚𝙡𝙥 𝙢𝙚𝙣𝙪 𝙩𝙤 𝙠𝙣𝙤𝙬 𝙝𝙤𝙬 𝙩𝙤 𝙪𝙨𝙚 𝙩𝙝𝙞𝙨 𝙘𝙤𝙢𝙢𝙖𝙣𝙙")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"🌐 [{s}]({url}) \n"
        except BaseException:
            pass
    await event.edit(
        "WikiPedia Search: {} \n\n Result: \n\n{}".format(query, result),
        disable_web_page_preview=True,
    )
