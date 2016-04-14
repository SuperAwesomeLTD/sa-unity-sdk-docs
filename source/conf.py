import sys
import os

# project variables
project = '<sdk_project>'
copyright = '<sdk_company>'
author = '<sdk_author>'
version = '<sdk_version>'
release = '<sdk_version>'

# theme config
html_theme = '<sdk_theme>'
html_theme_options = {"logo_only":True}
html_theme_path = ["<sdk_theme_folder>",]
html_logo = '<sdk_themeres_folder>/logo.png'
html_context = {
    'all_versions' : ['3.0.9'],
    'domain': '<sdk_aa_domain>',
    'sourcecode': '<sdk_source>'
}

# aux vars
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
show_authors = True
pygments_style = 'sphinx'
todo_include_todos = False
