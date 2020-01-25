from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from avitoparser.spiders.avito import AvitoSpider
from avitoparser import settings


if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    section = input('Введите категорию на латинице например, avtomobili, kvartiry, velosipedy: ')
    process.crawl(AvitoSpider, section=section)
    process.start()
