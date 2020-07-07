from django.core.management.base import BaseCommand, CommandError
from backend.models import Category, Subcategory, Enterprises

from requests_html import HTMLSession
import re

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start')
        Enterprises.objects.all().delete()
        session = HTMLSession()
        resp = session.get('http://west-info.ua/katalog-predpriyatij/')
        a = 1
        start_urls = []
        while True:
            b = 1
            try:
                links = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/a/text()')
                print('Категория: {}'.format(links[0]))
                while True:
                    try:
                        link = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a')
                        print('Подкатегория -- {}'.format(link[0]))
                        url = str(link[0]).split("href=")[1].rstrip('\'>').lstrip("\'")
                        dom = "http://west-info.ua"
                        full_url = f"{dom}{url}"
                        cat = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/a/text()')
                        pod = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a/text()')
                        page = 1
                        page_one = 1
                        while True:
                            try:
                                max_page = []
                                i = 20
                                while i>=0:
                                    full_url_page = f"{full_url}?page={page_one}"
                                    session = HTMLSession()
                                    resp = session.get(full_url_page)
                                    tit = resp.html.xpath('/html/body/main/div/section/div/ul/li[5]/a/text()')
                                    max_page.append(tit)
                                    i -= 1
                                    page_one += 1
                                max_page = int(str(max_page[-1]).strip("[']"))
                                if page <= max_page:
                                    full_url_page = f"{full_url}?page={page}"
                                    session = HTMLSession()
                                    resp = session.get(full_url_page)
                                    print(full_url_page)
                                    try:
                                        code = resp.text
                                        company_url = re.findall(r'<a href="/company/.+', code)
                                        for i in company_url:
                                            url = i.lstrip('<a href="').rstrip()
                                            url = url.split("/")
                                            url = f'{dom}/{url[1]}/{url[2]}/'
                                            print(url)
                                            try:
                                                session = HTMLSession()
                                                resp = session.get(url)
                                                code = resp.text
                                                company_name = re.findall(r'<h1 class="main-ttl"><span>.+', code)
                                                company_name = company_name[0].split('span')
                                                company_name = company_name[1]
                                                company_name = company_name.strip('></')
                                                print('Название: ', company_name)
                                                city = re.findall(r'<b>Город:</b>.+', code)
                                                city = city[0].split('<')
                                                city = city[2]
                                                city = city.split('>')
                                                city = city[1]
                                                print('Город: ', city)
                                                phone = re.findall(r'<b>Телефон</b> .+', code)
                                                phone = phone[0].split('<b>Телефон</b> ')
                                                phone = phone[1]
                                                phone = phone.split('</')
                                                phone = phone[0]
                                                print('Телефоны: ', phone)
                                                content = re.findall(r'<p>.+', code)
                                                content = content[0]
                                                content = content.split('p>')
                                                content = content[1]
                                                content = content.split('<')
                                                content = content[0]
                                                print('Контент', content)
                                                address = re.findall(r'Адрес:</b> .+', code)
                                                address = address[0].split('Адрес:</b> ')
                                                address = address[1]
                                                address = address.split('</')
                                                address = address[0]
                                                print('Адрес: ', address)
                                                image = re.findall(r'/admin/uploads/products/images/.+', code)
                                                image = image[0]
                                                image = image.split('"')
                                                image = image[0]
                                                image = f'{dom}{image}'
                                                
                                                print('Изображение: ', image)
                                                subcat = Subcategory.objects.all()
                                                firm = Enterprises()
                                                firm.name = company_name
                                                firm.content = content
                                                firm.image = image
                                                firm.phone = phone
                                                firm.address = address
                                                for i in subcat:
                                                    if i.name == pod[0]:
                                                        firm.subcategory = i
                                                # firm.category = cat
                                                firm.save()
                                            except:
                                                break
                                    except:
                                        break
                                    page += 1
                                else:
                                    break
                            except:
                                break
                        b += 1 
                    except:
                        break
                a += 1 
            except:
                break
        print(start_urls)
