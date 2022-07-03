`````{slide}
---
classes: bg-black-blue aligncenter
---

```{span}
---
classes: background dark
style: background-image:url('https://source.unsplash.com/6njoEbtarec/')
---
```

````{div}
---
classes: wrap
---

```{paragraph}
---
classes: text-subtitle
---
WebSlides Tutorial
```
```{heading} h1
---
classes: text-landing
---
Classes
```
```{paragraph}
---
classes: text-symbols
---
a * * *
```
```{link}
---
classes: button ghost
---
{fa}`fa-github` Free Download
```
````
`````

`````{slide}
---
classes: aligncenter
---
````{div}
---
classes: wrap
---

**{ph2}`Webslides Classes`**
```{paragraph}
---
classes: text-intro
---
Friendly naming conventions.
```
```{flexblock}
---
classes: border
---
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
`````

`````{slide}
````{div}
---
classes: wrap size-50
---
```{heading} h2
{fa}`fa-heart-o` CSS Syntax
```
```{paragraph}
---
classes: text-intro
---
WebSlides is so easy to understand and love. Baseline: 8.
```
{hr}`a`
```{description-list}
- {text-label}`Typography:` .text-landing, .text-subtitle, .text-data, .text-intro...
- {text-label}`BG Colors:` .bg-primary, .bg-blue,.bg-apple...
- {text-label}`BG Images:` .background, .background-center-bottom...
- {text-label}`Cards:` .card-60, .card-50, .card-40...
- {text-label}`Sizes:` .size-50, .size-40...
- {text-label}`Flex Blocks:` .flexblock.clients, .flexblock.gallery, .flexblock.metrics...`
```
````
`````

````````{slide}
```````{div}
---
classes: wrap
---
``````{div}
---
classes: grid vertical-align
---
`````{div}
---
classes: column
---
**{ph3}`WebSlides is really easy`**
````{paragraph}
---
classes: text-intro
---
Each parent `<section>` in the #webslides element is an individual slide.
````
Code is neat, scalable, and well documented. It uses **intuitive markup with popular naming conventions**. There's no need to overuse classes or nesting. **Based on [SimpleSlides](https://github.com/jennschiffer/SimpleSlides), by [Jenn Schiffer](http://jennmoney.biz)** :)
`````
`````{div}
---
classes: column
---
````{preformatted}
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
{hr}`a`
``````{paragraph}
---
classes: aligncenter
---
Vertical sliding? `<article id="webslides" class="vertical">`
``````
```````
````````

``````{slide}
`````{header}
````{div}
---
classes: wrap
---
Header (logo)
```{span-content}
---
classes: alignright
---
.alignright
```
````
`````
`````{div}
---
classes: aligncenter
---
{ph2}`Simple CSS Alignments`
Put content wherever you want.
`````
`````{footer}
````{div}
---
classes: wrap
---
```{span-content}
---
classes: alignleft
---
Footer: logo, credits... (.alignleft)
```
```{span-content}
---
classes: alignright
---
{fa}`fa-twitter` @username .alignright
```
````
`````
``````

``````{slide}
`````{div}
---
classes: wrap
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
`````
``````

``````{slide}
`````{div}
---
classes: wrap
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
````
`````
``````

`````{slide}
````{div}
---
classes: wrap
---
```{image} _static/images/iphone.png
---
class: aligncenter size-40
---
```
```{paragraph}
---
classes: aligncenter
---
`img.aligncenter.size-40`
```
````
`````

`````{slide}
---
classes: slide-top
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-left
---
{ph3}`1/9 left top`

Put content wherever you want. Have less. Do more. Create beautiful solutions.

`.slide-top and .content-left`
```
````
`````

`````{slide}
---
classes: slide-top
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-center
---
{ph3}`2/9 center top`

In a village of La Mancha, the name of which I have no desire to call to mind,

`.slide-top and .content-center`
```
````
`````

`````{slide}
---
classes: slide-top
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-right
---
{ph3}`3/9 right top`

there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.

`.slide-top and .content-right`
```
````
`````

`````{slide}
````{div}
---
classes: wrap
---
```{div}
---
classes: content-left
---
{ph3}`4/9 left center`

An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays,

`.content-left`
```
````
`````

`````{slide}
````{div}
---
classes: wrap
---
```{div}
---
classes: content-center
---
{ph3}`5/9 center`

lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.

`.content-center`
```
````
`````

`````{slide}
````{div}
---
classes: wrap
---
```{div}
---
classes: content-right
---
{ph3}`6/9 right center`

he rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays,

`.content-right`
```
````
`````

`````{slide}
---
classes: slide-bottom
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-left
---
{ph3}`7/9 left bottom`

while on week-days he made a brave figure in his best homespun.

`.slide-bottom` and `.content-left`
```
````
`````

`````{slide}
---
classes: slide-bottom
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-center
---
{ph3}`8/9 center bottom`

He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place,

`.slide-bottom` and `.content-center`
```
````
`````

`````{slide}
---
classes: slide-bottom
---
````{div}
---
classes: wrap
---
```{div}
---
classes: content-right
---
{ph3}`9/9 right bottom`

who used to saddle the hack as well as handle the bill-hook.

`.slide-bottom` and `.content-right`
```
````
`````

```````{slide}
---
classes: aligncenter
---
``````{div}
---
classes: wrap
---
{ph2}`.grid + .column`
`````{paragraph}
---
classes: text-intro
---
Basic Grid (auto-fill and equal height).
`````
`````{div}
---
classes: grid
---
````{div}
---
classes: column
---
{ph6}`Why Webslides?`

There're excellent presentation tools out there. WebSlides is about good karma and sharing content. Hypertext, clean code, and beauty as narrative elements.

```{paragraph}
---
classes: text-symbols
---
a* * *
```
````
````{div}
---
classes: column
---
```{figure} _static/images/setup.png
---
class: aligncenter
---
```
````
````{div}
---
classes: column
---
{ph6}`How easy is WebSlides?`

You can create your own presentation instantly. Just a basic knowledge of HTML and CSS is required. Simply choose a demo and customize it.

```{paragraph}
---
classes: text-symbols
---
a* * *
```
`````
``````
```````

```````{slide}
---
classes: aligncenter
---
``````{div}
---
classes: wrap
---
{ph2}`.grid.**vertical-align** + .column`
`````{paragraph}
---
classes: text-intro
---
Basic Grid (auto-fill and equal height).
`````
`````{div}
---
classes: grid vertical-align
---
````{div}
---
classes: column
---
{ph6}`Why Webslides?`

There're excellent presentation tools out there. WebSlides is about good karma and sharing content. Hypertext, clean code, and beauty as narrative elements.

```{paragraph}
---
classes: text-symbols
---
a* * *
```
````
````{div}
---
classes: column
---
```{figure} _static/images/setup.png
---
class: aligncenter
---
```
````
````{div}
---
classes: column
---
{ph6}`How easy is WebSlides?`

You can create your own presentation instantly. Just a basic knowledge of HTML and CSS is required. Simply choose a demo and customize it.

```{paragraph}
---
classes: text-symbols
---
a* * *
```
`````
``````
```````

``````{slide}
`````{div}
---
classes: wrap
---
{ph2}`.grid.ms (main +  sidebar)`

{hr}`a`

````{div}
---
classes: grid sm
---
```{div}
---
classes: column
---
{ph3}`.column 1`

Stendhal syndrome is a psychosomatic disorder that causes rapid heartbeat, dizziness, fainting, confusion and even hallucinations when an individual is exposed to an experience of great personal significance, particularly viewing art.

```
```{div}
---
classes: column
---
{ph3}`.column 2`

The illness is named after the 19th-century French author Stendhal (pseudonym of Marie-Henri Beyle), who described his experience with the phenomenon during his 1817 visit to Florence in his book Naples and Florence: A Journey from Milan to Reggio.

When he visited the Basilica of Santa Croce, where Niccolò Machiavelli, Michelangelo and Galileo Galilei are buried, he saw Giotto's frescoes for the first time and was overcome with emotion.
```
````
`````
``````

``````{slide}
`````{div}
---
classes: wrap
---
{ph2}`.grid.ms (main +  sidebar)`

{hr}`a`

````{div}
---
classes: grid ms
---
```{div}
---
classes: column
---
{ph3}`.column 1`

Beauty is a characteristic of an animal, idea, object, person or place that provides a perceptual experience of pleasure or satisfaction. Beauty is studied as part of aesthetics, culture, social psychology and sociology. 

An "ideal beauty" is an entity which is admired, or possesses features widely attributed to beauty in a particular culture, for perfection.
```
```{div}
---
classes: column
---
{ph3}`.column 2`

The experience of "beauty" often involves an interpretation of some entity as being in balance and harmony with nature, which may lead to feelings of attraction and emotional well-being.
```
````
`````
``````