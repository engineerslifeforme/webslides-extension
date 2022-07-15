from os import path

from .webslides_builder import WebslidesBuilder
from .slide import setup_slide
from .font_awesome import setup_fa
from .heading import setup_heading
from .header import setup_header
from .div import setup_div
from .link import setup_link
from .paragraph import setup_paragraph
from .span import setup_span
from .flexblock import setup_flexblock
from .hr import setup_hr
from .description_list import setup_description_list
from .preformatted import setup_preformatted
from .footer import setup_footer
from .web import setup_web
from .video import setup_video
from .blockquote import setup_blockquote

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
    setup_flexblock(app)
    setup_hr(app)
    setup_description_list(app)
    setup_preformatted(app)
    setup_heading(app)
    setup_footer(app)
    setup_web(app)
    setup_video(app)
    setup_blockquote(app)