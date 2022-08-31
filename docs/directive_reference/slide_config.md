(slide_config_directive)=

# `slide-config` Directive

The `slide-config` directive shares all the same optional arguments
as the {ref}`slide_directive`, but it sets the configuration details
for all following slides.  So if a footer is desired on ALL slides
within the presentation, the `slide-config` directive can be used
a single time at the begining of the file as opposed to on every
single slide.

```rst
.. slide-config::
    :footer: a simple footer

.. slide::

    This slide will contain the footer

.. slide::

    And so will this one.
```

