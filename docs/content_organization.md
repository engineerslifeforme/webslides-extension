(content_organization)=

# Content Organization

Sphinx offers many options and approaches to content management.
This section is intended to provide some conventions to consider
that may aid in better reuse of slide content and managing some
of the more complex elements of slide definition.

## `_static` Directory

By default `sphinx-quickstart` will create a `_static` directory
to store static assets, e.g. images, custom CSS, etc.  Custom
CSS files, images, videos, and really any non-source text file
should be stored in this directory.

The `_static` directory is also a good location to put submodules
to common content.  Some of the techniques described in the
following section will allow the separation of real slide content
and slide style/theme.  With this separation, it is then possible
to store the style/theme in its own repository which can be
shared among multiple projects to create consistently styled
presentations.  It can also potentially assist and updating content
to a new slide style/theme.

## `include` Directive

Sphinx provides the `include` directive to literally include content.
Combining `include` and {ref}`slide_config_directive`, we can move
the "theme" of the presentation into a reuseable file.  Consider
the two example files below

**`theme.rst`**

```rst
.. slide-config::
    :header: IMPORTANT
    :footer: CRITICAL
    :background-color: bg-apple
```

**`deck.rst`**

```rst
.. include:: theme.rst

.. slide::

    This slide will follow the theme defined in theme.rst
```

This type of approach can also be helpful when using complex
footers and headers.

Now that most of the theme/style has been separated from the content
of this specific presentation, the `theme.rst` could be moved to
a totally separate respository that could be reduced in multiple
deck repositories via a 
[git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
or similar technique.  Submodules are nice in this use case because
update can be made to theme, but consuming repos will not automatically
adopt the changes without a manual update of the submodule.  In
other words, it is easy to get updates and fixes, but they will not
surprise or appear at undesired times.

Example of `deck.rst` if the `theme.rst` were in `_static/theme_repo`
as a submodule might appear:

```rst
.. include:: _static/theme_repo/theme.rst

.. slide::

    This slide will follow the theme defined in theme.rst
```

### `exclude_patterns`

When creating files with source content that will not be added to
`index.rst` as its own page, consider using a file name convention
in conjunction with the 
[`exclude_patterns`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-exclude_patterns)
option in `conf.py`.  This can reduce warnings shown by Sphinx
during slide compilation.

An example convention would be to prepend filenames that will only
be included with `part_`, and then adding an exclusion to `conf.py`
like:

```python
exclude_patterns = ['part_*']
```

This `conf.py` modification is not required, but any source files
that are not included in the `index.rst` will produce a warning
during Sphinx compilation of the slides.

## Template Organization

Templates are more thoroughly described in {ref}`content_templating`,
but this section is an approriate location to discuss a convention
for organizing templates.

Continuing with the `theme.rst` and `deck.rst` example above, the
`theme.rst` file is a convenient place to define slide templates.

Common template use cases are title slides and final contact slides.
Like the reusable theme elements, templates are likely be to be
reused across multiple slide decks, so they will also benefit
from the source separation and separate repo sharing opportunities
discussed above.  The content below could be added to `theme.rst`:

```rst
.. template-define:: cover

    .. slide::

        .. content-left::

            .. image:: _static/images/company_logo.png

        .. content-left::

            # {{ title }}

            ### {{ subtitle }}

            {{ author_name }}

            {{ author_email }}

.. template-define:: contact

    .. slide::
        :background-image: _static/images/contact.png
        :horizontal-alignment: center
        :verticcal-alignment: center

        {{ author_name }}

        {{ author_email }}
```

Then these templates can be used from any deck and repository
that includes theme.  `deck.rst`:

```rst
.. include:: _static/theme_repo/theme.rst

.. template:: cover

    title: Amazing Presentation
    subtitle: Using WebSlides!
    author_name: Talented Individual
    author_email: me@awesome.com

.. slide::

    Many slides of an awesome presentation

.. template:: contact

    author_name: Talented Individual
    author_email: me@awesome.com
```


