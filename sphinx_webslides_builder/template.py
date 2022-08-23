from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.writers.html import HTMLTranslator
import jinja2

environment = jinja2.Environment()

TD = 'template_definitions'

class TemplateDefinitionDirective(SphinxDirective):
    required_arguments = 1
    has_content = True

    def run(self):
        if TD not in self.env.app.config:
            self.env.app.config[TD] = {}
        self.env.app.config[TD][self.arguments[0]] = self.content.data
        return []

class TemplateExecuteDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 10

    def run(self):
        template_parts = []
        index = 0
        while ':' not in self.arguments[index]:
            template_parts.append(self.arguments[index])
            index += 1
        option_data = {self.arguments[i].replace(':', ''): self.arguments[i+1] for i in range(index, len(self.arguments), 2)}

        rendered_content = []
        for template_line in self.env.app.config[TD][' '.join(template_parts)]:
            template = environment.from_string(template_line)
            rendered_content.append(template.render(**option_data))

        return [self._process_content(rendered_content)]
        

    def _process_content(self, content):        
        par = nodes.container()
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