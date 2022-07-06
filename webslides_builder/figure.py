from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    generic_visit,
    generic_depart,
)

TAG = 'figure'

class FigureTranslator(HTMLTranslator):
    """ Figure directive works fine EXCEPT
    webslides uses a "figure" tag around the
    normal stuff
    """

    def visit_figure(self, node):
        generic_visit(self, TAG, node)
        super().visit_figure(node)

    def depart_figure(self, node):
        generic_depart(self, TAG)
        super().depart_figure(node)