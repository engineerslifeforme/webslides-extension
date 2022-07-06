````{slide}
---
horizontal-alignment: center
background-color: bg-black-blue
dark-background-image: https://source.unsplash.com/6njoEbtarec/
wrap: True
---

{text-subtitle}`Webslides Tutorial`
{tlh1}`Classes`
{text-symbols}`a * * *`

```{ghost-button-link} https://github.com/webslides/webslides
{fa}`fa-github` Free Download
```
````

````{slide}
---
horizontal-alignment: center
wrap: True
---
**{ph2}`Webslides Classes`**
{ti}`Friendly naming conventions.`
```{flexblock-border}
- {ph3}`Layout`
    1. CSS Syntax
    2. .alignleft
    3. .alignright
    4. .aligncenter
    5. .slide-top
    6. .content- (left, center, right)
    7. .slide-bottom
    8. .grid > .column
    9. .grid.vertical-align
    10. .card- (50,60,70...)
- {ph3}`Backgrounds`
    1. .bg-primary...(Corp Colors)
    2. .bg-black...(General Colors)
    3. .bg-gradient-(position)
    4. .background-video
    5. Background Images:
        1. .background (fullscreen)
        2. .background-(position)
        3. .background.dark
        4. .background.light
        5. .background.anim
- {ph3}`Flexible Blocks`
    1. .flexblock
    2. .flexblock.clients
    3. .flexblock.features
    4. .flexblock.gallery
    5. .flexblock.metrics
    6. .flexblock.plans
    7. .flexblock.specs
    8. .flexblock.reasons
    9. .flexblock.steps
    10. .flexblock.activity
- {ph3}`Typography (Roboto)`
    1. .text-landing
    2. .text-intro
    3. .text-subtitle
    4. .text-shadow
    5. .text-date
    6. .text-context
    7. .text-cols
    8. .text-label
    9. .text-serif (Maitree)
    10. .text-pull (-right/-left)
```
````

````{slide}
---
wrap: True
wrap-size: 50
---
```{heading} h2
{fa}`fa-heart-o` CSS Syntax
```
{ti}`WebSlides is so easy to understand and love. Baseline: 8.`
```{hr}
```
```{description-list}
- {tl}`Typography:` .text-landing, .text-subtitle, .text-data, .text-intro...
- {tl}`BG Colors:` .bg-primary, .bg-blue,.bg-apple...
- {tl}`BG Images:` .background, .background-center-bottom...
- {tl}`Cards:` .card-60, .card-50, .card-40...
- {tl}`Sizes:` .size-50, .size-40...
- {tl}`Flex Blocks:` .flexblock.clients, .flexblock.gallery, .flexblock.metrics...`
```
````

```````{slide}
---
wrap: True
---
``````{grid}

`````{column}
**{ph3}`WebSlides is really easy`**
```{ti}
Each parent `<section>` in the #webslides element is an individual slide.
```
Code is neat, scalable, and well documented. It uses **intuitive markup with popular naming conventions**. There's no need to overuse classes or nesting. **Based on [SimpleSlides](https://github.com/jennschiffer/SimpleSlides), by [Jenn Schiffer](http://jennmoney.biz)** :)
`````
`````{column}
````{pre}
```
<article id="webslides">
  <!-- Slide 1 -->
  <section>
    <h1>Design for trust</h1>
  </section>
  <!-- Slide 2 -->
  <section class="bg-primary">
    <div class="wrap">
      <h2>.wrap = container (width: 90%) with fadein</h2>
    </div>
  </section>
</article>
```
````
`````
``````
``````{hr}
``````
``````{text-center}
Vertical sliding? `<article id="webslides" class="vertical">`
``````
```````

````{slide}
```{header}
Header (logo)
```
```{center}
{ph2}`Simple CSS Alignments`
Put content wherever you want.
```
```{footer}
---
horizontal-alignment: right
---
{fa}`fa-twitter` @username .alignright
````

````{slide}
---
wrap: True
---
```{image} _static/images/iphone.png
---
class: alignleft size-50
---
```
{ph2}`img.alignleft`
```
img.alignleft.size-50
```
Jobs unveiled the iPhone to the public on January 9, 2007, at Macworld 2007 convention at the Moscone Center in San Francisco.  Apple sold 6.1 million first generation iPhone units over five quarters.

**Image size recommended**:

800x600px / 600x450px.
````

````{slide}
---
wrap: True
---
```{image} _static/images/iphone.png
---
class: alignright size-50
---
```
{ph2}`img.alignright`
```
img.alignright.size-50
```
Jobs unveiled the iPhone to the public on January 9, 2007, at Macworld 2007 convention at the Moscone Center in San Francisco.  Apple sold 6.1 million first generation iPhone units over five quarters.

**Image size recommended**:

800x600px / 600x450px.
```
````

````{slide}
---
classes: wrap
---
```{image} _static/images/iphone.png
---
class: aligncenter size-40
---
```
```{c}
`img.aligncenter.size-40`
```
````

```{slide}
---
content-alignment: left
vertical-alignment: top
wrap: True
---
{ph3}`1/9 left top`

Put content wherever you want. Have less. Do more. Create beautiful solutions.

`.slide-top and .content-left`
```

```{slide}
---
content-alignment: center
vertical-alignment: top
wrap: True
---
{ph3}`2/9 center top`

In a village of La Mancha, the name of which I have no desire to call to mind,

`.slide-top and .content-center`
```

```{slide}
---
content-alignment: right
vertical-alignment: top
wrap: True
---
{ph3}`3/9 right top`

there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.

`.slide-top and .content-right`
```

```{slide}
---
content-alignment: left
wrap: True
---
{ph3}`4/9 left center`

An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays,

`.content-left`
```

```{slide}
---
content-alignment: center
wrap: True
---
{ph3}`5/9 center`

lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.

`.content-center`
```

```{slide}
---
content-alignment: right
wrap: True
---
{ph3}`6/9 right center`

he rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays,

`.content-right`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: left
wrap: True
---
{ph3}`7/9 left bottom`

while on week-days he made a brave figure in his best homespun.

`.slide-bottom` and `.content-left`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: center
wrap: True
---
{ph3}`8/9 center bottom`

He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place,

`.slide-bottom` and `.content-center`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: right
wrap: True
---
{ph3}`9/9 right bottom`

who used to saddle the hack as well as handle the bill-hook.

`.slide-bottom` and `.content-right`
```

``````{slide}
---
horizontal-alignment: center
wrap: True
---
{ph2}`.grid + .column`
{ti}`Basic Grid (auto-fill and equal height).`
`````{grid}
````{column}
{ph6}`Why Webslides?`

There're excellent presentation tools out there. WebSlides is about good karma and sharing content. Hypertext, clean code, and beauty as narrative elements.

{ts}`a * * *`
````
````{column}
```{figure} _static/images/setup.png
---
class: aligncenter
---
```
````
````{column}
{ph6}`How easy is WebSlides?`

You can create your own presentation instantly. Just a basic knowledge of HTML and CSS is required. Simply choose a demo and customize it.

{ts}`a * * *`
````
`````
``````