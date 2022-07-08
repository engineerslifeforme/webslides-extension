import copy

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .common import (
    process_classes,
    GenericDirective,
    generic_visit,
    generic_depart,
    get_node,
    get_generic_directive,
    get_generic_translator_class,
    add_visit_depart,
    add_role_and_directive,
    BaseNode,
    BaseClassNode,
)

TAG = 'div'

class div_node(BaseClassNode): pass
class div_wrap_node(BaseClassNode):
    classes=['wrap']
class grid_node(BaseClassNode):
    classes=['grid']
class column_node(BaseClassNode):
    classes=['column']
class center_node(BaseClassNode):
    classes=['aligncenter']
class flex_content_node(BaseClassNode):
    classes=['flex-content']
class content_left_node(BaseClassNode):
    classes=['content-left']
class overlay_node(BaseClassNode):
    classes=['overlay']

ALLOWED_SIDEBAR_CONFIGS = [
    'sm', 'ms', 'sms'
]
class GridDirective(GenericDirective):
    
    node_type = grid_node
    option_spec = copy.deepcopy(GenericDirective.option_spec)
    option_spec.update({
        'alignment': directives.unchanged,
        'sidebar-config': directives.unchanged,
    })

    def run(self):
        node = super().run()[0]
        a = 'alignment'
        if a in self.options:
            requested_alignment = self.options[a]
            if requested_alignment == 'vertical':
                node.add_class('vertical-align')
            else:
                print(f'ERROR: Unknown grid alignment: {requested_alignment}, ignoring')
        sc = 'sidebar-config'
        if sc in self.options:
            requested_config = self.options[sc].lower()
            if requested_config in ALLOWED_SIDEBAR_CONFIGS:
                node.add_class(requested_config)
        return [node]

div_map = {
    'div': div_node,
    'div-wrap': div_wrap_node,
    'column': column_node,
    'center': center_node,
    'flex-content': flex_content_node,
    'content-left': content_left_node,
    'overlay': overlay_node,
}

def setup_div(app):
    for label in div_map:
        node_type = div_map[label]
        app.add_node(node_type)
        add_role_and_directive(app, node_type, label)
    app.add_node(grid_node)
    app.add_directive('grid', GridDirective)

class DivTranslator(HTMLTranslator):
    pass

add_visit_depart(DivTranslator, grid_node.__name__, TAG)
for node_type in div_map.values():
    add_visit_depart(DivTranslator, node_type.__name__, TAG)

