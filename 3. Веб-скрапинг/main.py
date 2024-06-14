import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

SEARCH = input("Какие вакансии вы хотите получить:").strip() or "python"
URL = f"https://hh.ru/search/vacancy?hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text={SEARCH}&enable_snippets=false&L_save_area=true"
KEYWORDS = ["django", "flask"]
CITIES = ["москва", "санкт-петербург"]
CURRENCY = input("В какой вылюте хотите получать зарплату: $  €  ₽ :").strip() or "$"


# Генерация заголовков
def get_headers():
    return Headers(browser="chrome", os="win").generate()


# Парсинг списка вакансий
def get_vacancies():
    main_respons = requests.get(URL, headers=get_headers()).text
    main_soup = BeautifulSoup(main_respons, "lxml")

    tag_content = main_soup.find("div", id="a11y-main-content")

    jobs = tag_content.find_all(
        "div", class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter"
    )

    return jobs


# Парсинг информации о вакансиях
def vacancy_info():
    jobs = get_vacancies()
    parsed_data = []

    for job in jobs:
        name = job.find("a", {"class": "bloko-link"}).text
        link = job.find("a", {"class": "bloko-link"})["href"]

        city = job.find("span", {"data-qa": "vacancy-serp__vacancy-address"}).text
        if city.lower() in CITIES:
            city = city.split()
            city = " ".join(city).title()
        else:
            continue

        job_response = requests.get(link, headers=get_headers())
        job_soup = BeautifulSoup(job_response.text, "lxml")

        salary = job_soup.find(
            "span",
            {
                "class": "magritte-text___pbpft_3-0-4 magritte-text_style-primary___AQ7MW_3-0-4 magritte-text_typography-label-1-regular___pi3R-_3-0-4"
            },
        ).text
        if CURRENCY in salary:
            salary = salary.split()
            salary = " ".join(salary)
        else:
            continue

        company = job_soup.find(
            "span", {"class": "bloko-header-section-2 bloko-header-section-2_lite"}
        ).text

        description = job_soup.find("div", {"class": "g-user-content"}).text
        if KEYWORDS[0] in description.lower() and KEYWORDS[1] in description.lower():
            description = description
        else:
            continue

        job_info = {
            "name": name,
            "link": link,
            "company": company,
            "salary": salary,
            "city": city,
        }
        parsed_data.append(job_info)

    return parsed_data


if __name__ == "__main__":
    parsed_data = vacancy_info()

    with open("vacancies.json", "w", encoding="utf-8") as file:
        json.dump(parsed_data, file, indent=4, ensure_ascii=False)

    print(f'Вакансии с ключевыми словами "{KEYWORDS}" сохранены в "vacancies.json"')
