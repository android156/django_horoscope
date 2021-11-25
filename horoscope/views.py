from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect  # классы ответов при вызове
# создается соотв. объект
from django.shortcuts import render
from django.template.loader import render_to_string  # метод передающий html файл в виде строки
from django.urls import reverse  # метод собирающий пути

# Create your views here.

zodiac_descriptions_dict = {
    'aries':
        {'name': 'Овен',
         'description': 'первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'begin': '0321', 'end': '0420'},

    'taurus':
        {'name': 'Телец',
         'description': 'второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'begin': '0421', 'end': '0521'},

    'gemini':
        {'name': 'Близнецы',
         'description': 'третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'begin': '0522', 'end': '0621'},

    'cancer':
        {'name': 'Рак',
         'description': 'четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'begin': '0622', 'end': '0722'},

    'leo':
        {'name': 'Лев',
         'description': 'пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'begin': '0723', 'end': '0821'},

    'virgo':
        {'name': 'Дева',
         'description': 'шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
         'begin': '0822', 'end': '0923'},

    'libra':
        {'name': 'Весы',
         'description': 'седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
         'begin': '0924', 'end': '1023'},

    'scorpio':
        {'name': 'Скорпион',
         'description': 'восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)',
         'begin': '1024', 'end': '1122'},

    'sagittarius':
        {'name': 'Стрелец',
         'description': 'девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'begin': '1123', 'end': '1222'},

    'capricorn':
        {'name': 'Козерог',
         'description': 'десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'begin': '1223', 'end': '0120'},

    'aquarius':
        {'name': 'Водолей',
         'description': 'одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'begin': '0121', 'end': '0219'},

    'pisces':
        {'name': 'Рыбы',
         'description': 'двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'begin': '0220', 'end': '0320'},

}

month_dict = {
    'january': {
        'code': '01',
        'length': 31,
    },
    'february': {
        'code': '02',
        'length': 29,
    },
    'march': {
        'code': '03',
        'length': 31,
    },
    'april': {
        'code': '04',
        'length': 30,
    },
    'may': {
        'code': '05',
        'length': 31,
    },
    'june': {
        'code': '06',
        'length': 30,
    },
    'jule': {
        'code': '07',
        'length': 31,
    },
    'august': {
        'code': '08',
        'length': 31,
    },
    'september': {
        'code': '09',
        'length': 30,
    },
    'october': {
        'code': '10',
        'length': 31,
    },
    'november': {
        'code': '11',
        'length': 30,
    },
    'december': {
        'code': '12',
        'length': 31,
    },

}

data = {
    'title': '',
    'h1': '',

}

month_list = list(month_dict)

zodiac_signs_list = list(zodiac_descriptions_dict)

zodiac_signs_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

zodiac_signs_types_list = list(zodiac_signs_types)


def get_type_of_sign(sign):
    for type in zodiac_signs_types_list:
        if sign in zodiac_signs_types[type]:
            return type


def horoscope_main_page(request):
    # 1. Заменяем прямой вывод на вывод через шаблонизатор

    # li_elements = ''
    # for sign in zodiac_signs_list:
    #     sign_url = reverse('horoscope_name', args=[sign])
    #     li_elements += f'<li><a href="{sign_url}">{sign}</a></li>'
    # return HttpResponse(f"""
    # <h1>Главная страница гороскоп</h1>
    #     <ul>
    #         {li_elements}
    #     </ul>
    # """)

    # 2. render_to_string + HttpResponse можно заменить на рендер
    # response = render_to_string('horoscope/horoscope_main.html')
    # return HttpResponse(response)
    sign_url_dict = {}
    for sign in zodiac_signs_list:
        sign_url_dict[sign] = reverse('horoscope_name', args=[sign])

    data['title'] = 'Двенадцать знаков Зодиака'
    data['h1'] = 'Знаки Зодиака'
    data['sign_url_dict'] = sign_url_dict

    return render(request, 'horoscope/sign_list.html', context=data)


def horoscope_types(request):
    elements_url_dict = {}
    for zodiac_signs_type in zodiac_signs_types_list:
        elements_url_dict[zodiac_signs_type] = reverse('elements_types', args=[zodiac_signs_type])
    data['title'] = 'Стихии знаков Зодиака'
    data['h1'] = 'Стихии'
    data['elements_url_dict'] = elements_url_dict

    return render(request, 'horoscope/elements_list.html', context=data)


# Заменили на общую для всех знаков функцию
# def leo(request):
#     return HttpResponse('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).')
#
#
# def scorpio(request):
#     return HttpResponse('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).')


def get_info_about_zodiac_sign(request, sign_zodiac: str):  # В аргумент функции дабавили аннотацию :str, хотим тут
    # видеть строку
    if zodiac_descriptions_dict.get(sign_zodiac):
        data['title'] = f'Знак {sign_zodiac}'
        data['h1'] = sign_zodiac
        data['sign_zodiac'] = sign_zodiac
        data['description'] = zodiac_descriptions_dict[sign_zodiac]['description']
        data['name'] = zodiac_descriptions_dict[sign_zodiac]['name']


        return render(request, 'horoscope/sign_description.html', context=data)
    else:
        return HttpResponseNotFound(f'Знак "{sign_zodiac.upper()}" мне неизвестен')


def get_info_about_zodiac_sign_from_it_number(request, number_of_zodiac_sign: int):  # В аргумент функции дабавили
    # аннотацию :int, хотим тут видеть число
    if 0 < number_of_zodiac_sign <= len(zodiac_descriptions_dict):
        sign_zodiac = list(zodiac_descriptions_dict)[number_of_zodiac_sign - 1]
        # return HttpResponseRedirect(f'/horoscope/{sign_zodiac}')   Редирект на существующий роут
        # /horoscope/{sign_zodiac} - начало пути захардкожено исправляем
        redirect_url = reverse('horoscope_name', args=(sign_zodiac,))  # в кортеж args попадет sign_zodiac, а начало
        # пути - "/horoscope" найдется по имени роута (его параметр name = 'horoscope_name') в urls. Аргументов может
        # быть и больше.
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Знак Зодиака №{number_of_zodiac_sign} мне неизвестен')


def get_zodiac_signs_by_elements(request, element):
    elements_url_dict = {}
    for sign in zodiac_signs_types[element]:
        elements_url_dict[sign] = reverse('horoscope_name', args=[sign])

    data['title'] = f'Знаки стихии {element}'
    data['h1'] = f'Стихия {element}'
    data['elements_url_dict'] = elements_url_dict

    return render(request, 'horoscope/element.html', context=data)


def find_sign_by_date(month, day):
    my_date = month * 100 + day
    for sign in zodiac_signs_list:
        sign_begin = int(zodiac_descriptions_dict[sign]['begin'])
        sign_end = int(zodiac_descriptions_dict[sign]['end'])
        if sign_begin <= my_date <= sign_end:
            return sign
    if my_date >= 1223 or my_date <= 120:
        return 'capricorn'


def get_info_by_mixed_data(request, month: str, day: int):
    if month_dict.get(month):
        redirect_url = reverse('horoscope_data', args=(month_list.index(month) + 1, day))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Месяц {month} мне неизвестен')


def get_info_by_numeric_data(request, month: int, day: int):
    if 0 < month <= 12:
        if day < month_dict[month_list[month - 1]]['length']:
            my_sign = find_sign_by_date(month, day)
            type_of_my_sign = get_type_of_sign(my_sign)
            sign_url = reverse('horoscope_name', args=[my_sign])
            type_url = reverse('elements_types', args=[type_of_my_sign])
            return HttpResponse(f'''{month}/{day} числовой формат даты<br> 
            Ваш знак - <a href="{sign_url}">{my_sign}</a>. Стихия - <a href="{type_url}">{type_of_my_sign}</a>    
        ''')
        else:
            return HttpResponseNotFound(f'В месяце №{month} ({month_list[month - 1]}) нет столько ({day}) дней')

    else:
        return HttpResponseNotFound(f'Месяц №{month} мне неизвестен')
