# pylint: skip-file

project = 'Graphene'
copyright = '2019-2022, Gramine Contributors'
author = 'Gramine Contributors'
version = ''
release = ''
extensions = [
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
}

master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
}
html_logo = 'graphene_logo.svg'

html_static_path = ['_static']
