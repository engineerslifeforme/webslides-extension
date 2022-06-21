---
myst:
    substitutions:
        white_google: |
            ````{div}
            ```{image} _static/images/logos/google.svg
            :class: whitelogo
            ```
            ````
        white_netflix: |
            ````{div}
            ```{image} _static/images/logos/netflix.svg
            :class: whitelogo
            ```
            ````
        white_microsoft: |
            ````{div}
            ```{image} _static/images/logos/microsoft.svg
            :class: whitelogo
            ```
            ````
        white_apple: |
            ```{image} _static/images/logos/apple.svg
            :class: whitelogo
            ```
        fa_link: |
            ````{generic} svg
            :attribute_names: class
            :attribute_values: fa-link
            ```{generic} use
            :attribute_names: xlink:href
            :attribute_values: "#fa-link"
            ```
            ````
---
# {{white_apple}}

<!-- I can't class a header image, should be whitelogo -->

```{slide-config} 
---
classes: bg-apple aligncenter
---
```

# Make a Keynote presentation using HTML

```{slide-config} 
---
classes: bg-apple
size: 50
---
```

WebSlides is an open source framework for building HTML presentations, landings, and portfolios.

````
.bg-apple
````

## HTML presentations can be easy

```{slide-config}
---
classes: bg-apple aligncenter
---
```

## Features

```{slide-config}
---
classes: bg-apple
---
```

```{flexblock-feature}
- {span-raw}`&rarr;` {ph2}`Simple Navigation` with arrow keys and swipe.
- {{fa_link}} {ph2}`Permalinks` Go to a specific slide.
- Slide Counter Current/Total number
- 40+ Beautiful Components Covers, cards, quotes...
- Vertical Rhythm Use multiple of 8.
- 500+ SVG Icons Font Awesome Kit.
```

## content-left div test

```{slide-config}
---
classes: bg-apple
---
```
````{div}
classes: wrap
```{div}
---
classes: content-left
---

Webslides was made to inspire people.
```

```{div}
---
classes: content-left
---

WebSlides is a wonderful way to showcase your company. All content is for demo purposes only. Images are property of their respective owners.
```

```{flexblock}
- {{white_google}}
- {{white_netflix}}
- {{white_microsoft}}
```
````

# Testing psuedo heading

{ph1}`some test ext`