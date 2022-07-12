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
    get_node,
    get_generic_translator_class,
    add_role_and_directive,
    BaseNode,
    BaseClassNode,
    add_visit_depart,
    process_style,
)

TAG = 'a'

class link_node(BaseNode): pass
class ghost_button_node(BaseClassNode):
    classes=['ghost', 'button']

def setup_link(app):
    app.add_node(link_node)
    app.add_node(ghost_button_node)
    app.add_directive('link', LinkDirective)
    app.add_directive('ghost-button-link', GhostButtonLinkDirective)
    app.add_role('ghost-button-link', ghost_button_role)

class LinkDirective(GenericDirective):
    required_arguments = 1
    node_type = link_node

    def run(self):
        node = super().run()[0]
        node['target'] = self.arguments[0]
        return [node]

class GhostButtonLinkDirective(LinkDirective):
    node_type = ghost_button_node    

def ghost_button_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = ghost_button_node()
    node['target'] = text
    return [node], []

class LinkTranslator(HTMLTranslator):
    
    def visit_link_node(self, node):
        content = f"<{TAG} href=\"{node['target']}\">"
        content = process_classes(content, node, TAG)
        content = process_style(content, node, TAG)
        self.body.append(content)

    def depart_link_node(self, node):
        generic_depart(self, TAG)

    def visit_ghost_button_node(self, node):
        self.visit_link_node(node)

    def depart_ghost_button_node(self, node):
        generic_depart(self, TAG)
