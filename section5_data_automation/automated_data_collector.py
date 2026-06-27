import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_books(page_number):
    url = f"http://books.toscrape.com/catalogue/page-{page_number}.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page {page_number}.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating_word = book.p["class"][1]

        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_map.get(rating_word, 0)

        data.append({"Title": title, "Price": price, "Rating": rating})

    return data


def save_to_csv(data, filename="books.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename} successfully.")
    return df


def main():
    print("=" * 40)
    print("     Automated Book Data Collector")
    print("=" * 40)

    try:
        pages = int(input("How many pages to scrape? (1-50): "))
        if pages < 1 or pages > 50:
            print("Please enter a number between 1 and 50.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    all_books = []
    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        books = scrape_books(page)
        all_books.extend(books)

    if not all_books:
        print("No data collected.")
        return

    print(f"\nTotal books collected: {len(all_books)}")
    df = save_to_csv(all_books)

    print("\n" + "=" * 40)
    print("         PREVIEW (First 5 Books)")
    print("=" * 40)
    print(df.head().to_string(index=False))
    print("=" * 40)


main()