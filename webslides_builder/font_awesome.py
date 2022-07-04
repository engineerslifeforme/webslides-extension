from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

def setup_fa(app):
    app.add_node(fa_node)
    app.add_node(fa_span_node)
    app.add_role('fa', fa_role_maker())
    app.add_role('fa_span', fa_role_maker(span=True))
    app.add_directive('font-awesome', FontAwesomeDirective)

class fa_node(nodes.Element):
    pass

class fa_span_node(nodes.Element):
    pass

def fa_role_maker(span=False):
    def fa_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        if span:
            # TODO: this should really add a span node with fa_node inside
            node = fa_span_node()
        else:
            node = fa_node()
        node['fa_type'] = text
        return [node], []
    return fa_role

class FontAwesomeDirective(SphinxDirective):
    required_arguments = 1

    option_spec = {
        'span': directives.unchanged,
    }

    def run(self):
        # TODO: This should be handled better, i.e.
        # span node containing fa node
        if 'span' in self.options:
            node = fa_span_node()
        else:
            node = fa_node()
        node['fa_type'] = self.arguments[0]
        return [node]

class FontAwesomeTranslator(HTMLTranslator):
    
    def visit_fa_node(self, node):
        fa_type = node['fa_type']
        self.body.append(f"""<svg class=\"{fa_type}\">
    <use xlink:href=\"#{fa_type}\"></use>
</svg>""")

    def visit_fa_span_node(self, node):
        self.body.append('<span>')
        self.visit_fa_node(node)

    def depart_fa_node(self, node):
        pass
    
    def depart_fa_span_node(self, node):
        self.body.append('</span>')