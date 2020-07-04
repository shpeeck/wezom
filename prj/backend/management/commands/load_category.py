from requests_html import HTMLSession


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


