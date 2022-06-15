from typing import (TYPE_CHECKING, Any, Dict, Generator, Iterable, List, Optional, Set, Tuple,
                    Union, cast)
                    
from sphinx.util.docutils import SphinxTranslator
from sphinx.writers.html import HTMLWriter, HTMLTranslator
#from sphinx.writers.html import HTMLWriter
#from docutils.writers.html4css1 import HTMLTranslator, HTMLWriter

from docutils import nodes, writers

from .page_template import get_page

#class WebslidesTranslator(HTMLTranslator):
class WebslidesTranslator(SphinxTranslator):

    body = []
    meta = ['a', 'b', 'c', 'd']
    
    @property
    def merged_body(self) -> str:
        return ''.join(self.body)
    
    def astext(self):
        return "astext output"

    def visit_title(self, node) -> None:
        self.body.append(f'<h1>{node.astext()}')

    def depart_title(self, node) -> None:
        self.body.append('</h1>')

    def visit_Text(self, node):
        pass

    def depart_Text(self, node):
        self.body.append(node.astext())

    def visit_document(self, node):
        pass

    def depart_document(self, node):
        pass

    def visit_paragraph(self, node):
        pass

    def depart_paragraph(self, node):
        pass

    def visit_section(self, node):
        self.body.append("<section>")

    def depart_section(self, node):
        self.body.append("</section>")

    def visit_comment(self, node):
        pass

    def depart_comment(self, node):
        pass

    def visit_reference(self, node):
        pass

    def depart_reference(self, node):
        pass

    def visit_list_item(self, node):
        pass

    def depart_list_item(self, node):
        pass

    def visit_bullet_list(self, node):
        pass

    def depart_bullet_list(self, node):
        pass

    def visit_compound(self, node):
        pass

    def depart_compound(self, node):
        pass

#class WebslidesWriter(HTMLWriter):
class WebslidesWriter(writers.Writer):
    translator_class = WebslidesTranslator

    def __init__(self, builder):
        super().__init__()
        self.builder = builder

    def translate(self) -> None:
        visitor = self.builder.create_translator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = get_page(body=cast(WebslidesTranslator, visitor).merged_body)