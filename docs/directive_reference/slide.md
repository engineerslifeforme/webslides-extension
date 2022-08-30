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

### `card-size`

`card-size` allows the use of the WebSlides `.card` class features. 
Typically used to present an image with structured data to the side,
e.g.:

```rst
.. slide::
    :card-size: 50

    .. figure:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
        :class: aligncenter

    .. flex-content::

        # Slide 2
        
        :ti:`Sphinx`

        An ancient structure in Egypt.
```

```{note}
`figure` MUST be used for the image as opposed to `image`.
```

To put the picture on the right simply change the order of the content.

Different sizes will adjust the amount used by the image.

```rst
.. slide::
    :card-size: 60

    .. flex-content::

        # Slide 2
        
        :ti:`Sphinx`

        ``card-size`` = 60
        
    .. figure:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
        :class: aligncenter
```

### `card-background`

`card-background` sets the background color of the card to differentiate
from the background.

```rst
.. slide::
    :background-color: bg-apple
    :card-size: 60
    :card-background: bg-white

    .. flex-content::

        # Slide 2
        
        :ti:`Sphinx`

        ``card-size`` = 60
        
    .. figure:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
        :class: aligncenter
```

### `full-screen`

`full-screen` is used in combination with a video to display it as a
full-screen video.  It can be used with both youtube videos and normal
`background-video`s.

```{note}
This is one of the rare situations where `no-wrap` can/should be used.
```

```rst
.. slide::
    :full-screen: True
    :no-wrap: True

    .. youtube:: WuHSBSLK3_A
```

```rst
.. slide::
    :full-screen: True
    :no-wrap: True
    :background-video: https://webslides.tv/static/videos/peggy.mp4
    :background-video-poster: https://webslides.tv/static/images/peggy.jpg
```

### `background-video`

`background-video` produces a video as the background for the slide.
Typically used with `full-screen` and `back-video-poster`.

```rst
.. slide::
    :full-screen: True
    :no-wrap: True
    :background-video: https://webslides.tv/static/videos/peggy.mp4
    :background-video-poster: https://webslides.tv/static/images/peggy.jpg
```

### `background-video-poster`

It is not clear what the effects of NOT using `background-video-poster`
with `background-video` are.  The video appears to function exactly
the same.  WebSlides examples typically use them together.

```rst
.. slide::
    :full-screen: True
    :no-wrap: True
    :background-video: https://webslides.tv/static/videos/peggy.mp4
    :background-video-poster: https://webslides.tv/static/images/peggy.jpg
```

### `background-video-dark`

`background-video-dark` can make the video opaque for easier reading
of the text.  `background-color` should be used simultaneously as 
shown below.

```rst
.. slide::
    :full-screen: True
    :background-video: https://webslides.tv/static/videos/peggy.mp4
    :background-video-dark: True
    :background-color: bg-apple

    # Slide 2
```

### `text-serif`

`text-serif` to use serif text on the slide.

```rst
.. slide::
    :text-serif: True

    # Slide 2
```

### `no-header`

`no-header` allows the temporary removal of a default header
set by the `slide-config` directive.

### `header`

`header` allows the addition of simple text headers.

```rst
.. slide::
    :header: A simple header

    # Slide 2
```

### `header-alignment`

`header-alignment` is used with `header` to align the text used in
the `header` option.

Allowed alignment values:

- left (default)
- right

```rst
.. slide::
    :header: A simple header
    :header-alignment: left

    # Slide 2
```

```rst
.. slide::
    :header: A simple header
    :header-alignment: right

    # Slide 2
```

### `no-footer`

`no-footer` temporarily disables the slide footer when a default has
been set with `slide-config` directive.

### `footer`

`footer` same behavior as header, except footer.

```rst
.. slide::
    :footer: a simple footer

    # Slide 2
```

### `footer-alignment`

`footer-alignment` has the same functionalitiy as `header-alignment`
except for the footer.

