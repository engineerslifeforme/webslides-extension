from typing import (TYPE_CHECKING, Any, Dict, Generator, Iterable, List, Optional, Set, Tuple,
                    Union, cast)
                    
from sphinx.util.docutils import SphinxTranslator
from sphinx.writers.html import HTMLWriter, HTMLTranslator
#from sphinx.writers.html import HTMLWriter
#from docutils.writers.html4css1 import HTMLTranslator, HTMLWriter
from bs4 import BeautifulSoup

from docutils import nodes, writers

from .page_template import get_page

class WebslidesTranslator(HTMLTranslator):
    slide_open = False

    def visit_slide_class_node(self, node):
        index = -1
        current_element = self.body[index]
        while '<section' not in current_element:
            index -= 1
            current_element = self.body[index]
        soup = BeautifulSoup(current_element, 'html.parser')
        soup.find('section')['class'] = soup.find('section').get('class', []) + [node.astext()]
        # bs4 adds a close tag, removing
        self.body[index] = str(soup).replace('</section>', '')
        #pass

    def depart_slide_class_node(self, node):
        pass

    def visit_section(self, node):
        super().visit_section(node)
        # The div section that is added is problematic
        # Removing the div but still running to maintain
        # other state info
        self.body.pop()

    def depart_section(self, node):
        super().depart_section(node)
        # The div section that is added is problematic
        # Removing the div but still running to maintain
        # other state info
        self.body.pop()

    def visit_title(self, node):
        # Having an issue where slides would be immediately closed
        if self.slide_open:
            self.body.append("</section>")
        self.body.append("<section>")
        self.slide_open = True
        super().visit_title(node)

    def visit_literal_block(self, node):
        self.body.append(f'<code>')

    def depart_literal_block(self, node):
        self.body.append('</code>')

class WebslidesWriter(HTMLWriter):
    translator_class = WebslidesTranslator
