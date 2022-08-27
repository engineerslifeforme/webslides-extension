# Slide Directive

The `slide` directive is the single required directive within the
extension, i.e. it is impossible to make a slide deck without
using at least one instance of the `slide` directive.

The `slide` directive is used to identify individual slide
content within a the larger slide deck which typically exists
as a single file.

```rst
.. slide::

    # Slide 1

.. slide::

    # Slide 2
```

The `slide` directive produces the `<section>` tag within the
raw WebSlides compatible HTML output.  Keep this in mind when
attempting to convert raw WebSlides HTML to reStructuredText.

The `slide` directive has no required arguments.

All of the examples within this section can be seen in the 
`reference_slide.html` output when building `example_decks`.

## Optional Arguments

The raw HTML WebSlides framework uses a complex combination
of tags immediately inside the slide (section) tag to create
a variety effects.  The design choice was made within this
extension to provide these capabilities as optional arguments
on the `slide` directive as opposed to requiring the writer
to use a large series of directives.  Ideally, this will
improve readability and writability of the slide source.

This section will discuss the effects of each of the optional
arguments.

### `no-wrap`

The `no-wrap` option reduces the margin on the slides.  The
WebSlides very rarely do not utilize wrap hence the default
to on.  Use of `no-wrap` is generally not recommended.

```rst
.. slide::
    :no-wrap: True

    # Slide 2 
```

See `keynote.html` in the `example_decks` for example uses.

### `wrap-size`

`wrap-size` allows increasing the margins around the primary
text.  The number provided reflects the % that will be used,
so smaller numbers will result in a smaller amount of
horizontal space used.

```rst
.. slide::
    :wrap-size: 50

    # Slide 2 
```

### `wrap-zoom-in`

`wrap-zoom-in` changes the slide in transition from the default
of fade to zoom in.

```rst
.. slide::
    :wrap-zoom-in: True

    # Slide 2 
```

### `background-image`

`background-image` image applies a background image to the slide.

```rst
.. slide::
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg

    # Slide 2
```

```{note}
File paths can be used an alternative to URLs, e.g. `_static/images/cool.png`
```

### `dark-background-image`

`dark-background-image` must be used along with `background-image` and
`background-color`.  The `background-color` should be dark like
`bg-black`. The image is slightly darker to improve text readability
with some images.

```{note}
Must be used with `background-image`!
```

```rst
.. slide::
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
    :dark-background-image: True
    :background-color: bg-black

    # Slide 2
```

### `light-background-image`

`light-background-image` is similar to `dark-background-image` in that
it uses the lighter color text.

```{note}
Must be used with `background-image`!
```

```rst
.. slide::
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
    :light-background-image: True
    :background-color: bg-black

    # Slide 2
```

### `background-image-location`

`background-image-location` allows the placement of the background
image.

Currently supported options:

- `right-bottom`
- `left-bottom`

```{note}
Must be used with `background-image`!
```

```rst
.. slide::
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
    :background-image-location: right-bottom

    # Slide 2
```

### `background-image-animation`

`background-image-animation` will animate the background image with a
slow vertical scroll.

```{note}
Must be used with `background-image`!
```

```rst
.. slide::
    :background-image-animation: True
    :background-color: bg-black
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg

    # Slide 2
```

### `background-color`

`background-color` provides simple background color.

```rst
.. slide::
    :background-color: bg-black
    
    # Slide 2
```

### `vertical-alignment`

`vertical-alignment` will set the vertical alignment of text on the
slide.

Supported values:

- top
- bottom
- center

Default is center.

```rst
.. slide::
    :vertical-alignment: bottom

    # Slide 2
```

### `content-alignment`

`content-alignment` sets the horizontal alignment of the text on the
slide.

Supported values:

- left
- center
- right

```rst
.. slide::
    :content-alignment: right

    # Slide 2
```
