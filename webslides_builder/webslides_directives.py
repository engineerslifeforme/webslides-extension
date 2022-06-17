from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
 
class slide_class_node(nodes.Text):
    pass

class SlideConfigDirective(SphinxDirective):

    option_spec = {
        'classes': directives.unchanged,
    }

    def run(self):
        new_nodes = []
        for class_name in self.options['classes'].split(' '):
            new_nodes.append(slide_class_node(class_name))
        return new_nodes