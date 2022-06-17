from sphinx.util.docutils import SphinxDirective
from docutils import nodes
 
class slide_class_node(nodes.Text):
    pass

class SlideConfigDirective(SphinxDirective):

    required_arguments = 1

    def run(self):
        return [ slide_class_node(self.arguments[0]) ]