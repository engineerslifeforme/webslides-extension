==================================
Development Log
==================================

The documentation is not fantastic on creating a custom
builder for sphinx, so I'm going to attempt to document
my pursuit.  With luck, this will be valuable to others
in the future.

The good news is that there are many examples.  Sphinx
includes many builders, and there are multiple builder
extensions.  The built in sphinx builders do not effectively
demonstrate a standalone builder extension, and many
of the extension builders are quite complicated.
Combining these, the initial learning curve is a little
steep.

Valuable Examples
=======================

- https://github.com/clayrisser/sphinx-jekyll-builder
- https://github.com/clayrisser/sphinx-markdown-builder
- https://github.com/nyergler/hieroglyph
- https://github.com/sphinx-doc/sphinx/tree/5.x/sphinx/builders
- https://github.com/sphinx-doc/sphinx/tree/5.x/sphinx/writers
- http://www.arnebrodowski.de/blog/write-your-own-restructuredtext-writer.html
- https://www.sphinx-doc.org/en/master/extdev/builderapi.html#writing-builders

Initial Package Setup
=======================

Extension package repo organization:

.. code-block::

    EXTENSION_NAME
        docs
        example_doc
        PACKAGE_FOLDER
            __init__.py
            PACKAGE_FOLDER.py
        setup.py

``EXTENSION_NAME`` - Name of the extension, e.g., ``webslides-extension``

``docs`` - Sphinx documentation on how to use the extension.  Use
``sphinx-quickstart`` within this directory.

``example_doc`` - A Sphinx document that demonstrates how to use
the extension.  This will be valuable for testing as well. Use 
``sphinx-quickstart`` in here and add ``PACKAGE_FOLDER`` to the ``extensions``.

``PACKAGE_FOLDER`` - the name of your package, e.g., ``webslides_builder``

``PACKAGE_FOLDER.py`` - the location of the main builder class, e.g., ``webslides_builder.py``

A basic "pip installable" package is a ``setup.py`` which includes:

.. code-block::

    entry_points = {
        'sphinx.builders': [
            'webslides = webslides_builder',
        ],
    }

Bare minimum contents of ``PACKAGE_FOLDER.py`` is:

.. code-block::

    from sphinx.builders import Builder

    class WebslidesBuilder(Builder):
        pass

This package should install with:

.. code-block::

    pip install -e .

within the ``EXTENSION_NAME`` directory.

Build the ``example_doc`` within the ``EXTENSION_NAME`` directory:

.. code-block::

    sphinx-build -b BUILDER_TYPE example_doc/ example_doc/_build/

.. note::

    This will fail with unable to find a builder of the name ``BUILDER_TYPE``.

Making ``BUILDER_TYPE`` Builder Findable
=========================================

Add ``name`` to the builder class in ``PACKAGE_FOLDER.py``, e.g.:

.. code-block::
    :emphasize-lines: 2

    class WebslidesBuilder(Builder):
    name = 'webslides'
    pass

.. note::

    Now we fail with a ``get_outdated_docs`` not implemented.

Adding ``get_outdated_docs``
==============================

Adding ``get_outdated_docs`` to the builder class in ``PACKAGE_FOLDER.py``, e.g.:

.. code-block::

    def get_outdated_docs(self):
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = path.join(self.outdir, docname + self.out_suffix)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except EnvironmentError:
                pass

Also need the following at the top:

.. code-block::

    from os import path

.. note::

    Fails with ``prepare_writing`` not implemented.

Adding ``prepare_writing``
=============================

Now we need a ``Writer``, which is concept from ``docutils``.

Creating ``webslides_writer.py`` (replace with desired type)
next to the existing builder file.  At this point, it is
worth determining whether the desired builder is similar to
an existing builder.  It may make sense to subclass from an
existing writer.  One of the primary purposes of the writer is
to define a Translator which will also define in this file.

Using the built-in ``text`` writer in sphinx as an example,
the writer and translator are subclassed as follows:

Initial contents:

.. code-block::

    from docutils import nodes, writers

    from sphinx.util.docutils import SphinxTranslator

    class WebslidesTranslator(SphinxTranslator):
        pass

    class WebslidesWriter(writers.Writer):
        supported = ('webslides',)
        settings_spec = ('No options here.', '', ())
        settings_defaults: Dict = {}

        output: str = None

        def __init__(self, builder: "WebslidesBuilder") -> None:
            super().__init__()
            self.builder = builder

        def translate(self) -> None:
            visitor = self.builder.create_translator(self.document, self.builder)
            self.document.walkabout(visitor)
            self.output = cast(WebslidesTranslator, visitor).body

Add two things to the builder file, at the top:

.. code-block::

    from .webslides_writer import WebslidesWriter, WebslidesTranslator

To the builder class:

.. code-block::

    def prepare_writing(self, docnames):
        self.writer = WebslidesWriter(self)

.. note::

    Fails with ``write_doc`` not implemented.

Adding ``write_doc``
===========================

Using ``write_doc`` from the jekyll example:

.. code-block::

    def write_doc(self, docname, doctree):
        self.current_docname = docname
        self.secnumbers = self.env.toc_secnumbers.get(docname, {})
        destination = StringOutput(encoding='utf-8')
        self.writer.write(doctree, destination)
        outfilename = path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(path.dirname(outfilename))
        try:
            with open(outfilename, 'w', encoding='utf-8') as f:  # type: ignore
                f.write(self.writer.output)
        except (IOError, OSError) as err:
            logger.warning(__("error writing file %s: %s"), outfilename, err)

And at the top:

.. code-block::

    from docutils.io import StringOutput

.. note::

    Failed with AssertionError: translator not found for webslides