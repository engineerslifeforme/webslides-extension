# Powerpoint Conversion

The first step to converting an existing powerpoint template to
webslides is to extract the media elements.  The `*.pptx` file
format is actually a compress directory of XML information for
the present + the media.  If you rename the file to .zip and
decompress, a media directory will exist in the decompressed
directory containing all the images used in the presentation
theme.

Depending on how the theme was constructed the media files can
be used to recreate the theme.  For example, if the primary
slide template used a 16x9 image for the background, that
image can also be set as the default for your Webslides
presentation:

```rst
..slide-config
    :background-image: ppt_background.png

    # Slide content
```

Using the `slide-config` directive will automatically apply the
defined styling to all following slides.  In a similar way
complex footers and headers can be constructed using the
`header-config` and `footer-config` directives.

Text styling can be a little more challenging and will likely
require the creation of a custom CSS file which can be included
in the `conf.py`:

```python
html_css_files = [
    'css/custom.css',
]
```

See the :ref:`my-reference-label` section for additional details
on custom CSS recommendations.