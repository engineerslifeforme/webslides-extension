from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.writers.html import HTMLTranslator
import jinja2
import yaml

environment = jinja2.Environment()

TD = 'template_definitions'

class template_node(nodes.Element): pass

class TemplateDefinitionDirective(SphinxDirective):
    required_arguments = 1
    has_content = True

    def run(self):
        try:
            len(self.env.app.config[TD])
        except AttributeError:
            self.env.app.config[TD] = {}
        self.env.app.config[TD][self.arguments[0]] = self.content.data
        return []

class TemplateExecuteDirective(SphinxDirective):
    required_arguments = 1
    has_content = True

    def run(self):
        option_data = yaml.safe_load('\n'.join(self.content.data))

        rendered_content = []
        for template_line in self.env.app.config[TD][self.arguments[0]]:
            template = environment.from_string(template_line)
            rendered_content.append(template.render(**option_data))

        return [self._process_content(rendered_content)]
        

    def _process_content(self, content):        
        par = template_node()
        self.state.nested_parse(
            ViewList(content, 'populated_template'), 
            self.content_offset, par
        )
        return par

def clear_templates(app, *args):
    """ I want to clear templates for each file.  No persistence"""
    if TD in app.config:
        app.config[TD] = {}

def setup_template(app):
    app.add_directive('template-define', TemplateDefinitionDirective)
    app.add_directive('template', TemplateExecuteDirective)
    app.connect('source-read', clear_templates)

class TemplateTranslator(HTMLTranslator):
    
    def visit_template_node(self, node):
        pass

    def depart_template_node(self, node):
        pass