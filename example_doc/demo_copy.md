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

```{flexblock}
---
classes: features
---

- {span-raw}`&rarr;` {ph2}`Simple Navigation` with arrow keys and swipe.
- {{fa_link}} {ph2}`Permalinks` Go to a specific slide.
- {fa}`fa-clock-o` {ph2}`Slide Counter` Current/Total number
- {ph2}`40+ Beautiful Components` Covers, cards, quotes...
- {fa}`fa-text-height` {ph2}`Vertical Rhythm` Use multiple of 8.
- {ph2}`500+ SVG Icons` Font Awesome Kit.
```

`````{slide}
---
classes: bg-apple
---

````{div}
---
classes: wrap
---

```{div}
---
classes: content-left
---

{ph2}`Webslides was made to inspire people.`
```

```{div}
---
classes: content-left
---

{p}`WebSlides is a wonderful way to showcase your company. All content is for demo purposes only. Images are property of their respective owners.`
```

```{flexblock}
- {{white_google}}
- {{white_netflix}}
- {{white_microsoft}}
```
````
`````

`````{slide}
---
classes: bg-apple
---

````{div}
---
classes: wrap
---

```{div}
---
classes: content-left
---

{ph2}`WebSlides help you build a culture of excellence.`
```

```{div}
---
classes: content-left
---

{p}`The art of storytelling. Hypertext, clean code, and beauty as narrative elements. Just essential features and lovely CSS. All content is for demo purposes only.`
```

```{flexblock}
---
classes: metrics
---

- Founded {span}`1976`
- {fa}`fa-users` 524M Subscribers
- {fa}`fa-line-chart` Revenue: $16M
- Montly Growth {span}`64%`
````
`````

`````{slide}
---
classes: bg-apple
---


````{div}
---
classes: wrap
---

```{flexblock}
---
classes: metrics border
---

- Founded {span}`1976`
- {fa_span}`fa-users` 542M Subscribers
- {fa_span}`fa-line-chart` Revenue: $16M
- Monthly Growth {span}`64%`
- {fa_span}`fa-building-o` 6 Offices
- {fa_span}`fa-smile-o` 14K Employees
- {span}`$4M` EBITDA
- {fa_span}`fa-university` Bank $76B
```
````
`````

`````{slide}
---
classes: bg-apple aligncenter
---

```{span}
---
classes: background dark
style: background-image:url('https://source.unsplash.com/pb_lF8VWaPU/')
---
```

````{div}
---
classes: wrap
---

```{heading} h2
---
classes: text-data
---
3,456,789
```
{ph3}`iPhone 7 in first 24 hours`
````
`````

`````{slide}
---
classes: bg-apple aligncenter
---

````{div}
---
classes: wrap
---

```{heading} h2
---
classes: text-data
---
$48 Billion
```
{ph3}`Revenue in Q4 2024`

````
`````

`````{slide}
---
classes: bg-apple slide-bottom
---

```{span}
---
classes: background
style: background-image:url('https://source.unsplash.com/Y5Tjb62cxl8/')
---
```

````{div}
---
classes: wrap
---

```{div}
---
classes: content-left
---

{fa}`fa-tree`
{ph2}`1,000,000`
{ph3}`We're working to protect up to a million acres of sustainable forest.`
```
````
`````

```````{slide}
---
classes: bg-apple
---

``````{div}
---
classes: wrap
---

`````{div}
---
classes: card-50
---

```{figure} _static/images/iphone.png
---
class: aligncenter
name: iPhone
---
```

````{div}
---
classes: flex-content
---

{ph2}`iPhone 7`

```{paragraph}
---
classes: text-intro
---
3D Touch, 12MP photos, and 4K video.
```

Every iPhone they have made was built on the same belief. That a phone should be more than a collection of features. That, above all, a phone should be absolutely simple, beautiful, and magical to use.
```
````
`````
``````
```````