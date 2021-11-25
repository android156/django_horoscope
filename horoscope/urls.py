from django.urls import path

from . import views  # Т.к. мы в той же папке, что и views, иначе было бы from horoscope import views

urlpatterns = [

    path('', views.horoscope_main_page, name='main'),  # ссылаемся(не вызываем, поэтому без скобок!!!) на функции из views
    # ссылаемся(не вызываем, поэтому без скобок!!!) на функции из views

    path('<int:month>/<int:day>', views.get_info_by_numeric_data, name='horoscope_data'),
    path('<str:month>/<int:day>', views.get_info_by_mixed_data),

    path('types', views.horoscope_types, name='elements'),
    path('types/<element>', views.get_zodiac_signs_by_elements, name='elements_types'),

    # строки ниже заменим на динамический URL - Uniform Resource Locator, или унифицированный указатель ресурса
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
    path('<int:number_of_zodiac_sign>', views.get_info_about_zodiac_sign_from_it_number),
    # int: конвертер, если sign_zodiac,
    # можно сконвертировать в число, то выполнится get_info_about_zodiac_sign_from_it_number

    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
    # str: конвертер, если sign_zodiac можно сконвертировать в строку, то выполнится
    # get_info_about_zodiac_sign. Добавлен параметр name, чтобы убрать хардкод /horoscope
    # во вьюхах

]
