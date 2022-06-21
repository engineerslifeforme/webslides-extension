from os import path

from .webslides_builder import WebslidesBuilder
from .webslides_directives import *

def setup(app):
    app.add_builder(WebslidesBuilder)
    app.add_node(slide_class_node)
    app.add_node(slide_size_node)
    app.add_node(div_node)
    app.add_node(flexblock_list_node)
    app.add_node(flexblock_feature_list_node)
    app.add_node(pseudo_heading_node)
    app.add_node(span_node)
    app.add_node(span_raw_node)
    app.add_node(generic_node)
    app.add_directive('slide-config', SlideConfigDirective)
    app.add_directive('flexblock-feature', FlexBlockFeatures)
    app.add_directive('flexblock', FlexBlock)
    app.add_directive('div', Div)
    app.add_directive('generic', GenericDirective)
    app.add_html_theme('webslides_theme', path.join(path.abspath(path.dirname(__file__)), 'themes', 'webslides_base'))
    app.add_role('ph1', pseudo_heading_role('h1'))
    app.add_role('ph2', pseudo_heading_role('h2'))
    app.add_role('ph3', pseudo_heading_role('h3'))
    app.add_role('span', span_roles())
    app.add_role('span-raw', span_roles(raw=True))
