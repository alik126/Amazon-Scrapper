from scraper import Scraper
from query_reader import FileReader


def main():
    input_file_path = input("Enter the input file path: ")
    file_reader = FileReader(input_file_path)

    # Initialize Scraper with extracted queries
    amazon_scraper = Scraper(file_reader)

    # Perform scraping
    amazon_scraper.perform_scrapping()


if __name__ == "__main__":
    main()
