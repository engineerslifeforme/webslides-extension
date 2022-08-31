(slide_styling)=

# Slide Styling

In order to produce content that is easy to read and easy to
manage, it is valuable to take a moment to think about the
styling for the entire presentation.  Fortunately, it is
relatively easy to start down the content generation path
and as reuse opportunities / redundancy becomes apparent,
content can be moved as needed.

The {ref}`content_organization` section provides good conventions
on how to organize common slide styling components.  The
following are valuable tools in the slide styling process:

1. {ref}`slide_config_directive`
2. {ref}`header_footer`
3. {ref}`content_templating`

These tools will allow presentation authors to avoid redundancy
and separate some complex styling instances from the content.

The example presentation decks within the `example_decks`
directory provide many examples of complex styling and the breadth
of options provided by WebSlides.

## Unique Slides

It is very common within a presentation that one or more slides
do not follow the theme of the majority of the other slides.
When utilizing `slide-config` these special slides can use
the `no-defaults` optional argument of the `slide` directive.

## classes and styles

Almost all WebSlides directives support the `classes` and `style`
optional arugments so that targetted styling can be applied to
individual elements.

```{note}
`image` directives use `class` instead of `classes`.
```