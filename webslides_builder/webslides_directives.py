from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
 
class slide_class_node(nodes.Text):
    pass

ALLOWED_SIZES = [
    '20',
    '30',
    '40',
    '50',
    '60',
    '70',
    '80',
]

class slide_size_node(nodes.Text):
    pass

class flexblock_feature_list_node(nodes.Structural, nodes.Element):
    pass

class FlexBlockFeatures(SphinxDirective):
    has_content = True

    def run(self):
        new_nodes = [
            flexblock_feature_list_node()
        ]
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        new_nodes.append(par)
        return new_nodes

class SlideConfigDirective(SphinxDirective):

    option_spec = {
        'classes': directives.unchanged,
        'size': directives.unchanged,
    }

    def run(self):
        new_nodes = []
        if 'classes' in self.options:
            for class_name in self.options['classes'].split(' '):
                new_nodes.append(slide_class_node(class_name))
        if 'size' in self.options:
            requested_size = self.options['size']
            if requested_size not in ALLOWED_SIZES:
                print(f'Slide size {requested_size} not allowed!  Ignoring...')
            else:
                new_nodes.append(slide_size_node(requested_size))
        return new_nodes