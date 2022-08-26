# General Design

This section discusses some of the design choices for the extension
itself.  

WebSlides makes extensive use unique tags, precise organization and encapsulation of the tagged content, and class attributes.  This
extension attempts to provide all the raw building blocks that
are available when developing WebSlides presentations directly in
HTML, but it also attempts to make intentional additions or
alternatives to allow less verbose slide construction in the
reStructuredText / Sphinx paradigm.

## Output

Direct users of WebSlides create presentations by writing HTML.
HTML is also the primary output format for Sphinx documentation.
In Sphinx terminology, output formats are handled by
[Sphinx Builders](https://www.sphinx-doc.org/en/master/usage/builders/index.html).
This extension is primarily an extension of the default HTML output
builder.  This mainly entails ensuring that specific document elements
are output with the precise tags required by WebSlides.

## WebSlides Elements

As stated earlier, this extension attempts to provide all the building
blocks available in WebSlides for flexibililty and the abililty to 
somewhat easily translate WebSlide HTML content to a Sphinx compatible
formamt like reStructuredText.  While all of the individual components
are available, the extension also attempts to provide assumptions or
options that produce more readable and maintainable slide content.

For example, many common slide formats use a common pattern of tags:

```html
<section class="">
    <div class="wrap">
        <h1>Slide Title</h1>
    </div>
</section>
```

In raw WebSlides HTML, the `<section>` tags are used to identify slides.
The section tag is very frequently followed by a `<div class="wrap">`
tag.

Because the "div wrap" is so common, it is generally handled by default.
Here is the equivalent slide in reStructuredText:

```rst
.. slide::

    # Slide Title
```

`<section>` has been replaced with "slide", and content within the
`slide` directive is "wrapped" by default.  The extension also provides
a markdown-like shorthand for simple headings. The defaults can however
be deactivated to allow building the content is more literally matching
style to the WebSlides HTML.  The example below will create the
equivalent of the 2 above:

```rst
.. slide::
    :no-wrap: True

    .. div-wrap::

        .. heading:: h1
        
            Slide Title
```

There is a more clear one to one mapping of directives to the raw HTML,
but it is also clearly much more verbose and arguably more difficult
to read and write.

Shortcuts are intended to be limited and in service to improved
reading and writing of content.

## Directives and Roles

All simple tags that do not require additional arguments generally
exist as both a role AND a directive to allow flexibility in the
writing content.  In some cases there is additionally an even shorter
role for more minimal in line tagging.  For example, WebSlides provides
a text modifier `text-label`.  WebSlides direct example:

```html
<span class="text-label">Label</span>
```

Below are four different equivalne methods

```rst
.. text-label::

    Label
```

```rst
.. tl::

    Label
```

```rst
:text-label:`Label`
```

```rst
:tl:`Label`
```

Obviously the final version is the most minimalistic for inline use, e.g.

```rst
A minimalistic sentence with a :tl:`Label`.
```

But this format is not suitable if you the text required an additional
directive/tag inside the span, e.g.

```
.. text-label::

    .. additional-directive::

        Label
```

## Classes and Styles

Almost all directives provide an optional `classes` and `style` argument
which allow defining style and adding additional classes to a particular
tag.

Technically an alternative to `div-wrap` could be:

```rst
.. div::
    :classes: wrap

    Some content to be wrapped.
```

Both of these optional arguments are advanced features ideally will only
be used rarely.  `style` similarly provides powerful style modification,
e.g.:

```rst
.. heading:: h1
    :style: color:green;

    A Green Heading h1
```