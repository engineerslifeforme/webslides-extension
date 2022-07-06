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

class GridDirective(GenericDirective):
    
    node_type = grid_node
    option_spec = copy.deepcopy(GenericDirective.option_spec)
    option_spec.update({
        'alignment': directives.unchanged
    })

    def run(self):
        node = super().run()[0]
        a = 'alignment'
        if a not in self.options:
            self.options[a] = 'vertical'
        requested_alignment = self.options[a]
        if requested_alignment == 'vertical':
            node.add_class('vertical-align')
        else:
            print(f'ERROR: Unknown grid alignment: {requested_alignment}, ignoring')
        return [node]

div_map = {
    'div': div_node,
    'div-wrap': div_wrap_node,
    'column': column_node,
    'center': center_node,
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

