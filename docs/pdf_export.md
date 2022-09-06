# PDF Export

Similar to PDF export of a normal Sphinx document, an additional
utility is required to produce the PDF.  Unlike a normal document,
an intermediate format (i.e. LaTeX) is not required; the PDF
will be produced from the normal HTML output.

[decktape](https://github.com/astefanutti/decktape) supports conversion
of WebSlides slides to PDF, and it could be used for WebSlides outputs
using Sphinx.  Follow the instructions at the link above to install
`decktape`.

## Steps to Produce PDF

Create slide content and build as normal.

Now execute `decktape` against the HTML output folder.

```bash
decktape -s 1920x1080 /path/to/html_output/deck.html pdfexport.pdf
```

To assure the PDF export looks the same as what was created during
development set the `-s` value to the resolution on which the 
presentation was developed.  This is also an opportunity to see
how the presentation will look in alternative resolutions.

Only absolute paths have been tested for the input HTML.