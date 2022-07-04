from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    process_classes,
    GenericDirective,
    add_attribute_to_tag,
    create_role,
)

TAG = 'span'

def setup_span(app):
    app.add_node(span_node)
    app.add_node(span_raw_node)
    app.add_node(background_node)
    app.add_node(dark_background_node)
    app.add_directive('span', SpanDirective)
    app.add_directive('background-image', BackgroundImageDirective)
    app.add_directive('dark-background-image', DarkBackgroundImageDirective)
    app.add_role('span', create_role(span_node))
    app.add_role('span-raw', raw_span_role)
    app.add_role('text-label', span_text_label_role)
    app.add_role('text-label', create_role(span_node, classes=['text-label']))
    app.add_role('background-image', background_image_role_maker(background_node))
    app.add_role('dark-background-image', background_image_role_maker(dark_background_node))

class span_node(nodes.Element):
    pass

    def set_background_image(self, url: str):
        self['style'] = f"background-image:url('{url}')"

class span_raw_node(nodes.Element):
    pass

class SpanDirective(GenericDirective):
    node_type = span_node

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

class background_node(span_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = [
            'background',
        ]

class dark_background_node(background_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = self['classes'] + [
            'dark',
        ]

class BackgroundImageDirective(GenericDirective):
    node_type = background_node
    required_arguments = 1

    def run(self):
        node_list = super().run()
        node_list[0].set_background_image(
            self.arguments[0]
        )
        return node_list

def background_image_role_maker(node_type):
    def background_image_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        node = node_type()
        return [node], []
    return background_image_role

class DarkBackgroundImageDirective(BackgroundImageDirective):
    node_type = dark_background_node