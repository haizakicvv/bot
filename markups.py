from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton('🔒 𝐩𝐫𝐨𝐟𝐢𝐥𝐞')
btnSub = KeyboardButton('🔑 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧')
btnChk = KeyboardButton('💳 𝐜𝐡𝐞𝐜𝐤')

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
mainMenu.add(btnProfile, btnSub, btnChk)

btnSubDay = InlineKeyboardButton(text="🤨 𝚜𝚞𝚋 𝚏𝚘𝚛 1 𝚍𝚊𝚢", callback_data="subday")
btnSubWeek = InlineKeyboardButton(text="😼 𝚜𝚞𝚋 𝚏𝚘𝚛 7 𝚍𝚊𝚢𝚜", callback_data="subweek")
btnSubMonth = InlineKeyboardButton(text="🥵 𝚜𝚞𝚋 𝚏𝚘𝚛 30 𝚍𝚊𝚢𝚜", callback_data="submonth")
submenu = InlineKeyboardMarkup(row_width=1)
submenu.add(btnSubDay)
submenu.add(btnSubWeek)
submenu.add(btnSubMonth)



def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIWI = InlineKeyboardButton(text="𝚕𝚒𝚗𝚔 𝚏𝚘𝚛 𝚙𝚊𝚢", url=url)
        qiwiMenu.insert(btnUrlQIWI)

    btnCheckQIWI = InlineKeyboardButton(text="𝚌𝚑𝚎𝚌𝚔 𝚙𝚊𝚢", callback_data="check_" + bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu
