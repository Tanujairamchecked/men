import wikipedia
from pyrogram import Client,filters
from plugins.admemes.Wiki.pluginhelpers import edit_or_reply
from plugins.admemes.Wiki.basic_helpers import get_text


@Client.on_message(filters.command(["wiki", "wikipedia"]))
async def wikipediasearch(Client, message):
    event = await edit_or_reply(message, "𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...🔎")
    query = get_text(message)
    if not query:
        await event.edit("𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝚂𝚈𝙽𝚃𝙰𝚇 𝚂𝙴𝙴 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳")
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
        "𝙒𝙄𝙆𝙄𝙋𝙀𝘿𝙄𝘼 𝙎𝙀𝘼𝙍𝘾𝙃: {} \n\n Result: \n\n{}".format(query, result),
        disable_web_page_preview=True,
    )
