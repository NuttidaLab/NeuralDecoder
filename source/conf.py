# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Add the parent directory of the RepKit module to sys.path
sys.path.insert(0, os.path.abspath('../'))

project = 'RepKit'
copyright = '2023, NuttidaLab'
author = 'Rudramani Singha'
release = 'v2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', 
    'myst_parser',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    ]

# Add the following line to exclude classes inherited from object from the documentation
# autodoc_default_options = {'members': True, 'undoc-members': True, 'private-members': True, 'special-members': "__init__", 'inherited-members': True, 'show-inheritance': True,}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = "RepKit"
html_static_path = ['_static']
