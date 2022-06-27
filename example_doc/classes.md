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