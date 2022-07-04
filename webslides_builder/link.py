from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    process_classes,
    GenericDirective,
    add_attribute_to_tag,
    create_role,
    create_directive,
    generic_visit,
    generic_depart,
)

TAG = 'a'

def setup_link(app):
    link_map = {
        'link': link_node,
        'ghost-button': ghost_button_node,
    }
    for label in link_map:
        node_type = link_map[label]
        app.add_node(node_type)
        app.add_role(label, create_role(node_type))
        app.add_directive(label, create_directive(node_type))

class link_node(nodes.Element):
    pass

class ghost_button_node(link_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs):
        self['classes'] = ['ghost', 'button']

class LinkTranslator(HTMLTranslator):

    def visit_link_node(self, node):
        generic_visit(self, TAG, node)

    def depart_link_node(self, node):
        generic_depart(self, TAG)
    
    def visit_ghost_button_node(self, node):
        generic_visit(self, TAG, node)

    def depart_ghost_button_node(self, node):
        generic_depart(self, TAG)