from os import path

from .webslides_builder import WebslidesBuilder

def setup(app):
    app.add_builder(WebslidesBuilder)
    app.add_html_theme('webslides_theme', path.join(path.abspath(path.dirname(__file__)), 'themes', 'webslides_base'))
