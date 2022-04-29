from vkwave.bots import Keyboard, ButtonColor

# menu
MENU_KB = Keyboard()
MENU_KB.add_text_button(text="Пройти тест!", payload={"test": "-1"}, color=ButtonColor.POSITIVE)

# TEST Questions
INPUT_NAME_TEXT = "Пожалуйста, введите имя:"

# 1
WHAT_ENGINEER_ARE_YOU = "Кто ты из инженеров?"
WHAT_ENGINEER_ARE_YOU_KB = Keyboard()
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Маск", payload={"q": "Маск", "test": "0"}, color=ButtonColor.PRIMARY)
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Рогозин", payload={"q": "Рогозин", "test": "0"}, color=ButtonColor.PRIMARY)
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Тесла", payload={"q": "Тесла", "test": "0"}, color=ButtonColor.PRIMARY)
WHAT_ENGINEER_ARE_YOU_KB.add_row()
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Кулибин", payload={"q": "Кулибин", "test": "0"}, color=ButtonColor.PRIMARY)
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Калашников", payload={"q": "Калашников", "test": "0"}, color=ButtonColor.PRIMARY)
WHAT_ENGINEER_ARE_YOU_KB.add_text_button(text="Кондратюк", payload={"q": "Кондратюк", "test": "0"}, color=ButtonColor.PRIMARY)

# 2
PROG_LANG = "Какой ЯП нравится?"
PROG_LANG_KB = Keyboard()
PROG_LANG_KB.add_text_button(text="Python", payload={"q": "Python", "test": "1"}, color=ButtonColor.PRIMARY)
PROG_LANG_KB.add_text_button(text="Pascal", payload={"q": "Pascal", "test": "1"}, color=ButtonColor.PRIMARY)
PROG_LANG_KB.add_text_button(text="C/C++", payload={"q": "ccpp", "test": "1"}, color=ButtonColor.PRIMARY)
PROG_LANG_KB.add_row()
PROG_LANG_KB.add_text_button(text="JS", payload={"q": "JS", "test": "1"}, color=ButtonColor.PRIMARY)
PROG_LANG_KB.add_text_button(text="HTML+CSS", payload={"q": "HTMLCSS", "test": "1"}, color=ButtonColor.PRIMARY)
PROG_LANG_KB.add_text_button(text="Haskel", payload={"q": "Haskel", "test": "1"}, color=ButtonColor.PRIMARY)

# 3
FAV_THEME = "Какой предмет нравится?"
FAV_THEME_KB = Keyboard()
FAV_THEME_KB.add_text_button(text="Матеша", payload={"q": "Матеша", "test": "2"}, color=ButtonColor.PRIMARY)
FAV_THEME_KB.add_text_button(text="Русский/Литра", payload={"q": "русскийлитра", "test": "2"}, color=ButtonColor.PRIMARY)
FAV_THEME_KB.add_text_button(text="Инфа", payload={"q": "Инфа", "test": "0"}, color=ButtonColor.PRIMARY)
FAV_THEME_KB.add_row()
FAV_THEME_KB.add_text_button(text="Физика", payload={"q": "Физика", "test": "2"}, color=ButtonColor.PRIMARY)
FAV_THEME_KB.add_text_button(text="другое", payload={"q": "other", "test": "2"}, color=ButtonColor.PRIMARY)

# 4
EGE = "Как готовился к ЕГЭ?"
EGE_KB = Keyboard()
EGE_KB.add_text_button(text="В школе", payload={"q": "школа", "test": "3"}, color=ButtonColor.PRIMARY)
EGE_KB.add_text_button(text="online", payload={"q": "online", "test": "3"}, color=ButtonColor.PRIMARY)
EGE_KB.add_text_button(text="репетитор", payload={"q": "репетитор", "test": "3"}, color=ButtonColor.PRIMARY)
EGE_KB.add_row()
EGE_KB.add_text_button(text="Сам", payload={"q": "Сам", "test": "3"}, color=ButtonColor.PRIMARY)
EGE_KB.add_text_button(text="wtf?", payload={"q": "wtf", "test": "3"}, color=ButtonColor.PRIMARY)

# last
LAST_MESSAGE = "Спасибо, что прошел тест!"
LAST_MESSAGE_KB = Keyboard()
LAST_MESSAGE_KB.add_text_button(text="Вернуться на главную", payload={}, color=ButtonColor.POSITIVE)


questions = [
    (WHAT_ENGINEER_ARE_YOU, WHAT_ENGINEER_ARE_YOU_KB),
    (PROG_LANG, PROG_LANG_KB),
    (FAV_THEME, FAV_THEME_KB),
    (EGE, EGE_KB),
]
