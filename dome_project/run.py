from scrapy import cmdline

# cmdline.execute("scrapy crawl dome".split())
# cmdline.execute("scrapy crawl jiandan".split())

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

if __name__ == '__main__':
    configure_logging()

    settings = get_project_settings()

    runner = CrawlerRunner(settings)
    runner.crawl('dome')
    runner.crawl('jiandan')

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()
