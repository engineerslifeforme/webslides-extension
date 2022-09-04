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
    optional_arguments = 1
    has_content = True
    option_spec = {
        'content_mode': directives.unchanged,
    }

    def run(self):
        
        rendered_content = []
        if 'content_mode' not in self.options:
            defined_input = '\n'.join(self.content.data)
            option_data = yaml.safe_load(defined_input)
            for template_line in self.env.app.config[TD][self.arguments[0]]:
                template = environment.from_string(template_line)
                rendered_content.append(template.render(**option_data))
        else:
            for template_line in self.env.app.config[TD][self.arguments[0]]:
                if '{{' in template_line and 'content' in template_line.lower() and '}}' in template_line:
                    char_index = 0
                    while template_line[char_index].isspace():
                        char_index +=1
                    white_space = template_line[0:char_index]
                    for line in self.content.data:
                        rendered_content.append(white_space+line)
                else:
                    rendered_content.append(template_line)

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