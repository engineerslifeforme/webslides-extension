===================
Change Log
===================

0.0.13
=======

Added ``content-mode`` to the ``template`` directive allowing normal
RST content instead of yaml content.

0.0.12
=======

``google_font.css`` paths to fonts did not match filenames retrieved
via curl in the github build.  Fixed.

``pyyaml`` was not in the dependencies.

0.0.11
=======

Removed hover header on slides.

Made offline compatible.

0.0.10
======

The sphinx directive arugment implementation in the previous
version was not robust enough to real data.  Changed to
inputing arguments as YAML in the body of the directive.

0.0.9
======

Add ``template`` and ``template-define`` directives to allow creating
reusable slide templates.

0.0.8
======

Added ``paragraph-style`` directive to allow temporary
paragraph styling for things like reduced vertical separatation
or fontsize changes.

0.0.7
=====

Bug in how the markdown style headings were implemented.
Changes made to address issues, but solution limits any formating
for now.

0.0.6
=====

Added ability to use markdown style headings

0.0.5
======

Fixed pypi repo link and set pypi description to README.

0.0.4
======

Bug fix to background video to not require poster.

0.0.3
======

Added full deck footer and header configuration and styling.

Also started documentation with a section on header and footer.

0.0.2
======

Fix to get webslides resources in pypi upload action.

0.0.1
======

Initial Release