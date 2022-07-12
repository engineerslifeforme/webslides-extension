````{slide}
---
horizontal-alignment: center
background-color: bg-black-blue
dark-background-image: https://source.unsplash.com/6njoEbtarec/
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
---
{ph3}`1/9 left top`

Put content wherever you want. Have less. Do more. Create beautiful solutions.

`.slide-top and .content-left`
```

```{slide}
---
content-alignment: center
vertical-alignment: top
---
{ph3}`2/9 center top`

In a village of La Mancha, the name of which I have no desire to call to mind,

`.slide-top and .content-center`
```

```{slide}
---
content-alignment: right
vertical-alignment: top
---
{ph3}`3/9 right top`

there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.

`.slide-top and .content-right`
```

```{slide}
---
content-alignment: left
---
{ph3}`4/9 left center`

An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays,

`.content-left`
```

```{slide}
---
content-alignment: center
---
{ph3}`5/9 center`

lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.

`.content-center`
```

```{slide}
---
content-alignment: right
---
{ph3}`6/9 right center`

he rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays,

`.content-right`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: left
---
{ph3}`7/9 left bottom`

while on week-days he made a brave figure in his best homespun.

`.slide-bottom` and `.content-left`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: center
---
{ph3}`8/9 center bottom`

He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place,

`.slide-bottom` and `.content-center`
```

```{slide}
---
vertical-alignment: bottom
content-alignment: right
---
{ph3}`9/9 right bottom`

who used to saddle the hack as well as handle the bill-hook.

`.slide-bottom` and `.content-right`
```

``````{slide}
---
horizontal-alignment: center
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
horizontal-alignment: center
---
{ph1}`Horizontal Gradient`

`section.bg-gradient-h`
```

```{slide}
---
background-color: bg-gradient-r
horizontal-alignment: center
---
{ph1}`Radial Gradient`

`section.bg-gradient-r`
```

```{slide}
---
background-color: bg-gradient-v
horizontal-alignment: center
---
{ph1}`Vertical Gradient`

`section.bg-gradient-v`
```

`````{slide}
---
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
background-video-dark: True
---
{tlh2}`BG Video with Overlay`

`section.bg-blue > .background-video.dark` or .light
```

``````{slide}
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
---
{ph2}`.background.anim`
```

````{slide}
---
horizontal-alignment: center
---
```{heading} h2
**Flexible blocks**
```
`ul.flexblock` = Flexible blocks with auto-fill and equal height.
```{hr}
```
```{flexblock}
- **{fa}`fa-bar-chart` .flexblock li 1**
  
  Multipurpose: servies, features, specs...
- **{fa}`fa-balance-scale` .flexblock li 2**
  
  Multipurpose: benefits, clients, work...
- **{fa}`fa-cog` .flexblock li 3**
  
  Multipurpose: news, metrics, plans...
```
````

```{slide}
Skipped how to write in html slide
```

```{slide}
Skipped blink vs without, could not see a difference

Other than the bottom seems to a be link, maybe, cursor changes
```

````{slide}
{ph3}`ul.flexblock.blink.border`
```{flexblock-border}
- {ph3}`Google` 2016.- Google Drive
- **Facebook** 2016.- F8 Conference
- **Airbnb**2015.- Creative Direction
- **Microsoft** 2015.- Content Strategy
- **The New York Times**2015.- Recruitment
- **Netflix** 2014.- Mobile Apps
- **Instagram**2014.- Identity
- **Spotify** 2013.- TV Commercials
```
````

`````{slide}
{ph2}`Clients`

`ul.flexblock.clients`
````{flexblock-clients}
- ```{figure} _static/images/logos/google.svg
  ---
  class: blacklogo
  ---
  {ph3}`Interfaces`

  Collaboration with the Acme team to design their mobile apps. `img.blacklogo`
  ```
- ```{figure} _static/images/logos/microsoft.svg
  ---
  class: blacklogo
  ---
  {ph3}`Interfaces`

  Collaboration with the Acme team to design their mobile apps. `img.blacklogo`
  ```
- ```{figure} _static/images/logos/instagram.svg
  ---
  class: blacklogo
  ---
  {ph3}`Interfaces`

  Collaboration with the Acme team to design their mobile apps. `img.blacklogo`
  ```
- ```{figure} _static/images/logos/netflix.svg
  ---
  class: blacklogo
  ---
  {ph3}`Interfaces`

  Collaboration with the Acme team to design their mobile apps. `img.blacklogo`
  ```
````
`````

`````{slide}
{ph3}`ul.flexblock.features`
````{flexblock-features}
- ```{heading} h2
  {span}`100%` customizable` 
  ```
  Well documented.
- {span}`$48` {ph2}`Extra virgin olive oil` The Spanish caviar.
- ```{heading} h2
  {fa}`fa-wifi` Ultra-fast Wifi
  ```
  Simple file sharing.
````
````{hr}
````
{ph3}`ul.flexblock.features.blink`
````{flexblock-features}
- {span}`$48` {ph2}`Extra virgin olive oil` The Spanish caviar.
- ```{heading} h2
  {fa}`fa-wifi` Ultra-fast Wifi
  ```
  Simple file sharing.
````
`````

`````{slide}
---
background-color: bg-primary
---
{ph3}`ul.flexblock.gallery`
````{flexblock-gallery}
- ```{figure} https://source.unsplash.com/vCF5sB7QecM/800x600
  {ph2}`uWatch` By Jan Doe
  ```
- ```{figure} https://source.unsplash.com/yvx7LSZSzeo/800x600
  {ph2}`Ellen Daniels` CEO
  ```
- ```{figure} https://source.unsplash.com/-sQ4FsomXEs/800x600
  {ph2}`New York` 3.456 rooms
  ```
````
`````

`````{slide}
{ph3}`ul.flexblock.gallery + .overlay`
````{flexblock-gallery}
- ```{overlay}
  {ph2}`uWatch` By Jan Doe
  ```
  ![Thumbnail](https://source.unsplash.com/vCF5sB7QecM/800x600)
- ```{overlay} 
  {ph2}`Ellen Daniels` CEO
  ```
  ![Thumbnail](https://source.unsplash.com/yvx7LSZSzeo/800x600)
- ```{overlay} 
  {ph2}`New York` 3.456 rooms
  ```
  ![Thumbnail](https://source.unsplash.com/-sQ4FsomXEs/800x600)
````
`````

```{slide}
Already shown metrics
```

```{slide}
skipping the plans stuff for now
```

`````{slide}
---
card-size: 50
---
````{flex-content}
{ph3}`ul.flexblock.specs`
```{flexblock-spec}
- {fa}`fa-wifi` {ph2}`Ultra-Fast Wifi` Simple and secure file sharing.
- {fa}`fa-battery-full` {ph2}`All day battery life` Your battery worries may be over.
- {fa}`fa-life-ring` {ph2}`Lifetime Warranty` We'll fix it or if we can't, we'll replace it.
```
````
````{figure} _static/images/android.png
---
class: aligncenter
---
````
`````

````{slide}
---
background-color: bg-gradient-gray
wrap-size: 50
---
{ph3}`.flexblock.reasons`
```{hr}
```
```{flexblock-reasons}
- {ph2}`Why WebSlides? Work better, faster.` Designers and marketers can now focus on the content. Simply choose a demo and customize it in minutes. Be memorable!
- {ph2}`Good karma. Just the essentials and using lovely CSS.` WebSlides is about telling the story, and sharing it in a beautiful way. Hypertext and clean code as narrative elements.
```
````

`````{slide}
{ph3}`ul.flexblock.steps`
````{flexblock-steps}
- ```{span}
  {fa}`fa-heartbeat`
  ```
  {ph2}`01. Passion` When you're really passionate about your job, you can change the world.
- ```{process-step} 2
  ```
  ```{span}
  {fa}`fa-magic`
  ```
  {ph2}`02. Purpose` Why does this business exist? How are you different? Why matters?
- ```{process-step} 3
  ```
  ```{span}
  {fa}`fa-balance-scale`
  ```
  {ph2}`03. Principles` Leadership through usefulness, openness, empathy, and good taste.
- ```{process-step} 4
  ```
  ```{span}
  {fa}`fa-cog`
  ```
  {ph2}`04. Process`
  - Useful
  - Easy
  - Fast
  - Beautiful
````
`````

````{slide}
{ph3}`ul.flexblock.activity`
```{flexblock-activity}
- {year}`2016` {title}`UX Designer at ACME` {summary}`This is a job description for the UX Designer role at ACME. Be concise. Content like a tweet: 2-3 lines recommended.`
- {year}`2 mins ago` {title}`14 world famous buildings to inspire you` {summary}`From the Colosseum to the Chrysler building, get a dose of inspiration from 14 of the world's most famous buildings.`
- {year}`2013` {title}`Co-Founder of GAMMA` {summary}`The culture within an organization is an essential part for success. This is a job description. Be concise. 2-3 lines recommended.`
```
````

``````{slide}
`````{cta}
````{number}
{span}`Ag`
````
````{benefit}
```{tsub}
Roboto in [Google Fonts](https://www.google.com/fonts#QuickUsePlace:quickUse/Family:Roboto:400,700,700italic,400italic,300,300italic)
```
```{heading} h3
**The quick brown fox jumps over the lazy dog**
```

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

1234567890(,.;:?!$&*)
````
`````
``````

```{slide}
---
horizontal-alignment: center
---
{tlh1}`Landings` `.text-landing`
```

```{slide}
---
horizontal-alignment: center
---
{tlh1}`Landings` {ti}`Create a simple web presence.` `.text-intro`
```

````{slide}
---
horizontal-alignment: center
---
```{tsub}
Powered by [#WebSlides](https://twitter.com/search?f=tweets&vertical=default&q=%23WebSlides&src=typd)
```
`.text-subtitle`
{tlh1}`Landings` {ti}`Create a simple web presence.`
````

````{slide}
---
horizontal-alignment: center
background-color: bg-black
background-image: https://source.unsplash.com/C1HhAQrbykQ/
---
```{text-landing} h1
---
classes: text-shadow
---
**Landings**
```
```{text-intro}
`.text-shadow`
```
````

````{slide}
---
background-color: bg-apple
horizontal-alignment: center
---
```{heading} h2
---
classes: text-data
---
4,235,678
```
`.text-data`
````

```{slide}
{tc}`Why WebSlides? .text-context` {ph2}`WebSlides is incredibly easy and versatile. The easiest way to make HTML presentations.`
```

````{slide}
`.text-cols (2 columns)`
```{text-cols-div}
**Why WebSlides?** There are excellent presentation tools out there. WebSlides is about sharing content, essential features, and clean markup. **Each parent `<section>`** in the #webslides element is an individual slide.

**WebSlides help you build a culture of innovation and excellence.** When you're really passionate about your job, you can change the world. How to manage a design-driven organization? Leadership through usefulness, openness, empathy, and good taste.
```
```{flexblock-metrics}
- {fa}`fa-phone` Call us at 555.345.6789
- {fa}`fa-twitter` @username
- {fa}`fa-envelope` Send us an email
```
````

``````{slide}
`````{grid}
---
alignment: vertical
---
````{column}
{ph2}`A Phone by Google` {ti}`Pixel's camera lets you take brilliant photos in low light, bright light or any light.`
```{description-list}
- {tl}`.text-label:` Google (2016).
- {tl}`Services:` Industrial Design.
- {tl}`Website:` [madeby.google.com/phone/](https://madeby.google.com/phone/)
````
````{column}
```{figure} _static/images/android.png
```
````
`````
``````

```{slide}
Skipping `text-serif` slide
```

````{slide}
---
text-serif: True
horizontal-alignment: center
---
```{content-left}
{ph2}`WebSlides is incredibly easy and versatile.` `.text-serif` (Maitree)
```
```{content-left}
Each parent `<section>` in the #webslides element is an individual slide.

Clean markup with popular naming conventions. Minimum effort. Just focus on your content.
```
````

````{slide}
---
wrap-size: 50
---
```{heading} h3
**What is Stendhal Syndrome?**
```
```{text-intro}
Beauty overdose. `.text-pull-right`
```
Imagine that you are in Florence. If you suddenly start to feel that you literally cannot breathe, you may be experiencing Stendhal Syndrome.
{tpr}`Psychiatrists have long debated whether it really exists.`

The syndrome is not only associated with viewing a beautiful place, but also good art. 

The beauty of Italian art has a concentrated perfection and transcendent sensuality that is incredibly addictive.

{tsym}`a* * *`
````

```{slide}
---
background-color: bg-apple
horizontal-alignment: center
---
{ph2}`One more thing...` 

`.text-apple / .bg-apple`
```

`````{slide}
---
horizontal-alignment: center
---
````{flexblock-gallery}
- ```{figure} https://webslides.tv/static/images/demos-why.png  
  ```
  {ph2}`Why WebSlides?`
- ```{figure} https://webslides.tv/static/images/demos-landings.png
  ```
  {ph2}`Landings`
- ```{figure} https://webslides.tv/static/images/demos-portfolios.png
  ```
  {ph2}`Portfolios`
- ```{figure} https://webslides.tv/static/images/demos-apple.png
  ```
  {ph2}`Appple Keynote`
````
`````
  


