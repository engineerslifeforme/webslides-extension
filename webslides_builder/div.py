from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    process_classes,
    GenericDirective,
    generic_visit,
    generic_depart,
)

TAG = 'div'

def setup_div(app):
    app.add_node(div_node)
    app.add_node(div_wrap_node)
    app.add_directive('div', DivDirective)
    app.add_directive('div-wrap', DivWrapDirective)

class div_node(nodes.Structural, nodes.Element):
    pass

class DivDirective(GenericDirective):
    node_type = div_node

class div_wrap_node(div_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = ['wrap']

class DivWrapDirective(GenericDirective):
    node_type = div_wrap_node

class DivTranslator(HTMLTranslator):

    def visit_div_node(self, node):
        generic_visit(self, TAG, node)

    def depart_div_node(self, node):
        generic_depart(self, TAG)