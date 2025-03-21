# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'assignment2'
copyright = '2025, Yousef'
author = 'Yousef'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import subprocess
import sys
from unittest.mock import MagicMock
# Mock missing ROS dependencies
MOCK_MODULES = ["tf","rospy", "actionlib","assignment_2_2024","assignment_2_2024.srv", "geometry_msgs.msg", "nav_msgs.msg", "std_msgs.msg", "assignment_2_2024.msg"]
sys.modules.update((mod, MagicMock()) for mod in MOCK_MODULES)
# sys.path.insert(0, os.path.abspath('../'))
# subprocess.call('doxygen Doxyfile.in', shell=True)
sys.path.insert(0, os.path.abspath('../../part1_ws/src/assignment_2_2024/scripts'))
sys.path.insert(0, os.path.abspath('../doxy'))

subprocess.call('doxygen $(pwd)/../doxy/Doxyfile', shell=True)
print(sys.path)
extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.doctest',
'sphinx.ext.intersphinx',
'sphinx.ext.todo',
'sphinx.ext.coverage',
'sphinx.ext.mathjax',
'sphinx.ext.ifconfig',
'sphinx.ext.viewcode',
'sphinx.ext.githubpages',
"sphinx.ext.napoleon",
'sphinx.ext.inheritance_diagram',
'breathe'
]
highlight_language = 'c++'
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
todo_include_todos = True

breathe_projects = {
"ui_node": "../doxygen/xml/"
}
breathe_default_project = "part2"
breathe_default_members = ('members', 'ui_node')