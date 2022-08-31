(header_footer)=

# Headers and Footers

Headers and footers exist as a banner across the top (header)
and or bottom (footer) of the slides.  Headers and footers
can be added via the directives below but also through
options in both `slide` and `slide-config` directives.
The slide options should be used for simple text headers
and footers while the directives can be used for complex
headers and footers.

## Header Directives

### `header-config` - Entire Slide Deck Configuration

`header-config` allows configuring the header for the current
file.  This will typically be performed at the beginning of
the file to produce a consistent header on each slide.  The
directive can be used multiple times to update the header
midway through the slide deck.

``` rst

    .. header-config::
    
        .. content-center::
            
            IMPORTANT
```

The example above will produce an `IMPORTANT` label centered
at the top of each slide.

The assigned header can be temporarily removed from a slide using
the `no-header` option on the `slide` directive, e.g.:

``` rst

    .. slide::
        :no-header: True
```

`header-config` settings will only persist within the content
of the file in which they are defined.

### `header` - Singe Slide Header

Use of the `header` directive is discouraged, but it is maintained
for advanced flexibility.  Using the `header` directive requires
using the `no-wrap` option on a slide and subsequent manually
wrapping within the slide as needed.

## Footer Directives

The `footer-config` and `footer` match their respective Header
directives in functionality.  `no-footer` option on the `slide`
directive will temporarily display `footer-config` settings.

Example of a footer with image:

``` rst
    .. footer-config::
        :no-wrap: True
        :style: padding:0rem;

        .. content-center::

            IMPORTANT
            
        .. image:: _static/images/image3.png
            :class: alignright
```