from bs4 import BeautifulSoup
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

def add_class_to_tag(html: str, tag_name: str, class_name: str) -> str:
    return add_attribute_to_tag(html, tag_name, 'class', class_name)

def add_attribute_to_tag(html: str, tag_name: str, attribute_name: str, value: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    soup.find(tag_name)[attribute_name] = soup.find(tag_name).get(attribute_name, []) + [value]
    # bs4 adds a close tag, removing
    return str(soup).replace(f'</{tag_name}>', '')

def process_classes(content: str, node, tag_name: str) -> str:
    for class_name in node['classes']:
        content = add_class_to_tag(
            content, tag_name, class_name
        )
    return content

def create_role(node_type, classes: list = None):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        node = node_type()
        if classes is not None:
            node['classes'] = classes
        node += nodes.Text(text)
        return [node], []
    return role

class GenericDirective(SphinxDirective):
    option_spec = {
        'classes': directives.unchanged,
    }
    has_content = True

    def run(self):
        node = self.node_type()
        return self.generic_process(node)

    def generic_process(self, node):
        node = self._process_classes(node)
        if self.has_content:
            node = self._process_content(node)
        return [node]

    def _process_classes(self, node):
        if 'classes' not in node:
            node['classes'] = []
        if 'classes' in self.options:
            node['classes'] = self.options['classes'].split(' ')
        return node
    
    def _process_content(self, node):        
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        node += par
        return node

def create_directive(requested_node_type):
    class SimpleDirective(GenericDirective):
        node_type = requested_node_type

    return SimpleDirective

def generic_visit(translator, tag: str, node):
    content = f'<{tag}>'
    content = process_classes(content, node, tag)
    translator.body.append(content)

def generic_depart(translator, tag):
    translator.body.append(f'</{tag}>')
