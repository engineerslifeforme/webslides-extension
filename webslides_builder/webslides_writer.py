from sphinx.writers.html import HTMLWriter

from .slide import SlideTranslator
from .font_awesome import FontAwesomeTranslator
from .heading import HeadingTranslator
from .header import HeaderTranslator
from .div import DivTranslator
from .span import SpanTranslator
from .paragraph import ParagraphTranslator
from .link import LinkTranslator
from .flexblock import FlexblockTranslator
from .hr import HRTranslator
from .description_list import DescriptionListTranslator
from .preformatted import PreformattedTranslator
from .footer import FooterTranslator
from .figure import FigureTranslator
from .web import WebTranslator

class WebslidesTranslator(
    SlideTranslator,
    HeadingTranslator,
    FontAwesomeTranslator,
    DivTranslator,
    SpanTranslator,
    ParagraphTranslator,
    LinkTranslator,
    FlexblockTranslator,
    HRTranslator,
    DescriptionListTranslator,
    PreformattedTranslator,
    HeaderTranslator,
    FooterTranslator,
    FigureTranslator,
    WebTranslator,
):

    def visit_section(self, node):
        super().visit_section(node)
        # The div section that is added is problematic
        # Removing the div but still running to maintain
        # other state info
        self.body.pop()

    def depart_section(self, node):
        super().depart_section(node)
        # The div section that is added is problematic
        # Removing the div but still running to maintain
        # other state info
        self.body.pop()

    def visit_literal_block(self, node):
        self.body.append(f'<code>')

    def depart_literal_block(self, node):
        self.body.append('</code>')

class WebslidesWriter(HTMLWriter):
    translator_class = WebslidesTranslator