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

{tsym}`a * * *`
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

{tsym}`a * * *`
````
`````
``````

``````{slide}
---
horizontal-alignment: center
wrap: True
---
`````{heading} h2
.grid.**vertical-align** + .column
`````
{ti}`Basic Grid (auto-fill and equal height).`
`````{grid}
---
alignment: vertical
---
````{column}
{ph6}`Why Webslides?`

There're excellent presentation tools out there. WebSlides is about good karma and sharing content. Hypertext, clean code, and beauty as narrative elements.

{tsym}`a* * *`
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

{tsym}`a* * *`
````
`````
``````

`````{slide}
---
wrap: True
---
````{heading} h2
.grid.**sm** (sidebar + main)
````
````hr
````
````{grid}
---
sidebar-config: sm
---
```{column}
{ph3}`.column 1`

Stendhal syndrome is a psychosomatic disorder that causes rapid heartbeat, dizziness, fainting, confusion and even hallucinations when an individual is exposed to an experience of great personal significance, particularly viewing art.

```
```{column}
{ph3}`.column 2`

The illness is named after the 19th-century French author Stendhal (pseudonym of Marie-Henri Beyle), who described his experience with the phenomenon during his 1817 visit to Florence in his book Naples and Florence: A Journey from Milan to Reggio.

When he visited the Basilica of Santa Croce, where Niccolò Machiavelli, Michelangelo and Galileo Galilei are buried, he saw Giotto's frescoes for the first time and was overcome with emotion.
```
````
`````

`````{slide}
---
wrap: True
---
````{heading} h2
.grid.**ms** (main +  sidebar)
````
````hr
````
````{grid}
---
sidebar-config: ms
---
```{column}
{ph3}`.column 1`

Beauty is a characteristic of an animal, idea, object, person or place that provides a perceptual experience of pleasure or satisfaction. Beauty is studied as part of aesthetics, culture, social psychology and sociology. 

An "ideal beauty" is an entity which is admired, or possesses features widely attributed to beauty in a particular culture, for perfection.
```
```{column}
{ph3}`.column 2`

The experience of "beauty" often involves an interpretation of some entity as being in balance and harmony with nature, which may lead to feelings of attraction and emotional well-being.
```
````
`````

`````{slide}
---
wrap: True
---
````{heading} h2
.grid.**sms** (sidebar + main + sidebar)
````
````{hr}
````
````{grid}
---
sidebar-config: sms
---
```{column}
{ph3}`.column 1`

Information architecture is considered to have been founded by Richard Saul Wurman.
```
```{column}
{ph3}`.column 2`

Information architecture (IA) is the structural design of shared information environments; the art and science of organizing and labelling websites, intranets, online communities and software to support usability and findability; and an emerging community of practice focused on bringing principles of design and architecture to the digital landscape.
```
```{column}
{ph3}`.column 3`

The difficulty in establishing a common definition for "information architecture" arises partly from the term's existence in multiple fields.
```
````
`````

`````{slide}
---
wrap: True
card-size: 50
card-background: bg-white
---
````{flex-content}
{ph2}`Unsplash`

.card-50.bg-white

```{ti}
[Unsplash](http://unsplash.com) is a really cool resource. It is a collection of Creative Commons Zero licensed photos that are really great.
```

```{description-list}
- **Role:** Fronted
- **Client:** Acme
- **Year:** 2018
```
````
````{figure} https://source.unsplash.com/rCOWMC8qf8A/
````
`````

`````{slide}
---
wrap: True
card-size: 50
card-background: bg-white
---
````{web} https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1241.8442158987712!2d-0.1268272!3d51.5005848!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487604c38c8cd1d9%3A0xb78f2474b9a45aa9!2sBig+Ben!5e0!3m2!1ses!2ses!4v1491497625579
```{link} https://maps.google.com
{fa}`fa-maps` Google Maps
```
````
````{flex-content}
{ph2}`Discover London`

.card-50.bg-white

```{description-list}
- **Density:** 5,518/km
- **Population:** 8,673,713
- **Website:** [visitlondon.com](http://www.visitlondon.com/)

There are many reasons to visit London. London has a diverse range of people and cultures, and more than 300 languages are spoken in the region.
```
````
`````

````{slide}
---
full-screen: True
card-size: 50
---
```{figure} https://source.unsplash.com/8lODM_TYmkI/800x600
Yosemite National Park
```
```{flex-content}
{ph2}`What is inspiration?`

In Greek thought, inspiration meant that the poet or artist would go into ecstasy or furor poeticus, the divine frenzy or poetic madness. The Muses are the inspirational goddesses of literature, science, and the arts in Greek mythology.
```
````

```{slide}
---
horizontal-alignment: center
background-color: bg-apple
---
{ph1}`Backgrounds` 

`<section class="bg-apple">`
```

```{slide}

I'm not sure how to handle the classes on list items in a not
painful way
```

````{slide}
---
background-color: bg-gradient-h
wrap: True
---
{ph1}`Gradients`
```{flexblock-border}
- Horizontal `.bg-gradient-h`
- Radial `.bg-gradient-r`
- Vertical `.bg-gradient-v`
```
````

```{slide}
---
background-color: bg-gradient-h
wrap: True
horizontal-alignment: center
---
{ph1}`Horizontal Gradient`

`section.bg-gradient-h`
```

```{slide}
---
background-color: bg-gradient-r
wrap: True
horizontal-alignment: center
---
{ph1}`Radial Gradient`

`section.bg-gradient-r`
```

```{slide}
---
background-color: bg-gradient-v
wrap: True
horizontal-alignment: center
---
{ph1}`Vertical Gradient`

`section.bg-gradient-v`
```

`````{slide}
---
wrap: True
wrap-size: 60
---
{ph3}`Background Videos`
````{pre}
```
<video class="background-video" autoplay muted loop poster="image.jpg">
  <source src="video.mp4" type="video/mp4">
</video>
```
````
`.background-video`
`````

````{slide}
---
background-color: bg-black
background-video: https://webslides.tv/static/videos/working.mp4
background-video-poster: https://webslides.tv/static/images/working.jpg
wrap: True
---
`.background-video`

```{heading} h2
**WebSlides is the easiest way to make HTML presentations. Inspire and engage.**
```
````

```{slide}
---
background-video-poster: https://webslides.tv/static/images/working.jpg 
background-video: https://webslides.tv/static/videos/working.mp4
horizontal-alignment: center
background-color: bg-blue
wrap: True
background-video-dark: True
---
{tlh2}`BG Video with Overlay`

`section.bg-blue > .background-video.dark` or .light
```

``````{slide}
---
wrap: True
---
`````{content-left}
{ph3}`Fullscreen Background Iamges`
````{pre}
```
<section>
  <span class="background" style="background-image:url('https://source.unsplash.com/UJbHNoVPZW0/')"></span>
  <div class="wrap">
    <h1>Slide</h1>
  </div>
</section>
```
````

How to [embed Unsplash photos](https://source.unsplash.com/)?
`````
`````{content-left}
{ph3}`16 Different Background`
````{text-cols}
- **.background** (cover)
- .background-top (cover)
- .background-bottom (cover)
- .background.light (opacity)
- .background.dark (opacity)
- .background-center
- .background-center-top
- .background-center-bottom
- .background-left
- .background-left-top
- .background-left-bottom
- .background-right
- .background-right-top
- .background-right-bottom
- .background-anim (animated)
- .**background-video** (fullscreen)
````
`````
``````

`````{slide}
---
background-image: _static/images/iphone-hand.png
background-image-location: right-bottom
wrap: True
---
````{content-left}
{ph3}`.background-(position)`

`.background-right-bottom`
```{flexblock-spec}
- {fa}`fa-wifi` {ph2}`Ultra-Fast Wifi` Simple and secure file sharing.
- {fa}`fa-battery-full` {ph2}`All day battery life` Your battery worries may be over.
- {fa}`fa-life-ring` {ph2}`Lifetime Warranty` We'll fix it for if we can't, we'll replace it.
````
`````

````{slide}
---
background-color: bg-black
horizontal-alignment: center
background-image: https://source.unsplash.com/UJbHNoVPZW0/
wrap: True
dark-background-image: True
---
```{text-landing} h1
---
shadow: True
---
Iceland
```
`section[class*="bg-"] > .background.dark`
````

````{slide}
---
background-color: bg-black
horizontal-alignment: center
background-image: https://source.unsplash.com/UJbHNoVPZW0/
wrap: True
light-background-image: True
---
```{text-landing} h1
---
shadow: True
---
Iceland
```
`section[class*="bg-"] > .background.light`
````

```{slide}
---
background-image-animation: True
horizontal-alignment: center
background-color: bg-black
background-image: https://source.unsplash.com/n9WPPWiPPJw/
wrap: True
---
{ph2}`.background.anim`
```