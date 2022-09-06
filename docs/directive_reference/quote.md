# Quotes

Two types of quotes are available: `block-quote` and `text-quote`.

Review the `reference.rst` deck to see different permutations.

## `text-quote`

The `text-quote` directive provides an optional `citiation`
argument.

```rst
.. slide::

    # Slide with Quote

    .. text-quote
        :citation: Famous Person

        Amazing, Life-Changing quote  with great meaning
```

`text-quote` can also be used as a role without a citation:

```rst

:text-quote:`Long label form`

:tq:`Short role label form`
```

`cite` can actually be used separately for more complex citation
than simply plain text that is available to the optional argument.

## `blockquote`

`blockquote` is almost exactly the same without the `citation`
optional arugment.  It is also not intended for use with `cite`.

`bq` available as a short label in role form.