.. slide-config::
    :vertical-alignment: top
    
.. header-config::
    
    .. content-center::
        
        IMPORTANT

.. footer-config::
    
    .. content-center::

        IMPORTANT

.. slide::
    :background-image: _static/images/image1.png
    :no-defaults: True

    .. content-right::

        .. heading:: h1
            
            **Title Slide**

        Some content

.. footer-config::
    :no-wrap: True
    :style: padding:0rem;

    .. content-center::

        IMPORTANT
        
    .. image:: _static/images/image3.png
        :class: alignright

.. slide::
    :card-size: 50

    .. content-left::
        
        :ph1:`Header`

        - Some Bullets
            - more
            - more
        - other

    .. figure:: _static/images/iphone.png
        :class: alignright

.. slide::
    :card-size: 50

    .. figure:: _static/images/iphone.png
        :class: alignleft
        
    .. content-right::
        
        :ph1:`Header`

        2 Some content

.. template-define:: test_content

    .. slide::
        :background-color: bg-apple

        {{ content }}

.. template:: test_content
    :content_mode:

    # Using a content template

    - with
    - some
    - bullets

.. slide::

    .. content-left::

        # A slide

        content

    .. content-left::

        .. web:: https://badge.fury.io/py/sphinx-webslides-builder.svg
            :height: 200
            :width: 200