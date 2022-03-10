# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
import toml

sys.path.insert(0, os.path.join(os.path.abspath('../..'), 'dacb4ea'))


# Pull metadata from the pyproject.toml file
metadata = toml.load(os.path.join(os.path.abspath('../..'), 'pyproject.toml'))['tool'][
    'poetry'
]

# -- Project information -----------------------------------------------------

project = metadata['name']
copyright = '2022, Jiri VALASEK'
author = 'Jiri VALASEK'
# root_doc = "dacb4ea"

# The full version, including alpha/beta/rc tags
release = metadata['version']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "sphinx.ext.intersphinx",
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
    'sphinx_rtd_theme',
    'autoapi.extension',
]


# Napoleon settings for docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# autodoc settings
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# auto-api settings
autoapi_type = 'python'
autoapi_dirs = [os.path.join(os.path.abspath('../..'), 'dacb4ea')]
autoapi_template_dir = '_templates/autoapi'
autoapi_add_toctree_entry = True
autoapi_generate_api_cos = True
autoapi_root = 'autoapi'
templates_path = ['_templates']
exclude_patterns = [
    os.path.join(os.path.abspath('../..'), 'tests'),
    os.path.join(os.path.abspath('../..'), 'examples'),
]
add_function_parentheses = False
add_module_names = False

# todo settings
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    'vcs_pageview_mode': 'blob',
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    # 'github_url': ''
    # https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
}

html_show_sphinx = False
html_show_copyright = True
