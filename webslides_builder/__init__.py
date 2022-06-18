from os import path

from .webslides_builder import WebslidesBuilder
from .webslides_directives import *

def setup(app):
    app.add_builder(WebslidesBuilder)
    app.add_node(slide_class_node)
    app.add_node(slide_size_node)
    app.add_directive('slide-config', SlideConfigDirective)
    app.add_directive('flexblock-feature', FlexBlockFeatures)
    app.add_html_theme('webslides_theme', path.join(path.abspath(path.dirname(__file__)), 'themes', 'webslides_base'))
