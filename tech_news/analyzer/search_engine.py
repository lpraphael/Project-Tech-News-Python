from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})

    result = []

    for new in news_by_title:
        result.append((new["title"], new["url"]))

    return result


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

        result = []

        news_by_date = search_news({"timestamp": {"$eq": date_format}})

        for new in news_by_date:
            result.append((new["title"], new["url"]))

        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
