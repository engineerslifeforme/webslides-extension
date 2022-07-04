from copy import deepcopy

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .div import div_wrap_node
from .span import background_node, dark_background_node
from .common import (
    add_class_to_tag,
    process_classes,
    GenericDirective,   
)

SECTION_TAG = 'section'

def setup_slide(app):
    app.add_node(slide_node)
    app.add_directive('slide', Slide)

class slide_node(nodes.Element):
    pass

class SlideTranslator(HTMLTranslator):
    slide_open = False
    
    def visit_slide_node(self, node):
        if self.slide_open:
            self.body.append(f'</{SECTION_TAG}>')
        content = process_classes(f'<{SECTION_TAG}>', node, SECTION_TAG)
        self.body.append(content)

    def depart_slide_node(self, node):
            self.body.append('</section>')
            self.slide_open = False 

class Slide(GenericDirective):
    node_type = slide_node
    option_spec = deepcopy(GenericDirective.option_spec)
    option_spec.update({
        'wrap': directives.unchanged,
        'background-image': directives.unchanged,
        'dark-background-image': directives.unchanged,
    })

    def run(self):
        node = slide_node()
        if 'background-image' in self.options:
            background = background_node()
            background.set_background_image(
                self.options['background-image']
            )
            node += background
        if 'dark-background-image' in self.options:
            background = dark_background_node()
            background.set_background_image(
                self.options['dark-background-image']
            )
            node += background
        if 'wrap' in self.options:
            div = div_wrap_node()
            node += div
        return self.generic_process(node)