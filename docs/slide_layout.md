# Slide Layout

This section provides basic guidance on creating common slide layouts.

Each of the slides is shown in the example decks, `slide_layout.rst`.

## Text Bullet Slide

The most common and basic slide format

```rst

.. slide::

    # Meeting Agenda

    - Coffee
    - Introductions
    - Requirements
    - Design
    - Testing
```

Also sub-bullets:

```rst
.. slide::

    # Meeting Agenda

    - Coffee
    - Introductions
    - Requirements

        - Software
        - System
```

## Image Only Slide

```rst
.. slide::

    # The Great Sphinx
    
    .. image:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
        :class: aligncenter
        :height: 500
```

No Heading

```rst
.. slide::

    .. image:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
        :class: aligncenter
```

Full slide

```rst
.. slide::
    :background-image: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg

    # The Great Sphinx
```

## Text and Image

```rst
.. slide::

    .. content-left::

        # The Great Sphinx

        - Is in Egypt
        - Is X years old
        - Is Y meters tall

    .. content-left::

        .. image:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg
```

Image left, text right

```rst
.. slide::

    .. content-left::

        .. image:: https://cdn.britannica.com/06/9306-050-1816909E/Great-Sphinx-dynasty-Giza.jpg

    .. content-left::

        # The Great Sphinx

        - Is in Egypt
        - Is X years old
        - Is Y meters tall
```