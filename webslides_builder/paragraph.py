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
)

TAG = 'p'

class paragraph_node(BaseNode): pass
class text_subtitle_node(BaseClassNode, paragraph_node):
    classes=['text-subtitle']
class text_symbols_node(BaseClassNode, paragraph_node):
    classes=['text-symbols']
class text_intro_node(BaseClassNode, paragraph_node):
    classes=['text-intro']
class text_center_node(BaseClassNode, paragraph_node):
    classes=['aligncenter']

paragraph_map = {
    'paragraph': paragraph_node,
    'text-subtitle': text_subtitle_node,
    'text-symbols': text_symbols_node,
    'text-intro': text_intro_node,
    'text-center': text_center_node,
}

def setup_paragraph(app):
    for label in paragraph_map:
        node_type = paragraph_map[label]
        app.add_node(node_type)
        add_role_and_directive(app, node_type, label)
    # Convenience label
    add_role_and_directive(app, text_intro_node, 'ti')
    add_role_and_directive(app, text_center_node, 'c')

class ParagraphTranslator(HTMLTranslator):
    pass

for thing in paragraph_map.values():
    add_visit_depart(
        ParagraphTranslator,
        thing.__name__,
        TAG,
    )