from django.core.management.base import BaseCommand, CommandError
from backend.models import Category, Subcategory

from requests_html import HTMLSession


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start')
        Category.objects.all().delete()
        Subcategory.objects.all().delete()

        session = HTMLSession()
        resp = session.get('http://west-info.ua/katalog-predpriyatij/')
        a = 1

        while True:
            b = 1
            try:
                links = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/a/text()')
                print('Категория: {}'.format(links[0]))
                cat = Category()
                cat.name = links[0]
                cat.save()
                while True:
                    try:
                        links = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a/text()')
                        print('Подкатегория -- {}'.format(links[0]))
                        sub = Subcategory()
                        sub.name = links[0]
                        sub.category = cat
                        sub.save()
                        b += 1 
                    except:
                        break
                a += 1 
            except:
                break







'''
session = HTMLSession()
resp = session.get('http://west-info.ua/katalog-predpriyatij/')

links = resp.html.xpath('/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[1]/a/text()')
print(links)

a = 1
while True:
    b = 1
    try:
        links = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/a/text()')
        print('Категория: {}'.format(links[0]))
        while True:
            try:
                links = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a/text()')
                print('Подкатегория -- {}'.format(links[0]))
                b += 1 
            except:
                break
        a += 1 
    except:
        break


'''
