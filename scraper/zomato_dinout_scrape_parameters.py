from scraper import zomato_info_page

def more_info_from_links(driver, output):

    for elements in output[1:]:
        element_link = elements[4]
        retrieved_more = zomato_info_page.get_more_info(driver, element_link)
        elements.append(retrieved_more)

    
def images_form_links(driver, output):
    for elements in output[1:]:
        element_link = elements[4]
        images_list = zomato_info_page.get_images(driver, element_link)
        elements.append(images_list)