from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    process_classes,
    GenericDirective,
    add_attribute_to_tag,
    create_role,
    get_generic_directive,
    add_role_and_directive,
    get_generic_translator_class,
    get_node,
    create_role,
    BaseNode,
    BaseClassNode,
    add_visit_depart,
)

TAG = 'span'

class span_node(BaseClassNode):
    
    def set_background_image(self, url: str):
        self['style'] = f"background-image:url('{url}')"

class text_label_node(BaseClassNode):
    classes = ['text-label']
class span_raw_node(span_node): pass
class background_node(span_node):
    classes=['background']
class dark_background_node(background_node):
    classes= background_node.classes + ['dark']

class BackgroundImageDirective(GenericDirective):
    node_type = background_node
    required_arguments = 1

    def run(self):
        node_list = super().run()
        node_list[0].set_background_image(
            self.arguments[0]
        )
        return node_list

class DarkBackgroundImageDirective(BackgroundImageDirective):
    node_type = dark_background_node

def setup_span(app):
    app.add_node(span_node)
    app.add_node(span_raw_node)
    app.add_node(background_node)
    app.add_node(dark_background_node)
    app.add_node(text_label_node)
    add_role_and_directive(app, span_node, 'span')
    app.add_role('span-raw', raw_span_role)
    add_role_and_directive(app, text_label_node, 'text-label')
    app.add_directive('background-image', BackgroundImageDirective)
    app.add_directive('dark-background-image', DarkBackgroundImageDirective)
    app.add_role('background-image', create_role(background_node))
    app.add_role('dark-background-image', create_role(dark_background_node))

    # Convenience
    add_role_and_directive(app, text_label_node, 'tl')

def raw_span_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = span_raw_node()
    node['content'] = text
    return [node], []

class SpanTranslator(HTMLTranslator):
    
    def visit_span_node(self, node):
        content = f'<{TAG}>'
        content = process_classes(content, node, TAG)
        if 'style' in node:
            content = add_attribute_to_tag(
                content,
                TAG,
                'style',
                node['style']
            )
        self.body.append(content)
    
    def depart_span_node(self, node):
        self.body.append(f'</{TAG}>')

    def visit_span_raw_node(self, node):
        self.body.append(f"<{TAG}>{node['content']}")
    
    def depart_span_raw_node(self, node):
        self.depart_span_node(node)

    def visit_text_label_node(self, node):
        self.visit_span_node(node)

    def depart_text_label_node(self, node):
        self.depart_span_node(node)

