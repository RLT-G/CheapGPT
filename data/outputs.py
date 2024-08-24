import config


answer_texts = {
    'ru': {
        'main': """
CheapGPT — полный аналог ChatGPT в Telegram, но в 6 раз дешевле!

⚡️ Всегда актуальная версия GPT-4

🦸‍♂️ Качество ответов как у ChatGPT, потому что не "оптимизируем" запросы

🗂 Поддержка файлов, ссылок, распознавания изображений и голосового ввода

💰 Цена подписки на полгода равна цене подписки на месяц в ChatGPT

🎁 5 бесплатных запросов ежедневно
""",
        'more': "Ещё",
        'referral': """
Реферальная программа
➖➖➖➖➖➖➖➖➖➖➖
🎉 Вы пригласили {} новых пользователей
💵 и получили за их расходы {}₽!

📋 Условия: 
За каждого приглашенного пользователя вы получаете 10% от всех его расходов!
Сейчас, благодаря накоплениям, вы можете пользоваться ботом, 
а в ближайшем будущем появится возможность выводить накопленные деньги!

🔗 Ваша реферальная ссылка:
`{}`
""",
        'settings': 'Настройки ИИ',
        'first_promt': '📝 Отправьте текст новых инструкций по ответу',
        'first_promt_ok': '✅ Теперь вы используете новые инструкций по ответу',
        'second_promt': '📝 Отправьте текст нового описания желаемого ответа',
        'second_promt_ok': '✅ Теперь вы используете новое описание желаемого ответа',
        'see_promts': """
📋 Текущие инструкции по ответу:

{}


📋 Текущее описание желаемого ответа:

{}
""",
        'set_default_promt': '✅ Значение промптов "Инструкции по ответу" и "Описание желаемого ответа" установлены по умолчанию',
        'info': 'Справочник',

        'token': """
⚖️ Отличие от ChatGPT
➖➖➖➖➖➖➖➖➖➖➖
CheapGPT предлагает те же функции и ответы, что и ChatGPT, но не за $20 в месяц, а всего за $2.49 при годовой подписке или $3.49 при месячной. 

💸 Таким образом, цена подписки на полгода в бот CheapGPT равна цене подписки на месяц в ChatGPT! 🚀
""",
        'settings_ai': """
📋 <b>Что такое настройки ИИ?</b>
➖➖➖➖➖➖➖➖➖➖➖
<b>Описание желаемого ответа</b> — это четкие и конкретные указания, что требуется получить в ответе. Чем точнее описание, тем более релевантный и полезный будет результат.

<b>Инструкции по ответу</b> — это набор правил и требований, которые языковая модель должна соблюдать при создании ответа. Эти инструкции помогают настроить модель на определенный стиль, формат и содержание ответа, чтобы удовлетворить запрос пользователя.
""",
        'usage_ai': """
<b>Базовое отличие</b> нашего CheapGPT от других ботов — они "оптимизируют" запросы, урезая их, что ухудшает качество ответов.  За счет такой "оптимизации" другие боты могут предлагать подписку на GPT-4o по цене ниже 8$ в месяц. 
💰 В действительности же, себестоимость одного пользователя с "чистыми" запросами к GPT-4o составляет примерно 7$ в месяц.
💡 <b>Именно из-за урезания запросов ответы от других ботов будет хуже, чем ответы от оригинального ChatGPT.</b>

📊 В тестах на производительность GPT-4o mini уступает GPT-4o в среднем всего на 4%. А оптимизация запросов к GPT-4o часто более значительно ухудшает качество ответа.

🤝 Поэтому наша команда решила развивать бота с "<b>чистыми</b>" запросами без урезаний, чтобы предоставлять ответы <b>ровно такие же как в оригинального ChatGPT.</b>
✨ В итоге, CheapGPT использует GPT-4o mini, сохраняя при этом весь функционал GPT-4o, включая обработку ссылок, файлов, изображений и голосовых команд, но по минимальной цене.
""",
        'actual_ai': """
🔄 Мы используем только самые последние версии GPT-4 и Vision.
""",
        'bot_benefit': """
KABA
""",

        'feedback_1': "🙏 Будем благодарны за обратную связь! Пока только в формате текста.",
        'feedback_2': "Благодарим за обратную связь!",
        'dialogue': "Выберите диалог",
        'inner_dialogue': """
"{}" активен
""",
        'create_new_chat': """
💬 Диалог создан, можете задавать вопросы
""",
        'change_name_1': "📝 Введите новое название диалога (до 40 символов)",
        'change_name_2': "✅ Новое название диалога успешно применено",
        'change_model': "Выберите ИИ",
        'not_money_not_limit': "🚫 Подписки нет, лимит бесплатных запросов исчерпан. Оплатите подписку для безграничных запросов.",
        'not_money': """
🚫 У вас нет подписки. 🗓 Осталось {} бесплатных запросов в сутки (с 00:00 до 23:59) для модели, но не более 10 тысяч токенов в сумме.

Подробнее о выгоде от использования бота /benefit
""",
        'wallet': """
Кошелек
➖➖➖➖➖➖➖➖➖➖➖
💳 Баланс

На кошельке: ${}.
От реферальной программы: ${}.
➖➖➖➖➖➖➖➖➖➖➖
📊 Доступные токены

GPT-4o: {} токенов.
GPT-4o mini: {} токенов.
DALL·E 3: {} генераций.
➖➖➖➖➖➖➖➖➖➖➖
💸 Зарабатывайте токены и деньги с помощью нашей <b>реферальной программы</b> /referral✨
""",
        'payment_type': 'Выберите тип оплаты',
        'del_d': '✅ Диалог успешно удален',
        'continue': 'В каком диалоге хотите продолжить?',
        'empty_history': 'История сообщений пуста',
        'not_subcribe': """
❌ <b>Подписка</b> не приобретена.

➖➖➖➖➖➖➖➖➖➖➖
💸 Зарабатывайте токены и деньги с помощью нашей реферальной программы /referral✨
""",
        'yes_subcribe': """
<b>Подписка</b>
➖➖➖➖➖➖➖➖➖➖➖
✅ Ваша <b>подписка</b> активна до {}.
"""
    },
    'en': {

    }
}

default_answer_texts = answer_texts[config.DEFAULT_LAUNGAGE]

btn_texts = {
    'ru': {
        'dialogue': '💬 Диалоги',
        'wallet': '💳 Подписка',
        'more': 'Ещё',
        'referral': '💰 Реферальная программа',
        'settings': '⚙️ Настройки ИИ',
        'info': '📖 Справочник',
        'feedback': '✉️ Обратная связь',
        'back': 'Назад ⬅',
        'first_promt': 'Изменить инструкции по ответу',
        'second_promt': 'Изменить описание желаемого ответа',
        'see_promts': 'Увидеть текущие настройки',
        'set_default_promt': 'Установить по умолчанию',

        'settings_ai': '⚙️ Настройки ИИ',
        'actual_ai': '🔄 Актуальность ИИ',

        'token': '⚖️ Отличие от ChatGPT',
        'usage_ai': '⚖️ Отличие от других ботов',
        'bot_benefit': 'О разработчиках',

        'create_new_chat': '➕ Создать',
        'change_name': '✏️ Сменить название',
        'show_history': '📋 Показать историю',
        'del_d': '🗑️ Удалить диалог',
        'change_model': '🤖 Сменить ИИ',
        'gpt-4o': 'GPT-4o (для сложных задач)',
        'gpt-4o-mini': 'GPT-4o mini (для повседневных задач)',
        'dall-e-3': 'DALL·E 3 (для создания изображений)',
        'payment_1': 'Ежемесячная 329₽ / мес.',
        'payment_2': 'Годовая ₽ 199₽ / мес.',
        'payment_type_1': 'Оплатить банковской картой',
        'payment_type_2': 'Оплатить криптовалютой',
        'to_wallet': '💳 Купить подписку'
    },
    'en': {

    }
}

default_btn_texts = btn_texts[config.DEFAULT_LAUNGAGE]