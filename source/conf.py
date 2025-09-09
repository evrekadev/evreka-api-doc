# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Evreka360 API'
copyright = '2024, Evreka'
author = 'Evreka'
version = '1.19.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinxawesome_theme",
]

templates_path = ['_templates']
exclude_patterns = []

"""
html_theme_options = {
    "extra_header_links": {
        "Evreka360 Dashboard": "https://360.evreka.co",
    }
}
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

highlight_language = 'python'

extensions = ['rst2pdf.pdfbuilder']
pdf_documents = [('index', u'Evreka360Doc', u'Evreka360 API Doc', u'Evreka'), ]
