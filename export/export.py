import pandas as pd
from scraper.zomato_dineout_scraper import zomato_dine_out_scrape

class SCRAPE_ZOMATO_DINEOUT:

    def __init__(self, city, scroll_count, more_info, images, as_csv, as_json, as_xlsx) -> None:
        self.city = city
        self.scroll = scroll_count
        self.more_info = more_info
        self.images = images
        self.csv = as_csv
        self.json = as_json
        self.xslx = as_xlsx
        

    def scrape(self):
        results = zomato_dine_out_scrape(
            city= self.city,
            scroll_count= self.scroll,
            more_info=self.more_info,
            images=self.images,
        )

        if self.csv:
            df = pd.DataFrame(results[1:]).to_csv(self.city+'.csv', header=results[0])
        if self.json:
            df = pd.DataFrame(results[1:], columns=results[0]).T.to_json(self.city+'.json', index=False)
        if self.xslx:
            df = pd.DataFrame(results[1:]).to_excel(self.city+'.xlsx', header=results[0])

