import importlib.util
spec = importlib.util.spec_from_file_location("botconfig", "./discord_bot/discord_botconfig.py")
botconfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(botconfig)

def get():
    name = botconfig.botconfig['name']
    prefix = botconfig.botconfig['prefix'] 
    return [
            'Russian',
            [
                [
                    ' - простой и немного расширяемый. Developed by Jaxee. **Префикс:** `{0}`{1}\n\n**А Вы знаете, что...** {2}',
                  [ # 1.0.1
                    'Основное', # 1.0.1.0
                    '`help`, `state`, `profile`, `tnews`, `feedback`, `info`' # 1.0.1.1
                  ],
                  [ # 1.0.2
                    'Развлечения', # 1.0.2.0
                    '`photo`, `8ball` (`crystball`), `music`'
                  ],
                  [
                    'Служебное', # 1.0.3.0
                    '`settings`, `post`' # 1.0.3.1
                  ],
                  [ # 1.0.4
                    'Разное', # 1.0.4.0
                    '`calc`, `weather`, `codec`, `poll`, `rep`' # 1.0.4.1
                  ],
                  '**Префикс:** ', # 1.0.5
                  [ # 1.0.6
                    'Требования', # 1.0.6.0
                    'Инструкция', # 1.0.6.1
                    'Параметры', # 1.0.6.2
                  ]
                ],
                [
                    'Состояние бота',
                    'Задержка',
                    ' мс',
                    'Под управлением',
                    'Центральный процессор',
                    'Версия Python',
                    'Дата сборки Python',
                    'Версии пакетов',
                    'Аналитика',
                    ' ядро',
                    ' ядра',
                    ' ядер',
                    ' МГц',
                    'Оперативная память',
                    ' кБ',
                    ' МБ',
                    ' ГБ',
                    ' свободно'
                ],
                [
                    'Настройки',
                    'Для доступа к нужной настройке нажмите на одну из соотвествующих реакций.\n\n**🗣️ Язык бота (Bot language)**\n**🕓 Часовой пояс**\n**🗨️ Счетчик сообщений**\n**🌈 Свой цвет вложенных сообщений**\n🚩 **Префикс бота**\n🏆 **Система уровней**\n👋 **Приветственные/прощальные сообщения**',
                    [
                        'Язык бота (Bot language)',
                        'Для изменения значения введите команды, которые указаны внизу.\n\n**🇷🇺 Русский**\n```{0}set -l ru-RU```\n\n**🇺🇸 English**\n```{0}set -l en-US```'
                    ],
                    [
                        'Часовой пояс',
                        'Текущее время',
                        'Допустимые значения',
                        'От -120 до 140 (UTC)',
                        'Пример',
                        '```{0}set -tz -80\n{0}set -tz 30\n{0}set -tz 55```',
                        '-80 для UTC-8:00, 30 для UTC+3:00 (Москва), 55 для UTC+5:30.'
                    ],
                    [
                        'Ошибка',
                        'Это значение должно быть исключительно числовым.',
                        'Вы изменили часовой пояс на UTC'
                    ],
                    [ # 1.2.5
                        'Счетчик сообщений', # 1.2.5.0
                        'Вы настраиваете бота Console на уровне Вашего сервера или лично для себя? Для выбора ответа нажмите одну из соответствующих реакций.\n||_да, мы используем БД SQLite_||\n\n🏠 - на уровне сервера\n👤 - для себя', # 1.2.5.1
                        'Счетчик сообщений включен.', # 1.2.5.2
                        'Счетчик сообщений выключен.', # 1.2.5.3
                        'Извините, но у Вас нет прав на управление сервером. Пожалуйста, воспользуйтесь личными настройками.', # 1.2.5.4
                        'Ошибка' # 1.2.5.5
                    ],
                    [ # 1.2.6
                        'Счетчик сообщений', # 1.2.6.0
                        'Всего подсчитанных сообщений с начала ', # 1.2.6.1
                        ' сообщений', # 1.2.6.2
                        'Допустимые значения', # 1.2.6.3
                        '`on` - включить, `off` - отключить', # 1.2.6.4
                        'Пример', # 1.2.6.5
                        '```{0}set -mc on```' # 1.2.6.6
                    ],
                    [ # 1.2.7
                        'Свой цвет вложенных сообщений (🏠)', # 1.2.7.0
                        'Допустимые значения', # 1.2.7.1
                        '`red`, `orange`, `yellow`, `green`, `skyblue`, `blue`, `violet`, `rose`', # 1.2.7.2
                        'Пример', # 1.2.7.3
                        '```{0}set -ec skyblue```', # 1.2.7.4
                        'Свой цвет вложенных сообщений (🏠)', # 1.2.7.5
                        'Изменения сохранены.' # 1.2.7.6
                    ],
                    [ # 1.2.8
                        'Префикс бота', # 1.2.8.0
                        'Значение по умолчанию', # 1.2.8.1
                        'Пример', # 1.2.8.2
                        '```{0}set -pfx v!```', # 1.2.8.3
                        'Изменения сохранены.', # 1.2.8.4
                        '**ВНИМАНИЕ!** Поскольку вы сейчас используете самую свежую версию бота, то, соответственно, эта настройка может нуждаться в доработке.', # 1.2.8.4
                    ],
                    [ # 1.2.9
                        'Система уровней',
                        'Допустимые значения',
                        '`on` - включить, `off` - отключить',
                        'Пример',
                        '```{0}set -lvs on```'
                    ],
                    [ # 1.2.10
                        'Приветственные/прощальные сообщения', # 1.2.10.0
                        'Допустимые значения', # 1.2.10.1
                        '`[ID канала] [Текст]` - включить или отредактировать\n`off` - отключить', # 1.2.10.2
                        'Пример', # 1.2.10.3
                        '```{0}set -wl_msg 794585820312633354 Привет, ╭user╮\n{0}set -gb_msg 794585820312633354 Пока, ╭user╮```', # 1.2.10.4
                        'Автоформатирование', # 1.2.10.5
                        '`{user}` - имя пользователя\n`{user_with_discrim}` - имя пользователя с дискриминатором\n`{gn}` - имя сервера\n`{mention}` - упоминание пользователя',  # 1.2.10.6
                        'Ошибка', # 1.2.10.7
                        'Этот канал невозможно найти на Вашем Discord-сервере.' # 1.2.10.8
                    ]
            ],
            [ # 1.3
                'О пользователе ', # 1.3.0
                'Псевдоним', # 1.3.1
                'Дата прихода в сервер', # 1.3.2
                'Дата регистрации', # 1.3.3
                'Всего сообщений с ', # 1.3.4
                ' сообщ.', # 1.3.5
                '_У этого пользователя счетчик сообщений выключен_', # 1.3.6
                '[БОТ] ', # 1.3.7
                'Аватар пользователя ', # 1.3.8
                '', # 1.3.9
                'Статус', # 1.3.10
                [ # 1.3.11
                    '<:online:861861013241856001> Онлайн', # 1.3.11.0
                    '<:idle:861861016043913216> Отошел', # 1.3.11.1
                    '<:dnd:861861013347106836> Занят', # 1.3.11.2
                    '<:offline:861861010163367947> Оффлайн' # 1.3.11.3
                ],
                'Роли ', # 1.3.12
                'Дата отправки последнего сообщ.', # 1.3.13
                'Репутация', # 1.3.14
                'Уровень', # 1.3.15
                'Ссылка на аватар', # 1.3.16
            ],
            [
                'О сервере ',
                '',
                'Описание',
                'Владелец',
                'Дата создания',
                'Бустов',
                'Каналов',
                'Участников',
                'Фильтрация контента 18+',
                'Канал для правил',
                'Канал бездействия',
                'Защита 2FA',
                'Уровень верификации',
                [
                    'Без ограничений',
                    'Простой',
                    'Средний',
                    'Сложный',
                    'Строгий'
                ],
                [   
                    'Вкл.',
                    'Выкл.',
                    '_Не включено "Сообщество"_',
                    '_Нет канала бездействия_'
                ],
                [
                    '💎 ',
                    ' | 🧙 ',
                    '💬 ',
                    ' | 🔉 ',
                    '👤 ',
                    ' | 🔌 '
                ],
                'Сообщений',
                '_У этого сервера счетчик сообщений выключен_',
                'Ссылка на аватар',
            ],
            [
                'Профили',
                '`{0}profile -u [ID]` - узнать информацию о пользователе.\n`{0}profile -g` - узнать информацию о сервере',
                '**Свои параметры** (изменить можно в `{0}settings`)**:**\n',
                'вкл. счетчик сообщений',
                'часовой пояс UTC',
                '',
                '🇷🇺',
                'выкл. счетчик сообщений',
            ],
            [ # 1.6
                'Новости Тинеликса', # 1.6.0
                'Для выбора заголовка нажмите одну из соответствующих реакций.\n\n' # 1.6.1
            ],
            [ # 1.7
                ' ', # 1.7.0
                ' ', # 1.7.1
                ' ', # 1.7.2
                ' ', # 1.7.3
                ' ', # 1.7.4
                ' ', # 1.7.5
                ' ', # 1.7.6
                ' ', # 1.7.7
                ' ', # 1.7.8
                ' ', # 1.7.9
                ' ', # 1.7.10
                ' ', # 1.7.11
                ' ', # 1.7.12
                ' ', # 1.7.13
                ' ' # 1.7.14      
            ],
            [ # 1.8
                'Случайные фото', # 1.8.0
                'Автор', # 1.8.1
                'Лайков', # 1.8.2
                'Пока хватит!', # 1.8.3
                'Посмотреть еще фотки можно будет только через час, так как в API Unsplash действует лимит - не больше 50 запросов за час. Приносим извинения за доставленные неудобства.', # 1.8.4
                '`{0}photo -u` - просмотр фотографий из Unsplash.\n`{0}photo -r` - просмотр фотографий из сабреддитов.', # 1.8.5
                '`{0}photo -u` - просмотр фотографий из Unsplash.', # 1.8.6
                '`{0}photo -r` - просмотр фотографий из сабреддитов.', # 1.8.7
                'Эта команда не работает без доступа к двум API.', # 1.8.8
                'Вы не можете просматривать фотографии без доступа к Unsplash API. Для решения этой проблемы свяжитесь с автором бота.', # 1.8.9
                'Вы не можете просматривать фотографии без доступа к Reddit API. Для решения этой проблемы свяжитесь с автором бота.', # 1.8.10
            ],
            [ # 1.9
                'Калькулятор', # 1.9.0
                'Листинг', # 1.9.1
                'Результат', # 1.9.2
                'Обнаружено исключение!\n', # 1.9.3
                'Вы забыли ввести выражение.\n```{0}calc 4 * 58```', # 1.9.4
                'В этой версии Калькулятора можно совершать только простые арифметические выражения.', # 1.9.5
                'Доступные знаки', # 1.9.6
                '`+` - прибавить\n`-` - убавить\n`*` - умножить\n`/` - разделить', # 1.9.7
                'Попытка деления на ноль', # 1.9.8
                'Выражение слишком большое', # 1.9.9
                'Переменные не принимаются', # 1.9.10
            ],
            [ # 1.10
                'Обратная связь', # 1.10.0
                'Баг-трекер {0}'.format(name), # 1.10.1
                'Автор бота ответит на Ваш вопрос в ближайшее время, подождите.', # 1.10.2
                'Вы забыли указать аргументы. Кстати, можно скриншоты отправлять, так проще разобраться.\n\n```{0}feedback Привет!```', # 1.10.3
                'Вам ответили: ', # 1.10.4
                'Приблизительное время ожидания', # 1.10.5
                'более 10 минут', # 1.10.6
                '{0} минут', # 1.10.7
                'Обычно в такие часы (после {0} по местному времени) наша служба поддержки не сможет отправить Вам ответное сообщение.'
            ],
            [ # 1.11
                'Погода | ', # 1.11.0
                'Температура ', # 1.11.1
                'мин. ', # 1.11.2
                '\nсрд. ', # 1.11.3
                '\nмакс. ', # 1.11.4
                'Скорость ветра', # 1.11.5
                ' м/с', # 1.11.6
                'Влажность', # 1.11.7
                'Прогноз на ближайшие 12 часов', # 1.11.8
                'Используется OpenWeatherMap API', # 1.11.9
                'ru', # 1.11.10
                'Ошибка', # 1.11.11
                'Не удается найти город или населенный пункт по запросу.\n\nМожет, напишете по-другому?', # 1.11.12
                'Код ошибки', # 1.11.13
                'Вы забыли дописать имя города или населенного пункта.\n```{0}weather Москва```' # 1.11.14
            ],
            [ # 1.12
                'Магический шар', # 1.12.0
                'Вопрос', # 1.12.1
                'Он говорит', # 1.12.2
                'Все совпадения случайны. Воспринимайте как игру, а не как реальность.', # 1.12.3
                'Ошибка', # 1.12.4
                'Сначала задайте ему вопрос.' # 1.12.5
            ],
            [ # 1.13
                'Ошибка', # 1.13.0
                'Вы должны обязательно включить функции сообщества на Вашем Discord-сервере для публикации новостей.', # 1.13.1
                'Вы забыли указать сообщение для публикации.', # 1.13.2
                'Команда недоступна, так как у Вас недостаточно прав на управление сообщениями.',
                'Сначала переключитесь на новостной канал.\n\n**Инфа для креаторов:** Новостные каналы - это и есть каналы с объявлениями, но чтобы постить сообщения, Вам нужно обязательно в настройках канала (не путать с настройками сервера!) поставить галочку в пункте "Канал с объявлениями". Текст этого пункта может отличаться в зависимости от Вашей установленной локализации клиента.'
            ],
            [ # 1.14
              'Кодек', # 1.14.0 
              'Вам предстоит выбрать тип данных для декодирования в обычную строку. Выбор типа осуществляется нажатием на соответствующую реакцию.', # 1.14.1
              'Вам предстоит выбрать тип данных для кодирования из обычной строки. Выбор типа осуществляется нажатием на соответствующую реакцию.', # 1.14.2
              '1️⃣ Base64\n2️⃣ Base32\n3️⃣ Base16\n4️⃣ Двоичный код', # 1.14.3
              'Результат',
              '`{0}codec -d` - расшифровка текста\n`{0}codec -e` - зашифровка текста',
              'Расшифровать не получилось. Неверно выбран тип данных.',
              'Просмотр в Embed-сообщении невозможен.',
              'Вы забыли ввести текст.\n\n```{0}codec -e Привет!\n{0}codec -d SGVsbG8h```'
            ],
            [ # 1.15
              'О боте', # 1.15.0
              '{0} - простой и расширяемый бот от Jaxee. Этот бот является заменой бота Effective bot, который был достаточно сырым для запуска на мониторинг ботов. Но не беспокойтесь, в боте Console есть (пускай, неидеальная) интеграция с БД SQlite3, когда в Effective bot был только примитивный JSON. Бот написан с нуля и учитывал ошибки, допущенные при разработке бота Effective bot. Теперь он развивается не только благодаря Вам, но и авторе (Jaxee\'у) своей продуктивностью.\n\nОн может узнавать погоду в Вашем городе, шифровать или расшифровать тексты, показывать случайные и довольно интересные фотографии с Reddit и Unsplash, поиграть в \"Шар судьбы\" и т. д.\n\n_Бот Console и его открытый исходный код распространяются с условиями лицензии MIT License'.format(name), # 1.15.1
              'Написан на', # 1.15.2
              'Автор', # 1.15.3
              'Мониторинги ботов', # 1.15.4
              '[bots.server-discord.com](https://bots.server-discord.com/785383439196487720)\n[BotiCord](https://boticord.top/bot/901352871071715408)\n[discord.bots.gg](https://discord.bots.gg/bots/901352871071715408)', # 1.15.5
              'Ссылки', # 1.15.6
              '[Пригласить бота](https://discord.com/api/oauth2/authorize?client_id=901352871071715408&permissions=8&scope=8)\n[GitHub](https://github.com/Mr-Jaxee/Console)\n[ВКонтакте](https://vk.com/jaxee_community)\n[YouTube](https://www.youtube.com/channel/UCN4WMA-kU57j6xeKF5tTwCA)\n[Сервер разработчика](https://discord.gg/QbQ8qs4jDz)' # 1.15.7
            ],
            [ # 1.16
              'Голосование', # 1.16.0
              'Вести это голосование могут только администраторы сервера.', # 1.16.1
              'Время пошло! Время окончания: {0}', # 1.16.2
              'Голосование закончено.', # 1.16.3
              'Вы забыли указать требуемые аргументы к этой команде или разделить аргументы знаками `[` и `],`. Следуйте примером внизу. И да, между скобками запятая без каких-либо пробелов обязательна.\n\n```{0}poll Что Вам нравится больше всего? -o [90-е],[2000-е],[2010-е],[2020-е] 2021-02-12=18:00```', # 1.16.4
              'Дата окончания голосования не должна быть раньше, чем сегодняшняя.'
            ],
            [ # 1.17
              'Репутация',
              'Вы хотите повысить или понизить человека? Выбор осуществляется нажатием на реакцию.\n\n👍 **Повысить**\n👎 **Понизить**',
              'Повышать или понижать самого себя нельзя!',
              'Окей, Вы его понизили.',
              'Окей, Вы его повысили.',
              'Пример',
              '```{0}rep <ID участника>```',
              'Этого человека нет в нашей базе данных.',
              'Вы его уже повысили.',
              'Вы его уже понизили.'
            ],
            [ # 1.18
                'Поздравляем!',
                '{0} перешел на новый уровень **{1}**! Главное - проявлять активность.'
            ],
            [ 'Доступ запрещен.'],
            [ 
              'Конструктор вложенных сообщений',
              'Вы забыли указать требуемые аргументы к этой команде или разделить аргументы знаками `[` и `],` Следуйте пример внизу. И да, между скобками запятая без каких-либо пробелов обязательна.\n\n```{0}embed Текст -t [Заголовок],[Футер]```'
            ],
            [ # 1.21
              'Музыкальный плеер', # 1.21.0
              'Не найдено результатов по Вашему запросу. Попробуйте другой запрос.', # 1.21.1
              'API временно недоступен.', # 1.21.2
              'Результаты поиска', # 1.21.3
              '**Сейчас играет:** {0} ({1}/{2})\n {3} из {4}', # 1.21.4
              'Очереди', # 1.21.5
              'Сначала присоединяйтесь к любому голосовому каналу, а затем повторите попытку.', # 1.21.6
              'Прослушивание остановлено.', # 1.21.7
              'Вы действительно хотите очистить плейлист?\nДля подтверждения нужно собрать 3 реакции.',
              'Плейлист очищен.',
              'Используется YouTube Data API',
              'Что-то пошло не так...',
              'Загрузка {0} из {1} МБ...',
              'Трек не должен превышать 30 минут в длительности.',
              'Для воспроизведения музыки достаточно указать запрос поиска на YouTube.\n\n```{0}music Tobu Cacao```',
              '**Пауза:** {0} ({1}/{2})\n{3} из {4}',
              'На данный момент воспроизведение потокового мультимедиа недоступно.',
              'Произошла ошибка с выводом результатов поиска. Скорее всего, это какая-то проблема на стороне модуля `youtube_search`. Попробуйте поискать еще раз.'
            ],
            [ #1.22
              'Кик', #1.22.0
              '```Модератор```', #1.22.1
              '```Нарушитель```', #1.22.2
              '```Причина```', #1.22.3
              'Причина не указана' #1.22.4
            ]
        ]
    ]

def longdate():
    return ['Russian', '{0} января {1} г.', '{0} февраля {1} г.', '{0} марта {1} г.', '{0} апреля {1} г.', '{0} мая {1} г.', '{0} июня {1} г.', '{0} июля {1} г.', '{0} августа {1} г.', '{0} сентября {1} г.', '{0} октября {1} г.', '{0} ноября {1} г.', '{0} декабря {1} г.']

def longdate_without_year():
    return ['Russian', '{0} января', '{0} февраля', '{0} марта', '{0} апреля', '{0} мая', '{0} июня', '{0} июля', '{0} августа', '{0} сентября', '{0} октября', '{0} ноября', '{0} декабря']

def shortdate_without_year():
    return ['Russian', '{0} янв.', '{0} фев.', '{0} мар.', '{0} апр.', '{0} мая', '{0} июн.', '{0} июл.', '{0} авг.', '{0} сен.', '{0} окт.', '{0} ноя.', '{0} дек.']
