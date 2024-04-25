# Product LST

This repository is aimed at providing publicly:
- LST30 related documentation
- LST30 demo data
- ET related documentation

Website is available [here](https://constellr.github.io/product-lst/)

# Usage

To update the website

1. Edit the markdown files (*.md) from the docs folder on the 'main' branch
2. If you want to test locally that it works as intended use 'mkdocs build'. This requires your environement to be properly setup -> 'pdm sync'.
3. Run 'mkdocs gh-deploy --clean'

Warning, 'mkdocs gh-deploy' requires github pages to be enabled but set on no branch -> like this:
![github-pages-setup](docs/images/github-pages-setup.png)