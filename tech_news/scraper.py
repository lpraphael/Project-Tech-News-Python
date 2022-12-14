import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url: str) -> str:
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    selector = Selector(html_content)

    return selector.css('.entry-title a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    selector = Selector(html_content)

    return selector.css('.next::attr(href)').get()


# Requisito 4
def scrape_noticia(html_content: str) -> dict:
    selector = Selector(html_content)

    url = selector.css('link[rel=canonical]::attr(href)').get()
    title = selector.css('.entry-title::text').get().rstrip()
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('.author a::text').get()
    comments_count = selector.css('.post-comments-simple h5::text').get() or 0
    summary = selector.xpath('string(//p)').get().rstrip()
    tags = selector.css('.post-tags a::text').getall()
    category = selector.css('.meta-category span.label::text').get()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'comments_count': comments_count,
        'summary': summary,
        'tags': tags,
        'category': category,
    }


# Requisito 5
def get_tech_news(amount: int) -> list:
    url = 'https://blog.betrybe.com/'
    all_news = []
    n = len(all_news)

    while n < amount:
        html_content = fetch(url)
        news_url = scrape_novidades(html_content)

        for link in news_url:
            if n == amount:
                break
            new_content = fetch(link)
            all_news.append(scrape_noticia(new_content))
            n += 1

        url = scrape_next_page_link(html_content)

    create_news(all_news)

    return all_news
