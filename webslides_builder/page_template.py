def get_page(body='blank'):
    return f"""<!doctype html>
<html lang="en" prefix="og: http://ogp.me/ns#">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CLEAN MARKUP = GOOD KARMA.
      Hi source code lover,

      you're a curious person and a fast learner ;)
      Let's make something beautiful together. Contribute on Github:
      https://github.com/webslides/webslides

      Thanks!
    -->

    <!-- SEO -->
    <title>WebSlides Tutorial: Videos, Images, and Maps</title>
    <meta name="description" content="How to embed images, videos, and maps in your presentation.">

    <!-- URL CANONICAL -->
    <!-- <link rel="canonical" href="http://your-url.com/permalink"> -->

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,700,700i%7CMaitree:200,300,400,600,700&amp;subset=latin-ext" rel="stylesheet">

    <!-- CSS Base -->
    <link rel="stylesheet" type='text/css' media='all' href="_static/webslides.css">

    <!-- Optional - CSS SVG Icons (Font Awesome) -->
    <link rel="stylesheet" type='text/css' media='all' href="_static/svg-icons.css">

    <!-- SOCIAL CARDS (ADD YOUR INFO) -->

    <!-- FACEBOOK -->
    <meta property="og:url" content="/" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="WebSlides Tutorial: Media" />

    <!-- EDIT -->
    <meta property="og:description" content="How to embed images, videos, and maps in your presentation.">

    <!-- EDIT -->
    <meta property="og:updated_time" content="2017-01-04T17:25:31">

    <!-- EDIT -->
    <meta property="og:image" content="_static/images/share-webslides.jpg" >

    <!-- EDIT -->

    <!-- TWITTER -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@webslides">

    <!-- EDIT -->
    <meta name="twitter:creator" content="@jlantunez">

    <!-- EDIT -->
    <meta name="twitter:title" content="WebSlides Tutorial: Media">

    <!-- EDIT -->
    <meta name="twitter:description" content="How to embed images, videos, and maps in your presentation.">

    <!-- EDIT -->
    <meta name="twitter:image" content="_static/images/share-webslides.jpg">

    <!-- EDIT -->

    <!-- FAVICONS -->
    <link rel="shortcut icon" sizes="16x16" href="_static/images/favicons/favicon.png">
    <link rel="shortcut icon" sizes="32x32" href="_static/images/favicons/favicon-32.png">
    <link rel="apple-touch-icon icon" sizes="76x76" href="_static/images/favicons/favicon-76.png">
    <link rel="apple-touch-icon icon" sizes="120x120" href="_static/images/favicons/favicon-120.png">
    <link rel="apple-touch-icon icon" sizes="152x152" href="_static/images/favicons/favicon-152.png">
    <link rel="apple-touch-icon icon" sizes="180x180" href="_static/images/favicons/favicon-180.png">
    <link rel="apple-touch-icon icon" sizes="192x192" href="_static/images/favicons/favicon-192.png">

    <!-- Android -->
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#333333">

  </head>
  <body>
    <header role="banner">
      <nav role="navigation">
        <p class="logo"><a href="../index.html" title="WebSlides">WebSlides</a></p>
        <ul>
          <li class="github">
            <a rel="external" href="https://github.com/webslides/webslides" title="Github">
              <svg class="fa-github">
                <use xlink:href="#fa-github"></use>
              </svg>
              <em>WebSlides</em>
            </a>
          </li>
          <li class="twitter">
            <a rel="external" href="https://twitter.com/webslides" title="Twitter">
              <svg class="fa-twitter">
                <use xlink:href="#fa-twitter"></use>
              </svg>
              <em>@WebSlides</em>
            </a>
          </li>
          <!--  <li class="dribbble"><a rel="external" href="http://dribbble.com/webslides" title="Dribbble"><svg class="fa-dribbble"><use xlink:href="#fa-dribbble"></use></svg> <em>webslides</em></a></li> -->
        </ul>
      </nav>
    </header>

    <main role="main">
      <article id="webslides">
        {body}
      </article>
    </main>
    <!--main-->
    <!-- Required -->

    <script src="_static/js/webslides.js"></script>

    <script>
      window.ws = new WebSlides();
    </script>

    <!-- OPTIONAL - svg-icons.js (fontastic.me - Font Awesome as svg icons) -->
    <script defer src="_static/js/svg-icons.js"></script>

  </body>
</html>"""