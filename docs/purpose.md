# Purpose

The [WebSlides](https://github.com/webslides/WebSlides) HTML
presentation framework is capable of producing rich web based
presentations.  The sphinx webslides builder extension attempts
to provide the full set of features of the framework as an
output type from the [Sphinx Python Documentation Generator](https://www.sphinx-doc.org/en/master/).
This allows the building of WebSlides presentations via
reStructuredText or markdown and the utilization of the ecosystem
of Sphinx plugins.

## Motivation

Microsoft Powerpoint has a firm grip as the utility of choice
for business presentation creation.  Powerpoint and other WYSIWYG
presentation utilities provide a very capable and effective tool
in many scenarios.  Powerpoint in particular struggles in the
following scenarios:

1. Configuration Management (i.e. not git friendly)
2. Video content can be challenging
3. Web content can be challenging (e.g. Interactive Plots)
4. Reuse is all manual
5. Not condusive to auto generation
6. Content is not easily transferrable to other mediums

A text based, web output presentation framework can solve these
issues.

The WebSlides framework itself solves all of these issues, but
it requires users to create presentations directly in HTML.
The verbose tag structure of HTML is arguably difficult to read
and write.  HTML itself also does not provide great mechanisms
for extension or organization/complexity management.  On the other
hand, the HTML centered implementation (as opposed to javascript) 
makes the WebSlides framework an excellent target for Sphinx (and
underlying [docutils](https://docutils.sourceforge.io/)).

### Strengths of Powerpoint

To be fair and emphasize that Powerpoint still has utility, it
is worth explicitly noting its strengths which WebSlides and
this extension do not improve upon.

1. WYSIWYG Editing
2. Complex image manipulation within the editor
3. Slide builds and basic animations
4. Built in WSIWYG diagraming capabilities
5. Integration with other Microsoft business applications
6. Presenter mode/console
