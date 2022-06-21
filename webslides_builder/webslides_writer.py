from typing import (TYPE_CHECKING, Any, Dict, Generator, Iterable, List, Optional, Set, Tuple,
                    Union, cast)
                    
from sphinx.util.docutils import SphinxTranslator
from sphinx.writers.html import HTMLWriter, HTMLTranslator
#from sphinx.writers.html import HTMLWriter
#from docutils.writers.html4css1 import HTMLTranslator, HTMLWriter
from bs4 import BeautifulSoup

from docutils import nodes, writers

from .page_template import get_page

def find_previous_index(str_list: list, match: str) -> int:
    index = -1
    current_element = str_list[index]
    while match not in current_element:
        index -= 1
        current_element = str_list[index]
    return index

def add_class_to_tag(html: str, tag_name: str, class_name: str) -> str:
    return add_attribute_to_tag(html, tag_name, 'class', class_name)

def add_attribute_to_tag(html: str, tag_name: str, attribute_name: str, value: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    soup.find(tag_name)[attribute_name] = soup.find(tag_name).get(attribute_name, []) + [value]
    # bs4 adds a close tag, removing
    return str(soup).replace(f'</{tag_name}>', '')

class WebslidesTranslator(HTMLTranslator):
    slide_open = False
    slide_size_open = False
    flexblock_open = False
    flexblock_feature = False

    def visit_slide_class_node(self, node):
        index = find_previous_index(self.body, '<section')
        current_element = self.body[index]
        self.body[index] = add_class_to_tag(current_element, 'section', node.astext())

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
            if self.slide_size_open:
                self.slide_size_open = False
                self.body.append("</div>")
            self.body.append("</section>")
        self.body.append("<section>")
        self.slide_open = True
        super().visit_title(node)

    def visit_literal_block(self, node):
        self.body.append(f'<code>')

    def depart_literal_block(self, node):
        self.body.append('</code>')

    def visit_slide_size_node(self, node):
        index = find_previous_index(self.body, '<section')
        self.body.insert(index+1, f"<div class=\"wrap size-{node.astext()}\">")
        self.slide_size_open = True

    def depart_slide_size_node(self, node):
        pass

    def visit_flexblock_feature_list_node(self, node):
        self.flexblock_open = True
        self.flexblock_feature = True
    
    def visit_flexblock_list_node(self, node):
        self.flexblock_open = True

    def depart_flexblock_feature_list_node(self, node):
        pass
    
    def depart_flexblock_list_node(self, node):
        pass

    def visit_bullet_list(self, node):
        super().visit_bullet_list(node)
        if self.flexblock_open:
            self.body[-1] = add_class_to_tag(self.body[-1], 'ul', 'flexblock')
            if self.flexblock_feature:
                self.body[-1] = add_class_to_tag(self.body[-1], 'ul', 'features')
            self.flexblock_open = False
            self.flexblock_feature = False

    def visit_div_node(self, node):
        self.body.append('<div>')
        for class_name in node['classes']:
            self.body[-1] = add_class_to_tag(
                self.body[-1],
                'div',
                class_name,
            )

    def depart_div_node(self, node):
        self.body.append('</div>')

    def visit_div_class_node(self, node):
        index = find_previous_index(self.body, '<div')
        self.body[index] = add_class_to_tag(
            self.body[index],
            'div',
            node.astext(),
        )

    def visit_pseudo_heading_node(self, node):
        self.body.append(f"<{node['tag']}>")
    
    def depart_pseudo_heading_node(self, node):
        self.body.append(f"</{node['tag']}>")

    def visit_span_node(self, node):
        self.body.append('<span>')
    
    def depart_span_node(self, node):
        self.body.append('</span>')

    def visit_span_raw_node(self, node):
        self.body.append(f"<span>{node['content']}")
    
    def depart_span_raw_node(self, node):
        self.body.append("</span>")

    def visit_generic_node(self, node):
        new_tag = f"<{node['tag']}>"
        for index, attribute_name in enumerate(node['attribute_names']):
            new_tag = add_attribute_to_tag(
                new_tag,
                node['tag'],
                attribute_name,
                node['attribute_values'][index],
            )
        self.body.append(new_tag)

    def depart_generic_node(self, node):
        self.body.append(f"</{node['tag']}>")

class WebslidesWriter(HTMLWriter):
    translator_class = WebslidesTranslator
