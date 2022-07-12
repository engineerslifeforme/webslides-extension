from copy import deepcopy

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .div import div_wrap_node
from .span import span_node
from .common import (
    BaseNode,
    add_role_and_directive,
    add_visit_depart,
    GenericDirective,
)

TAG = 'header'

class header_node(BaseNode): pass

class HeaderDirective(GenericDirective):
    node_type = header_node

    def run(self):
        node = header_node()
        div = div_wrap_node()
        node += div
        active_node = div
        ha = 'horizontal-alignment'
        if ha in self.options:
            requested_alignment = self.options[ha].lower()
            good_alignment = False
            # TODO: can it do center?
            if requested_alignment == 'right':
                class_alignment = 'alignright'
                good_alignment = True
            elif requested_alignment == 'left':
                class_alignment = 'alignleft'
                good_alignment = True
            else:
                print(f'ERROR: Bad requested footer alignment {requested_alignment}, ignoring...')
            if good_alignment:
                span = span_node()
                span.add_class(class_alignment)
                div += span
                active_node = span
            del(self.options[ha])
        self._process_content(active_node)
        return [node]


def setup_header(app):
    app.add_node(header_node)
    app.add_directive('header', HeaderDirective)

class HeaderTranslator(HTMLTranslator):
    pass

add_visit_depart(HeaderTranslator, header_node.__name__, TAG)