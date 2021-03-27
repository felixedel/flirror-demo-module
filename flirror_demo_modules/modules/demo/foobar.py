import logging
import time

from flask import current_app

from flirror.modules import FlirrorModule


LOGGER = logging.getLogger(__name__)

# TODO (felix): Define some default values in FlirrorModule?
demo_module = FlirrorModule("flirror_demo", __name__, template_folder="templates")


@demo_module.view()
def get():
    return current_app.basic_get(template_name="demo/index.html")


@demo_module.crawler()
def crawl(module_id, app, message):
    demo_data = {"_timestamp": time.time(), "message": message}
    app.store_module_data(module_id, demo_data)
