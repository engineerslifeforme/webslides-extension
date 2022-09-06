# Images

Both the `image` and `figure` directive can be used.  `figure`
is generally preferred.

WebSlides makes some recommendations on desirable resolutions for
images.

## Alignment

The `class` optional argument is available for horizontal alignment
of images.

- `alignleft`
- `aligncenter`
- `alignright`

Example:

```rst
.. image:: _static/images/dog.png
    :class: alignleft
```

## Size

`height` and `width` can be used to explicitly manage the size of the
image.  Pixels is the unit.

Example:

```rst
.. image:: _static/images/dog.png
    :height: 400
    :width: 400
```