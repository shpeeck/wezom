

from requests_html import HTMLSession
import re


print('Start')

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
            print('Зашел в цикл')
            try:
                print("зашел в трай")
                link = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a')
                print('Подкатегория -- {}'.format(link[0]))
                url = str(link[0]).split("href=")[1].rstrip('\'>').lstrip("\'")
                dom = "http://west-info.ua"
                full_url = f"{dom}{url}"
                cat = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/a/text()')
                pod = resp.html.xpath(f'/html/body/header/div[3]/div/nav/ul/li[2]/ul/li[{a}]/ul/li[{b}]/a/text()')
                # print(cat, pod)
                page = 1
                page_one = 1
                while True:
                    print('tot цикл')
                    try:
                        print('tot трай')
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
                        # page = 1
                        print(max_page)
                        print(page)
                        if page <= max_page:
                            print('ok')
                            full_url_page = f"{full_url}?page={page}"
                            session = HTMLSession()
                            resp = session.get(full_url_page)
                            print(full_url_page)
                            try:
                                code = resp.text
                                # print(code)
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
                                        # city = re.findall(r'<h1 class="main-ttl"><span>.+', code)
                                        # phone = re.findall(r'<h1 class="main-ttl"><span>.+', code)
                                        # content = re.findall(r'<h1 class="main-ttl"><span>.+', code)
                                        address = re.findall(r'Адрес:</b> .+', code)
                                        address = address[0].split('Адрес:</b> ')
                                        address = address[1]
                                        address = address.split('</')
                                        address = address[0]
                                        print('Адрес: ', address)

                                        # image = re.findall(r'<h1 class="main-ttl"><span>.+', code)
                                    except:
                                        print('laja')


                                # print(company_url)
                                # http://west-info.ua/company/metall-proekt-chp/
                                # /html/body/main/div/section/div/div[2]/div[1]/div/h3/a # 1 металлообработка
                                # /html/body/main/div/section/div/div[1]/div[1]/div/h3/a # 2 деревообработка
                                # /html/body/main/div/section/div/div[1]/div[1]/div/h3/a # 3
                            except:
                                print("none")
                        # Пройтись по странице xpath и собрать ссылки
                            page += 1
                        else:
                            break


                        # /html/body/main/div/section/div/div[1]/div[1]/div/h3/a
                        # /html/body/main/div/section/div/div[2]/div[2]/div/h3/a
                        # /html/body/main/div/section/div/div[2]/div[1]/div/h3/a
                        # перейти на следующую страницу и повторить

                        # page += 1
                    except:
                        print('tot еусцепт')
                        break

                b += 1 
            except:
                print("зашел в эксцепт")
                break
        a += 1 
    except:
        break

print(start_urls)


# 