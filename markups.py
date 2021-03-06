from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton('๐ ๐ฉ๐ซ๐จ๐๐ข๐ฅ๐')
btnSub = KeyboardButton('๐ ๐ฌ๐ฎ๐๐ฌ๐๐ซ๐ข๐ฉ๐ญ๐ข๐จ๐ง')
btnChk = KeyboardButton('๐ณ ๐๐ก๐๐๐ค')

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
mainMenu.add(btnProfile, btnSub, btnChk)

btnSubDay = InlineKeyboardButton(text="๐คจ ๐๐๐ ๐๐๐ 1 ๐๐๐ข", callback_data="subday")
btnSubWeek = InlineKeyboardButton(text="๐ผ ๐๐๐ ๐๐๐ 7 ๐๐๐ข๐", callback_data="subweek")
btnSubMonth = InlineKeyboardButton(text="๐ฅต ๐๐๐ ๐๐๐ 30 ๐๐๐ข๐", callback_data="submonth")
submenu = InlineKeyboardMarkup(row_width=1)
submenu.add(btnSubDay)
submenu.add(btnSubWeek)
submenu.add(btnSubMonth)



def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIWI = InlineKeyboardButton(text="๐๐๐๐ ๐๐๐ ๐๐๐ข", url=url)
        qiwiMenu.insert(btnUrlQIWI)

    btnCheckQIWI = InlineKeyboardButton(text="๐๐๐๐๐ ๐๐๐ข", callback_data="check_" + bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu
