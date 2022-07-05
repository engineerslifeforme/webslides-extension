import copy

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    add_class_to_tag,
    GenericDirective,
    BaseNode,
    BaseClassNode,
)

class flexblock_list_node(BaseNode): pass
class flexblock_list_border_node(BaseClassNode, flexblock_list_node):
    classes = ['border']
class FlexblockDirective(GenericDirective):
    node_type = flexblock_list_node
class FlexblockBorderDirective(GenericDirective):
    node_type = flexblock_list_border_node

def setup_flexblock(app):
    app.add_node(flexblock_list_node)
    app.add_directive('flexblock', FlexblockDirective)
    app.add_directive('flexblock-border', FlexblockBorderDirective)

class FlexblockTranslator(HTMLTranslator):
    flexblock_open = False
    flexblock_classes = []
    description_list_open = False

    def visit_flexblock_list_node(self, node):
        self.flexblock_open = True
        self.flexblock_classes = copy.deepcopy(node['classes'])

    def depart_flexblock_list_node(self, node):
        pass

    def visit_flexblock_list_border_node(self, node):
        self.visit_flexblock_list_node(node)

    def depart_flexblock_list_border_node(self, node):
        self.depart_flexblock_list_node(node)

    def visit_bullet_list(self, node):
        # TODO: not sure how to handle this better
        # Not portable as written
        # Could consider combining
        if not self.description_list_open:
            super().visit_bullet_list(node)
            if self.flexblock_open:
                self.body[-1] = add_class_to_tag(self.body[-1], 'ul', 'flexblock')
                for class_name in self.flexblock_classes:
                    self.body[-1] = add_class_to_tag(self.body[-1], 'ul', class_name)
                self.flexblock_open = False
                self.flexblock_classes = []
