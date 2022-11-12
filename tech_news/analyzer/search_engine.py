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
    result = []

    news_by_tag = search_news({"tags": {"$regex": tag, "$options": "i"}})

    for news in news_by_tag:
        result.append((news["title"], news["url"]))

    return result


# Requisito 9
def search_by_category(category):
    result = []

    news_by_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    for news in news_by_category:
        result.append((news["title"], news["url"]))

    return result
