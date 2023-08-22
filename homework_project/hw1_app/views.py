from django.shortcuts import render

from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html = '<h1> Это главная страница сайта на Джанго </h1>' \
           '<p> Здесь я тренируюсь создавать что-то' \
           '<p><a href="../hw1/aboutme/"> ссылка на страницу обо мне </a>'
    return HttpResponse(html)


def aboutme(request):
    logger.info('About me page accessed')
    html = '<h1> Это страница обо мне </h1>' \
           '<p> Это красивая картинка:' \
           '<p><img src="https://gribnicha.ru/wp-content/uploads/2023/08/maslyata-foto-.jpg"> <br>' \
           '<p><a href="../"> ссылка на главную </a>'
    return HttpResponse(html)
