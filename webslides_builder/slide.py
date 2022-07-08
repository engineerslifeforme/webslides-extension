from copy import deepcopy

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.writers.html import HTMLTranslator

from .div import div_wrap_node, div_node
from .span import background_node
from .video import video_node
from .common import (
    add_class_to_tag,
    process_classes,
    GenericDirective,   
    BaseClassNode,
)

SECTION_TAG = 'section'

def setup_slide(app):
    app.add_node(slide_node)
    app.add_directive('slide', Slide)

class slide_node(BaseClassNode):
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
        'wrap-size': directives.unchanged,
        'background-image': directives.unchanged,
        'dark-background-image': directives.unchanged,
        'light-background-image': directives.unchanged,
        'background-image-location': directives.unchanged,
        'background-image-animation': directives.unchanged,
        'background-color': directives.unchanged,
        'vertical-alignment': directives.unchanged,
        'content-alignment': directives.unchanged,
        'card-size': directives.unchanged,
        'card-background': directives.unchanged,
        'flex-content': directives.unchanged,
        'full-screen': directives.unchanged,
        'background-video': directives.unchanged,
        'background-video-poster': directives.unchanged,
        'background-video-dark': directives.unchanged,
    })

    def run(self):
        node = slide_node()
        active_node = node
        # Slide Node modifcations        
        active_node = self.set_horizontal_alignment(active_node)
        active_node = self.set_vertical_alignment(active_node)
        active_node = self.set_class_options(active_node)
        active_node = self.set_background_color(active_node)
        active_node = self.set_full_screen(active_node)
        # Adding child nodes
        # Add before wrap
        active_node = self.set_background_image(active_node)        
        active_node = self.set_background_video(active_node)
        # wrap
        active_node = self.check_wrap(active_node)  
        # after wrap
        active_node = self.check_card(active_node)
        active_node = self._process_content(active_node)      
        return [node]
    
    def set_full_screen(self, node):
        fs = 'full-screen'
        if fs in self.options:
            node.add_class('fullscreen')
        return node
    
    def check_card(self, node):
        cs = 'card-size'
        active_node = node
        if cs in self.options:
            # TODO: probably need to verify size against
            # what is in the CSS
            requested_size = self.options[cs]
            div = div_node()
            node += div
            div.add_class(f'card-{requested_size}')
            active_node = div
            cb = 'card-background'
            if cb in self.options:
                div.add_class(self.options[cb])
        return active_node
    
    def set_background_color(self, node):
        bc = 'background-color'
        if bc in self.options:
            node.add_class(self.options[bc])
        return node

    def set_background_video(self, node):
        bv = 'background-video'
        bvp = 'background-video-poster'
        if bv in self.options:
            video = video_node(
                poster_target=self.options[bvp],
                video_target=self.options[bv],
                dark=('background-video-dark' in self.options),
            )
            node += video
        return node

    def set_background_image(self, node):
        bi = 'background-image'
        if bi in self.options:
            background = background_node()
            background.set_background_image(
                self.options[bi]
            )
            node += background
            if 'dark-background-image' in self.options:
                background.set_dark()
            if 'light-background-image' in self.options:
                background.set_light()
            if 'background-image-animation' in self.options:
                background.set_animation()
            bil = 'background-image-location'
            if bil in self.options:
                background.add_location(self.options[bil])
        return node
    
    def check_wrap(self, node):
        active_node = node
        if 'wrap' in self.options:
            div = div_wrap_node()
            active_node = div
            ws = 'wrap-size'
            if ws in self.options:
                div.add_class(f"size-{self.options[ws]}")
            node += div
        ca = 'content-alignment'
        if ca in self.options:
            div = div_node()
            requested_alignment = self.options[ca]
            good_request = False
            if requested_alignment == 'left':
                div.add_class('content-left')
                good_request = True
            elif requested_alignment == 'center':
                div.add_class('content-center')
                good_request = True
            elif requested_alignment == 'right':
                div.add_class('content-right')
                good_request = True
            else:
                print(f'ERROR: Bad requested content alignment: {requested_alignment}, ignoring...')
            if good_request:
                active_node += div
                active_node = div
        return active_node

    def set_vertical_alignment(self, node):
        va = 'vertical-alignment'
        if va in self.options:
            requested_alignment = self.options[va].lower()
            if requested_alignment == 'top':
                node.add_class('slide-top')
            elif requested_alignment == 'bottom':
                node.add_class('slide-bottom')
            else:
                print(f'ERROR: Vertical alignment {requested_alignment} unknown, ignoring...')
        return node   

        