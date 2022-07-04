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

TAG = 'p'

def setup_paragraph(app):
    paragraph_map = {
        'paragraph': paragraph_node,
        'text-subtitle': text_subtitle_node,
        'text-symbols': text_symbols_node,
        'text-intro': text_intro_node,
    }
    for label in paragraph_map:
        node_type = paragraph_map[label]
        app.add_node(node_type)
        app.add_role(label, create_role(node_type))
        app.add_directive(label, create_directive(node_type))

class paragraph_node(nodes.Element):
    pass

class text_subtitle_node(paragraph_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = ['text-subtitle']

class text_symbols_node(paragraph_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = ['text-symbols']

class text_intro_node(paragraph_node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['classes'] = ['text-intro']

class ParagraphTranslator(HTMLTranslator):
    
    def visit_paragraph_node(self, node):
        generic_visit(self, TAG, node)
    
    def depart_paragraph_node(self, node):
        generic_depart(self, TAG)
    
    def visit_text_symbols_node(self, node):
        generic_visit(self, TAG, node)
    
    def depart_text_symbols_node(self, node):
        generic_depart(self, TAG)
    
    def visit_text_subtitle_node(self, node):
        generic_visit(self, TAG, node)
    
    def depart_text_subtitle_node(self, node):
        generic_depart(self, TAG)
    
    def visit_text_intro_node(self, node):
        generic_visit(self, TAG, node)
    
    def depart_text_intro_node(self, node):
        generic_depart(self, TAG)