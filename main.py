import logging
from os import getenv
from dotenv import load_dotenv
from huepy import red
from telethon import TelegramClient, events
from funcs import get_cc, get_bin

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

client = TelegramClient("auscrap", API_ID, API_HASH)

# You can add chats here as long as your telegram account is in it
chats = [
"@BinsHellChat",
"@secretgroup01",
"@savagegroupoficial",
"@Venexchk",
"@RemChatChk",
"@ScrapperLala",
"https://t.me/+rl8ChsLqzBdkNTYx",
"@alterchkchat",
"@oficialscorpionsgrupo",
"@techzillacheckerchat",
"@kurumichat",
"@ChatA2Assiad",
"@fbinschat",
"@BinSkillerChat",
"@JohnnySinsChat",
"@leonbinerss",
"@OficialScorpionsGrupo",
"@AssociatonBinners1",
"@dSnowChat",
"@cardesclub",
"@RickPrimeChkFree",
"@savagegroupoficial",
"@CHECKEREstefany_bot",
"@CuartelCardingGrupo",
"@astachkccs",
"@bcycc",
"@MUGIWARAAC",
"@GodsOfTheBins",
"@botsakuraa",
"@ArthurChkGroup",
"@Sammy0007_Chat",
"@SkadiScrapper",
"@CCAUTH",
"@Ikaroscrapper",
"@Nasayuzakichkbot"
]

# Chat to send ccs
send_chat = "@idbuyertower"
ccs_ac = []


@client.on(events.NewMessage(chats=chats))
async def scrapper(e: events.NewMessage.Event):
    text = e.message.message
    ccs = get_cc(text)
    if not ccs:
        return

    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]
    ccf = f"{cc}|{mes}|{ano}|{cvv}"

    if ccf in ccs_ac:
        return

    print(red(f"CC FIND: {ccf}"))

    with open("ccs.txt", "a") as f:
        f.write(ccf + "\n")

    ccs_ac.append(ccf)
    bin = cc[:6]
    extra = f"{cc[:12]}xxxx|{mes}|{ano}|rnd"
    bin_data = await get_bin(bin)

    if isinstance(bin_data, bool):
        return

    if len(mes) == 1:
        mes = "0" + mes

    if len(ano) == 2:
        ano = "20" + ano

    brand = bin_data["brand"]
    country = bin_data["country"]
    country_flag = bin_data["country_flag"]
    bank = bin_data["bank"]
    level = bin_data["level"]
    card_type = bin_data["type"]

    # Text to send
    text_final = f"""
    (❀˵•́૩•̀˵)〴 NEW SCRAPPED CARD
    —————————————
        CC: {ccf}
        Brand: {brand}
        Type: {card_type}
        Level: {level}
        Bank: {bank}
        Country: {country}
        Country Flag: {country_flag}
        Extra: {extra}
    —————————————
    """

    await client.send_message(send_chat, text_final, parse_mode="html")


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
        level=logging.WARNING,
    )
    client.start()
    client.run_until_disconnected()
