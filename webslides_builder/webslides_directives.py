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

class div_node(nodes.Structural, nodes.Element):
    pass

class Div(SphinxDirective):
    has_content = True
    option_spec = {
        'classes': directives.unchanged,
    }

    def run(self):
        node = div_node()
        if 'classes' in self.options:
            node['classes'] = self.options['classes'].split(' ')
        else:
            node['classes'] = []
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        node += par
        return [node]

class flexblock_list_node(nodes.Element):
    pass

class FlexBlock(SphinxDirective):
    has_content = True
    option_spec = {
        'classes': directives.unchanged,
    }

    def run(self):
        this_node = flexblock_list_node()
        this_node['classes'] = []
        if 'classes' in self.options:
            for class_name in self.options['classes'].split(' '):
                this_node['classes'].append(class_name)
        new_nodes = [
            this_node
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

class pseudo_heading_node(nodes.Element):
    pass

def pseudo_heading_role(tag: str):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        node = pseudo_heading_node()
        node += nodes.Text(text)
        node['tag'] = tag
        return [node], []
    return role

class span_node(nodes.Element):
    pass

class span_raw_node(nodes.Element):
    pass

def span_roles(raw=False):
    def span_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        if raw:
            node = span_raw_node()
            node['content'] = text
        else:
            node = span_node()
            node += nodes.Text(text)
        return [node], []
    return span_role

class fa_node(nodes.Element):
    pass

def fa_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = fa_node()
    node['fa_type'] = text
    return [node], []

class generic_node(nodes.Element):
    pass

class GenericDirective(SphinxDirective):

    option_spec = {
        'attribute_names': directives.unchanged,
        'attribute_values': directives.unchanged,
    }
    has_content = True
    required_arguments = 1

    def run(self):
        node = generic_node()
        node['tag'] = self.arguments[0]
        if 'attribute_names' in self.options:
            node['attribute_names'] = self.options['attribute_names'].split(' ')
            node['attribute_values'] = self.options['attribute_values'].split(' ')
        else:
            node['attribute_names'] = []
            node['attribute_values'] = []
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        node += par
        return [node]
        
