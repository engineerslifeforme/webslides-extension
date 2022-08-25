# Getting Started

```{note}
The following steps assume the extension has already been
installed
```

Starting a WebSlides presentation via this Sphinx Extension
is exactly the same as a normal Sphinx document, which
is summarized in the following steps:

1. Start a sphinx document
2. Modify the `conf.py`
3. Create content (and add to `index.rst`)
4. Sphinx build the document
5. View generated content

## Starting a Sphinx Document

[Sphinx Getting Started](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
provides instructions on starting a sphinx document; namely:

```bash
sphinx-quickstart
```

Respond to the prompts.  Defaults are fine when available.

## Configuration Modifications

Modifications to the Sphinx configuration file `conf.py` are necessary
to:

1. Enable the WebSlides builder extension which provides WebSlides as an
   output target.
2. Set the Sphinx document theme

### Enable Extension

Within `conf.py` add `sphinx_webslides_builder` to the extensions list.
It should look something like the below, but it may contain additional
items if additional extensions are being used.

```python
extensions = [
    'sphinx_webslides_builder',
]
```

### Configure Document Theme

Within `conf.py` make sure the variable `html_theme` is set as follows:

```python
html_theme = 'webslides_theme'
```

```{note}
Building a custom theme is possible.  As with theme development on normal
Sphinx documents, it is recommended the included WebSlides theme be
extended.  In general though, it is not expected that theme extension
will be necessary.  Styling is highly configurable through a custom
CSS file and content layout is highly configurable through the document
content itself.
```

## Content Creation

Slide content is created very similarly to how it is described in the
Sphinx Getting Started documentation referenced above.  Create a new
file, e.g. `content.rst` and begin adding content.  Example:

```rst
.. slide::

  # A Title

  - Content A
  - Content B

.. slide::

  # A second slide

  With paragraph content
```

```{note}
It is NOT necessary to add `content.rst` to the `index.rst` as in a
typical Sphinx document.  It is however necessary that `index.rst`
exist, but modifications are not required.
```

By default each individual `*.rst` file will create a separate
presentation.

## Build Slides

Building the slides is very similar to normal [Sphinx document build](https://www.sphinx-doc.org/en/master/usage/quickstart.html#running-the-build) of the form:

```bash
sphinx-build -b builder sourcedir builddir
```

In this case the builder will be `webslides`.

For example the `example_decks` directory within this repository
can be built as follows:

```
sphinx-build -b webslides example_decks example_decks/_webslides_build
```

This command must be executed within the top level directory of the
repository as written.

The results will be placed at `example_decks/_webslides_build`

## Viewing / Presenting the Results

Within the defined `builddir`, there will be a corresponding `*.html`
file for each `*.rst` content file that was created.  And as stated
earlier, each of these resultant `*.html` is an individual presentation.
Simply open the HTML file in your browser of choice.
