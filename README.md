![Zomato Logo](images/work_banner_vyEql_Zomato.jpg)
### Zomato Scraper

---

#### Overview
This project, Zomato Scraper, is a web scraping tool developed to gather restaurant data from Zomato using Python and Selenium. It was created primarily for learning purposes to gain proficiency in web scraping with Selenium.

#### Tech Stack
- Python
- Selenium

#### Usage
The main functionality of the project is implemented in `main.py`. Here's how to use it:

1. Specify the city for which you want to scrape restaurant data by setting the `city` variable in `main.py`.
2. Adjust `scroll_count` to determine how many times the script should scroll to load more restaurants. More scrolls typically fetch more results.
3. Set other options such as `more_info`, `images`, `as_csv`, `as_json`, and `as_xslsx` based on your scraping requirements.
4. Run the `main.py` script.

#### Project Structure
- **main.py**: Contains the main script to initiate the scraping process.
- **export/export.py**: Includes the `SCRAPE_ZOMATO_DINEOUT` class for scraping Zomato data.
- **Other files**: Additional files or modules used in the project.

#### Educational and Non-Affiliation Disclaimer
This project is an independent and unofficial educational project. It is not endorsed by or affiliated with Zomato. Any trademarks or service marks displayed in the project are the property of their respective owners.

#### Notes
- This project serves as an educational tool and is not actively maintained or updated.
