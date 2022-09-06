(content_templating)=

# Content Templating

The `template` and `template-define` directives provide a powerful
capability to hide complexity and avoid redundancy.  Templates
utilize [jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
in the background.

The general pattern to to define a template and it can be used
many times.  This allows content and/or structure and styling to
be managed in a single location.

As stated in content management, you can also considering storing
the `template-define` statements in a separate file to keep the
slide deck itself cleaner and allow sharing within other decks.

## Special Formatted Slides

Templates are especially helpful in complex slides that have
complex formatting, e.g. the title slide.  Using
[jinja Expressions](https://jinja.palletsprojects.com/en/3.1.x/templates/#expressions)
a complex slide can be designed with configurable content
on each usage.

```rst
.. template-define:: cover

    .. slide::
        :background-image: _static/images/cover.png
        :header: PRIVATE
        :footer: PRIVATE

        # {{ title }}

        ### {{ subtitle }}

        **{{ author }}**

.. template:: cover

    title: An Amazing Slide Deck
    subtitle: Using Sphinx and WebSlides
    author: Mysself

.. template:: cover

    title: A second cover
    subtitle: but same formatting
    author: Still Myself
```

In the case of multiple slide decks the `template-define` can be
defined in a separate file and included via `include` directive.
This will allow consistent title slides among multiple decks,
and easy simultaneous changes to all decks.

Data is provided to the `template` in YAML format.

## Configurable Content

jinja + YAML provides quite a bit of flexibility, but in many
cases template are desired for simply slide formatting and
not the content itself.  `content-mode` should be used
for this operation.  In this pattern, `content` is the only
expression that can be used in the `template-define`.  

```{note}
The white space around `{{ content }}` is important because
this is the depth with which the content will be added.
No other jinja constructions or expressions can be used
with this mode.
```

Example:

```rst
.. template-define:: private

    .. slide::
        :header: PRIVATE

        {{ content }}

.. template-define:: public

    .. slide::
        :header: PUBLIC

        {{ content }}

.. template:: private

    # A private slide

.. template:: public

    # A public slide

.. template:: private

    # Another Private Slide
```

## Repeated Static Content

Some content is displayed multiple times through a presentation
without changes.  In WYSIWYG editors, this type of content can
be especially susceptible to human error in making sure all
instances are the same.

```{note}
`include` can also be used for this function when the content
is in a separate file.
```

Example:

```rst
.. template-define agenda

    .. slide::

        # Agenda

        - Topic 1
        - Topic 2
        - Topic 3

.. template:: agenda

..
    Topic 1 slides

.. template:: agenda

..
    Topic 2 slides
```