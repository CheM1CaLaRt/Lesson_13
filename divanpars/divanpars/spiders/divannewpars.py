import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # Пишем ту же команду, которую писали в терминале
        lights = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным светильником в списке
        for light in lights:
            # Используем новый для нас оператор "yield", который помогает обрабатывать одно отдельное действие
            # С его помощью мы можем управлять потоком выполнения, останавливать и возобновлять работу парсера
            # С другими операторами мы такого делать не можем
            yield {
                # Ссылки и теги получаем с помощью консоли на сайте
                # Создаём словарик названий
                'name': light.css('div.lsooF span::text').get(),
                # Создаём словарик цен
                'price': light.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок
                'url': light.css('a').attrib['href']
            }
