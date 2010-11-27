# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import cyraxlib

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Cyrax'
copyright = u'2009-2010, Alexander Solovyov'
version = release = cyraxlib.__version__
exclude_trees = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
html_style = 'custom.css'
html_title = "%s v%s" % (project, version)
html_static_path = ['_static']
html_use_smartypants = True
html_use_index = False
html_show_sourcelink = False
