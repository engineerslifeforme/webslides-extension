from os import path

from .webslides_builder import WebslidesBuilder
from .slide import setup_slide
from .font_awesome import setup_fa
from .header import setup_header
from .div import setup_div
from .link import setup_link
from .paragraph import setup_paragraph
from .span import setup_span

def setup(app):
    app.add_builder(WebslidesBuilder)
    app.add_html_theme('webslides_theme', path.join(path.abspath(path.dirname(__file__)), 'themes', 'webslides_base'))
    setup_slide(app)
    setup_fa(app)
    setup_header(app)
    setup_div(app)
    setup_link(app)
    setup_paragraph(app)
    setup_span(app)