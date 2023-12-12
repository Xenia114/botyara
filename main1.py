import telebot
from telebot import types
import settings

bot = telebot.TeleBot(settings.TG_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>! \nНажимай на меню и выбирай, что сыграть на гитрае сегодня! \n⬇️⬇️⬇️'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['instruction'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>!!! \n\nЭтот бот создан для дотого, чтобы было удобно и быстро находить нужную песню с аккордами. \n\nБезусловно есть множество различных сайтов, но в них уж очень все разбросано и, к сожалению, от рекламы никуда не деться, а этот бот отправляет ссылку на определенную песню + в самой ссылке сразу уже написаны аккорды, чтобы если вдруг вы знаете текст, то уже просто ориентироваться на аккорды! \n\nНу и еще одно, пожулуй уточнение, это слово - <b>капо(каподастр)</b> - штучка для того чтобы зажимать струны на любом ладу, повысив при этом тональность, на которой вам будет комфортно петь!\n\nНу вот и всё!'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['razrabotchik'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("ВКонтакте", url='https://vk.com/id268740786'))
    markup.add(types.InlineKeyboardButton("Telegram", url='https://t.me/Xenia015'))
    bot.send_message(message.chat.id, "Разработчик бота:", reply_markup=markup)

@bot.message_handler(commands=['prostolera'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F177980%2Flytiki%2F" title="Просто Лера - Лютики (Em, G, C,Am капо 2)">Просто Лера - Лютики (Em, G, C,Am капо 2)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F184529%2Fmne_20%2F" title="Просто Лера - Мне 20 (Dm, E, Am, F/G, капо 2)">Просто Лера - Мне 20 (Dm, E, Am, F/G, капо 2)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F178349%2Fsvetofory%2F" title="Просто Лера - Светофоры (Dm, E, Am, F/G, капо 2)">Просто Лера - Светофоры (Dm, E, Am, F/G, капо 2)</a>', parse_mode='html')


@bot.message_handler(commands=['zemfira'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F173432%2Fbeskonechnost_s_kapodastrom%2F&cc_key=" title="Земфира - Бесконечность (E, Am, С, В7, капо 1)">Земфира - Бесконечность (E, Am, С, В7, капо 1)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F9194%2Fglavnoe%2F&cc_key=" title="Земфира - Главное">Земфира - Главное</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F184805%2Fzloy_chelovek%2F&cc_key=" title="Земфира - Злой человек ( Am, F, Е)">Земфира - Злой человек ( Am, F, Е)</a>, <a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F4833%2Fiskala%2F&cc_key=" title="Земфира - Искала (Dm, C, G, A | F, А, F, А,F, А, G, A)">Земфира - Искала (Dm, C, G, A | F, А, F, А,F, А, G, A)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F16925%2Fp_m_m_l%2F&cc_key=" title="Земфира - П М М Л (Am, G,Am, G, Dm, Em, Dm, Em)">Земфира - П М М Л (Am, G,Am, G, Dm, Em, Dm, Em)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F1337%2Fromaski%2F&cc_key=" title="Земфира - Ромашки (капо 1)">Земфира - Ромашки (капо 1)</a>' , parse_mode='html')


@bot.message_handler(commands=['makskorshz'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://akkords.pro/songs/maks-korzh/slovo-pacana/" title="Макс Корж — Слово пацана (G, Bm, Em, C)">Макс Корж — Слово пацана (G, Bm, Em, C)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaks_korzh%2F196162%2Fgory_po_koleno%2F" title="Макс Корж - Горы по колено( капо 4 лад)">Макс Корж - Горы по колено( капо 4 лад)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaks_korzh%2F110384%2Fzhit_v_kayf%2F" title="Макс Корж - Жить в кайф">Макс Корж - Жить в кайф</a>', parse_mode='html')


@bot.message_handler(commands=['pornjfilms'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fpornofilmy%2F174824%2Fya_tak_soskuchilsya%2F&cc_key=" title="Порнофильмы - Я так соскучился (Am, F, C, E)">Порнофильмы - Я так соскучился (Am, F, C, E)</a>' , parse_mode='html')


@bot.message_handler(commands=['nervs'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://amdm.ru/akkordi/nervy/175385/nervi/" title="Нервы - Нервы (F, E, Am, С, капо 2)">Нервы - Нервы (F, E, Am, С, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F168401%2Fschaste%2F&cc_key=" title="Нервы - Счастье (Em, C, G, D, капо 2)">Нервы - Счастье (Em, C, G, D, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F123817%2Fya_ne_hochu_bez_tebya_spat%2F&cc_key=" title="Нервы - Я не хочу без тебя спать (F, E, Am, С, капо 2)">Нервы - Я не хочу без тебя спать (F, E, Am, С, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F116481%2Fslishkom_vlyblyon%2F&cc_key=" title="Нервы - Слишком влюблён (Am, В7, Em, C, капо 4)">Нервы - Слишком влюблён (Am, В7, Em, C, капо 4)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F160292%2Fsamyy_dorogoy_chelovek%2F&cc_key=" title="Нервы - Самый дорогой человек (Em, C, G, D)">Нервы - Самый дорогой человек (Em, C, G, D)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F100371%2Fbatarei%2F&cc_key=" title="Нервы - Батареи (Dm, E, Am, F)">Нервы - Батареи (Dm, E, Am, F)</a>', parse_mode='html')


@bot.message_handler(commands=['nlo'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnlo%2F202384%2Ftantsy%2F&cc_key=" title="NLO - Танцы (капо 2) (Dm, Am)">NLO - Танцы (капо 2) (Dm, Am)</a>' , parse_mode='html')


@bot.message_handler(commands=['grechka'])
def p(message):
    bot.send_message(message.chat.id, f'Гречка - Люби меня, люби (Em, G, D, Am)' , parse_mode='html')


@bot.message_handler(commands=['kish'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fkorol_i_shut%2F23540%2Fkukla_kolduna%2F&cc_key=" title="Король и Шут - Кукла колдуна (Dm, F, Gm, A, припев Dm, Gm, A)">Король и Шут - Кукла колдуна (Dm, F, Gm, A, припев Dm, Gm, A)</a>' , parse_mode='html')


@bot.message_handler(commands=['ddt'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fddt%2F92536%2Feto_vsyo%2F&cc_key=" title="ДДТ - Это всё (G, D/F, Em, C, D)">ДДТ - Это всё (G, D/F, Em, C, D)</a>' , parse_mode='html')


@bot.message_handler(commands=['zveri'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzveri%2F23675%2Frayoni_kvartali%2F&cc_key=" title="Звери - Районы-кварталы (Am, Dm. E, Am)">Звери - Районы-кварталы (Am, Dm. E, Am)</a>' , parse_mode='html')


@bot.message_handler(commands=['basta'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fbasta%2F159838%2Fvipusknoy_medlyachok%2F&cc_key=" title="Баста - Выпускной (Медлячок) (Am, F, G, Em, F, Dm, E, Am)">Баста - Выпускной (Медлячок) (Am, F, G, Em, F, Dm, E, Am)</a>' , parse_mode='html')


@bot.message_handler(commands=['strikalo'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')


@bot.message_handler(commands=['skriptonit'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fskriptonit%2F139809%2Feto_lybov%2F&cc_key=" title="Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)">Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)</a>', parse_mode='html')


@bot.message_handler(commands=['maksim'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaksim%2F101853%2Fznaesh_li_ti%2F&cc_key=" title="МакSим - Знаешь ли ты ( капо 5 лад)">МакSим - Знаешь ли ты ( капо 5 лад)</a>', parse_mode='html')


@bot.message_handler(commands=['ssshhhiiiitt'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fssshhhiiittt%2F188406%2Fnadezhda%2F&cc_key=" title="Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))">Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))</a>', parse_mode='html')


@bot.message_handler(commands=['5nizza'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2F5nizza%2F99457%2Fya_soldat%2F&cc_key=" title="5nizza - Я солдат (Em, Am, Em, B7)">5nizza - Я солдат (Em, Am, Em, B7)</a>' , parse_mode='html')


@bot.message_handler(commands=['sektorgaza'])
def p(message):
    bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fsektor_gaza%2F24057%2Flirika%2F&cc_key=" title="Сектор газа - лирика (Am, G, Dm, C)">Сектор газа - лирика (Am, G, Dm, C)</a>' , parse_mode='html')


@bot.message_handler(commands=['annaasti'])
def p(message):
    bot.send_message(message.chat.id, '<a href="https://amdm.ru/akkordi/anna_asti/199766/povelo/" title="ANNA ASTI - Повело (Dm, E, Am, F, капо 4)">ANNA ASTI - Повело (Dm, E, Am, F, капо 4)</a>\n<a href="https://amdm.ru/akkordi/anna_asti/194458/po_baram/" title="ANNA ASTI - По барам (Am, F, Dm, E, капо 2)">ANNA ASTI - По барам (Am, F, Dm, E, капо 2)</a>', parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if "Просто Лера" in message.text.lower() or "просто лера" in message.text.lower() or "лера" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F177980%2Flytiki%2F" title="Просто Лера - Лютики (Em, G, C,Am капо 2)">Просто Лера - Лютики (Em, G, C,Am капо 2)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F184529%2Fmne_20%2F" title="Просто Лера - Мне 20 (Dm, E, Am, F/G, капо 2)">Просто Лера - Мне 20 (Dm, E, Am, F/G, капо 2)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fprosto_lera%2F178349%2Fsvetofory%2F" title="Просто Лера - Светофоры (Dm, E, Am, F/G, капо 2)">Просто Лера - Светофоры (Dm, E, Am, F/G, капо 2)</a>', parse_mode='html')
    elif "корж" in message.text.lower() or "Корж" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://akkords.pro/songs/maks-korzh/slovo-pacana/" title="Макс Корж — Слово пацана (G, Bm, Em, C)">Макс Корж — Слово пацана (G, Bm, Em, C)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaks_korzh%2F196162%2Fgory_po_koleno%2F" title="Макс Корж - Горы по колено( капо 4 лад)">Макс Корж - Горы по колено( капо 4 лад)</a>\n<a href="https://vk.com/away.php?utf=1&to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaks_korzh%2F110384%2Fzhit_v_kayf%2F" title="Макс Корж - Жить в кайф">Макс Корж - Жить в кайф</a>', parse_mode='html')
    elif "нервы" in message.text.lower() or "ythds" in message.text.lower() or "Нервы" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://amdm.ru/akkordi/nervy/175385/nervi/" title="Нервы - Нервы (F, E, Am, С, капо 2)">Нервы - Нервы (F, E, Am, С, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F168401%2Fschaste%2F&cc_key=" title="Нервы - Счастье (Em, C, G, D, капо 2)">Нервы - Счастье (Em, C, G, D, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F123817%2Fya_ne_hochu_bez_tebya_spat%2F&cc_key=" title="Нервы - Я не хочу без тебя спать (F, E, Am, С, капо 2)">Нервы - Я не хочу без тебя спать (F, E, Am, С, капо 2)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F116481%2Fslishkom_vlyblyon%2F&cc_key=" title="Нервы - Слишком влюблён (Am, В7, Em, C, капо 4)">Нервы - Слишком влюблён (Am, В7, Em, C, капо 4)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F160292%2Fsamyy_dorogoy_chelovek%2F&cc_key=" title="Нервы - Самый дорогой человек (Em, C, G, D)">Нервы - Самый дорогой человек (Em, C, G, D)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnervy%2F100371%2Fbatarei%2F&cc_key=" title="Нервы - Батареи (Dm, E, Am, F)">Нервы - Батареи (Dm, E, Am, F)</a>', parse_mode='html')

    elif "Земфира" in message.text.lower() or "земфира" in message.text.lower() or "ptvabhf" in message.text.lower():
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F173432%2Fbeskonechnost_s_kapodastrom%2F&cc_key=" title="Земфира - Бесконечность (E, Am, С, В7, капо 1)">Земфира - Бесконечность (E, Am, С, В7, капо 1)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F9194%2Fglavnoe%2F&cc_key=" title="Земфира - Главное">Земфира - Главное</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F184805%2Fzloy_chelovek%2F&cc_key=" title="Земфира - Злой человек ( Am, F, Е)">Земфира - Злой человек ( Am, F, Е)</a>, <a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F4833%2Fiskala%2F&cc_key=" title="Земфира - Искала (Dm, C, G, A | F, А, F, А,F, А, G, A)">Земфира - Искала (Dm, C, G, A | F, А, F, А,F, А, G, A)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F16925%2Fp_m_m_l%2F&cc_key=" title="Земфира - П М М Л (Am, G,Am, G, Dm, Em, Dm, Em)">Земфира - П М М Л (Am, G,Am, G, Dm, Em, Dm, Em)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzemfira%2F1337%2Fromaski%2F&cc_key=" title="Земфира - Ромашки (капо 1)">Земфира - Ромашки (капо 1)</a>' , parse_mode='html')

    elif "танцы" in message.text.lower() or "Танцы" in message.text.lower() or 'nfyws' in message.text.lower() or 'Nfyws'in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Ftantsy_minus%2F4868%2Fpolovinka%2F&cc_key=" title="Танцы Минус - Половинка(У ночного огня под) (Em, C, G, B)">Танцы Минус - Половинка(У ночного огня под) (Em, C, G, B)</a>\n<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fnlo%2F202384%2Ftantsy%2F&cc_key=" title="NLO - Танцы (капо 2) (Dm, Am)">NLO - Танцы (капо 2) (Dm, Am)</a>' , parse_mode='html')
    elif "У ночного огня" in message.text.lower() or "у ночного огня" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Ftantsy_minus%2F4868%2Fpolovinka%2F&cc_key=" title="Танцы Минус - Половинка(У ночного огня под) (Em, C, G, B)">Танцы Минус - Половинка(У ночного огня под) (Em, C, G, B)</a>', parse_mode='html')
    elif "Гречка" in message.text.lower() or "гречка" in message.text.lower() or 'uhtxrf' in message.text.lower() or 'Uhtxrf' in message.text.lower():
        bot.send_message(message.chat.id, f'Гречка - Люби меня, люби (Em, G, D, Am)' , parse_mode='html')
    elif "лирика" in message.text.lower() or "Лирика" in message.text.lower() or 'kbhbrf' in message.text.lower() or 'Kbhbrf' in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fsektor_gaza%2F24057%2Flirika%2F&cc_key=" title="Сектор газа - лирика (Am, G, Dm, C)">Сектор газа - лирика (Am, G, Dm, C)</a>' , parse_mode='html')
    elif "Я солдат" in message.text.lower() or "я солдат" in message.text.lower() or 'z cjklfn' in message.text.lower() or 'Z cjklfn' in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2F5nizza%2F99457%2Fya_soldat%2F&cc_key=" title="5nizza - Я солдат (Em, Am, Em, B7)">5nizza - Я солдат (Em, Am, Em, B7)</a>' , parse_mode='html')
    elif "Кукла колдуна" in message.text.lower() or "кукла колдуна" in message.text.lower() or 'rerkf rjkleyf' in message.text.lower() or 'Rerkf rjkleyf' in message.text.lower() or "киш"  in message.text.lower() or "КиШ" in message.text.lower() or 'rbi' in message.text.lower() or 'RbI' in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fkorol_i_shut%2F23540%2Fkukla_kolduna%2F&cc_key=" title="Король и Шут - Кукла колдуна (Dm, F, Gm, A, припев Dm, Gm, A)">Король и Шут - Кукла колдуна (Dm, F, Gm, A, припев Dm, Gm, A)</a>' , parse_mode='html')
    elif "ДДТ" in message.text.lower() or "ддт" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fddt%2F92536%2Feto_vsyo%2F&cc_key=" title="ДДТ - Это всё (G, D/F, Em, C, D)">ДДТ - Это всё (G, D/F, Em, C, D)</a>' , parse_mode='html')
    elif message.text == "это всё":
        bot.send_message(message.chat.id,
                         f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fddt%2F92536%2Feto_vsyo%2F&cc_key=" title="ДДТ - Это всё (G, D/F, Em, C, D)">ДДТ - Это всё (G, D/F, Em, C, D)</a>',
                         parse_mode='html')
    elif message.text == "это все":
        bot.send_message(message.chat.id,
                         f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fddt%2F92536%2Feto_vsyo%2F&cc_key=" title="ДДТ - Это всё (G, D/F, Em, C, D)">ДДТ - Это всё (G, D/F, Em, C, D)</a>',
                         parse_mode='html')
    elif "Звери" in message.text.lower() or "Районы кварталы" in message.text.lower() or "районы кварталы" in message.text.lower() or "кварталы" in message.text.lower() or "районы" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fzveri%2F23675%2Frayoni_kvartali%2F&cc_key=" title="Звери - Районы-кварталы (Am, Dm. E, Am)">Звери - Районы-кварталы (Am, Dm. E, Am)</a>' , parse_mode='html')
    elif "Порнофильмы Я так соскучился" in message.text.lower() or "Я так соскучился" in message.text.lower() or "Порнофильмы" in message.text.lower() or "порнофильмы" in message.text.lower() or "я так соскучился" in message.text.lower() :
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fpornofilmy%2F174824%2Fya_tak_soskuchilsya%2F&cc_key=" title="Порнофильмы - Я так соскучился (Am, F, C, E)">Порнофильмы - Я так соскучился (Am, F, C, E)</a>' , parse_mode='html')
    elif "дайте мне" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fpornofilmy%2F174824%2Fya_tak_soskuchilsya%2F&cc_key=" title="Порнофильмы - Я так соскучился (Am, F, C, E)">Порнофильмы - Я так соскучился (Am, F, C, E)</a>' , parse_mode='html')

    elif "медлячок" in message.text.lower() or "Баста выпускной" in message.text.lower() or "Выпускной" in message.text.lower() or "выпускной" in message.text.lower() or "Медлячок" in message.text.lower():
        bot.send_message(message.chat.id, f'<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fbasta%2F159838%2Fvipusknoy_medlyachok%2F&cc_key=" title="Баста - Выпускной (Медлячок) (Am, F, G, Em, F, Dm, E, Am)">Баста - Выпускной (Медлячок) (Am, F, G, Em, F, Dm, E, Am)</a>' , parse_mode='html')
    elif message.text == "Яхта, парус":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "яхта, парус":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "яхта парус":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "яхта":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "парус":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "наше лето":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "Наше лето":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fvalentin_strykalo%2F97637%2Fyahta_parus%2F&cc_key=" title="Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)">Валентин Стрыкало - Яхта, парус (Am, F, Dm, E)</a>', parse_mode='html')
    elif message.text == "Скриптонит это любовь":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fskriptonit%2F139809%2Feto_lybov%2F&cc_key=" title="Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)">Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)</a>', parse_mode='html')
    elif message.text == "Это любовь":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fskriptonit%2F139809%2Feto_lybov%2F&cc_key=" title="Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)">Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)</a>', parse_mode='html')
    elif message.text == "это любовь":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fskriptonit%2F139809%2Feto_lybov%2F&cc_key=" title="Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)">Скриптонит - Это любовь (Am, C,Am, C,Am, C, F, C, G, Am)</a>', parse_mode='html')
    elif message.text == "Амега Лететь":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Famega%2F138922%2Fletet%2F&cc_key=" title="Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))">Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))</a>', parse_mode='html')
    elif message.text == "Лететь":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Famega%2F138922%2Fletet%2F&cc_key=" title="Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))">Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))</a>', parse_mode='html')
    elif "однажды он сказал" in message.text.lower():
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Famega%2F138922%2Fletet%2F&cc_key=" title="Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))">Амега - Лететь (Am, Em, D, C, капо 3 лад(однажды он сказал))</a>', parse_mode='html')
    elif "Знаешь ли ты" in message.text.lower():
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaksim%2F101853%2Fznaesh_li_ti%2F&cc_key=" title="МакSим - Знаешь ли ты ( капо 5 лад)">МакSим - Знаешь ли ты ( капо 5 лад)</a>', parse_mode='html')
    elif "знаешь ли ты" in message.text.lower():
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaksim%2F101853%2Fznaesh_li_ti%2F&cc_key=" title="МакSим - Знаешь ли ты ( капо 5 лад)">МакSим - Знаешь ли ты ( капо 5 лад)</a>', parse_mode='html')
    elif message.text == "Максим":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fmaksim%2F101853%2Fznaesh_li_ti%2F&cc_key=" title="МакSим - Знаешь ли ты ( капо 5 лад)">МакSим - Знаешь ли ты ( капо 5 лад)</a>', parse_mode='html')
    elif message.text == "бесконечно курим":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fssshhhiiittt%2F188406%2Fnadezhda%2F&cc_key=" title="Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))">Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))</a>', parse_mode='html')
    elif message.text == "Бесконечно курим":
        bot.send_message(message.chat.id, '<a href="https://vk.com/away.php?to=https%3A%2F%2Famdm.ru%2Fakkordi%2Fssshhhiiittt%2F188406%2Fnadezhda%2F&cc_key=" title="Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))">Ssshhhiiittt! - Надежда (Em, D, C, Em, Bm( бесконечно курим))</a>', parse_mode='html')
    elif "Anna Asti" in message.text.lower() or 'ANNA ASTI' in message.text.lower() or 'Asti' in message.text.lower() or 'anna asti' in message.text.lower() or 'Анна Асти' in message.text.lower() or 'анна асти' in message.text.lower() or 'асти' in message.text.lower() or 'Асти' in message.text.lower():
        bot.send_message(message.chat.id,
                         '<a href="https://amdm.ru/akkordi/anna_asti/199766/povelo/" title="ANNA ASTI - Повело (Dm, E, Am, F, капо 4)">ANNA ASTI - Повело (Dm, E, Am, F, капо 4)</a>\n<a href="https://amdm.ru/akkordi/anna_asti/194458/po_baram/" title="ANNA ASTI - По барам (Am, F, Dm, E, капо 2)">ANNA ASTI - По барам (Am, F, Dm, E, капо 2)</a>',
                         parse_mode='html')

    elif message.text == "вк":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ВКонтакте", url='https://vk.com/id268740786'))
        markup.add(types.InlineKeyboardButton("Telegram", url='https://t.me/Xenia015'))
        bot.send_message(message.chat.id, "Разработчик бота:", reply_markup=markup)
    elif 'разработчик' in message.text.lower() or 'разрабы'in message.text.lower() or 'кто создал' in message.text.lower() or 'создатель' in message.text.lower() or "разраб" in message.text.lower() or "Разраб" in message.text.lower() or "Автор" in message.text.lower() or "автор" in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ВКонтакте", url='https://vk.com/id268740786'))
        markup.add(types.InlineKeyboardButton("Telegram", url='https://t.me/Xenia015'))
        bot.send_message(message.chat.id, "Разработчик бота:", reply_markup=markup)
    elif message.text == "Вк":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ВКонтакте", url='https://vk.com/id268740786'))
        markup.add(types.InlineKeyboardButton("Telegram", url='https://t.me/Xenia015'))
        bot.send_message(message.chat.id, "Разработчик бота:", reply_markup=markup)
    elif "привет" in message.text.lower() or 'Привет' in message.text.lower() or 'ghbdtn' in message.text.lower() or 'Ghbdtn' in message.text.lower() or "привеи" in message.text.lower() or "Привеи" in message.text.lower() or 'Здравствуйте' in message.text.lower() or "здравствуйте" in message.text.lower() or 'plhfdcndeqnt' in message.text.lower() or 'Plhfdcndeqnt' in message.text.lower():
        bot.send_message(message.chat.id, 'О, здорово, что написал и тебя приветствую!))', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Нажимай на меню и выбирай, что сыграть на гитрае сегодня! \n⬇️⬇️⬇️', parse_mode='html')



bot.polling(none_stop=True)