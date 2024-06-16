from flask import Blueprint, render_template, request, redirect, url_for
from export.export import SCRAPE_ZOMATO_DINEOUT_FLASK

view = Blueprint("view", __name__)


@view.route("/", methods=["get", "post"])
def homepage():
    return render_template("zs-webpage.html")


@view.route("/submit", methods=["get", "post"])
def formsubmitted():
    form_data = request.form.to_dict()
    error_city, error_scroll, more_info, images, city, scroll = form_values(form_data=form_data)

    city_name = request.form.get("city") 
   
    action = request.form.get('action')
    
    try:
        initiate_scrape = SCRAPE_ZOMATO_DINEOUT_FLASK(city=city_name, 
            scroll_count = scroll,
            more_info = more_info,
            images = images,
            action=action
        )

        initiate_scrape.scrape()
    except Exception as e:
        print(e)

    return render_template(
        "zs-webpage.html",

        city=city_name,
        scroll=scroll,
        error_city = error_city,
        error_scroll = error_scroll
    )

@view.route("/export")
def file_export():
    action = request.args.get('action')

    return f'exported as {action}'

def form_values(form_data):
    error_city = False
    error_scroll = False
    more_info = False
    images = False
    city = form_data['city']
    scroll = None

    if len(form_data["city"].strip()) == 0:
        error_city= 'True'

    try:
        scroll = int(
            form_data["scroll"],
        )
    except:
        error_scroll = 'True'

    if "more-info" in list(form_data.keys()):
        more_info = True

    if "images" in list(form_data.keys()):
        images = True
    
    return error_city, error_scroll, more_info, images, city, scroll