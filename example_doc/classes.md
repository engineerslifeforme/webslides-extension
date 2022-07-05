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