# Installation

Python and pip are prerequisites for installation.  With these
properly configured, install via pip:

```
pip install sphinx-webslides-builder
```

## Local Development Installation

Installing from the repo directly is a 2 step process due
to the WebSlides assets not being present in the repo.
Install with the following:

```
bash .github/scripts/get_webslides.sh
pip install -e .
```