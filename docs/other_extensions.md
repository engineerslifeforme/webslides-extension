# Other Extensions

One of the benefits of using Sphinx is the additional extensions
that are available.  Also, since the WebSlides extension outputs
in HTML like the default Sphinx behavior, many of the extensions
will work quite well since they are also targetted at HTML outputs.

Using other extensions typically requires individual installation
of the extension, adding it to the extension list, and any
additional recommend configuration within `conf.py`.

## Markdown

While Sphinx does have some basic markdown capabilities out of the
box, [MyST](https://myst-parser.readthedocs.io/en/latest/) is the
recommended robust solution for markdown in Sphinx documents, and
it is necessary to utilize an extension like the WebSlides builder
which utilizes a lot of directives.

```{note}
The primary author of the WebSlides extension almost exclusively
uses MyST for typical Sphinx documentation, but reStructuredText
was actually preferred for WebSlides due to the frequent use
of directives.
```

## Kroki Diagrams

Another type of extension that can be used in conjunction with the
WebSlides builder are diagram extensions like 
[sphinxcontrib-kroki](https://github.com/sphinx-contrib/kroki)
which is a Sphinx extension providing directives to utilize an
instance of the [kroki](https://kroki.io/) API service.

Extensions like kroki can provide inline text diagram definition or
direct reuse of diagrams designed for Sphinx documentation.  These
text based solutions are very friendly to configuration management
which is also a key motivator for using the Sphinx WebSlides builder.