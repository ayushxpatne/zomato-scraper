from export.export import SCRAPE_ZOMATO_DINEOUT

city = 'pune'
scroll_count = 0
more_info = False
images = False
as_csv = True
as_json = True
as_xslsx = True

if __name__ == '__main__':

    Zomato_Scrape = SCRAPE_ZOMATO_DINEOUT(city=city, 
        scroll_count = scroll_count,
        more_info = more_info,
        images = images,
        as_csv = as_csv,
        as_json = as_json,
        as_xlsx = as_xslsx
    )

    Zomato_Scrape.scrape()
