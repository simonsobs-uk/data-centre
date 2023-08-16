html_css_files = [
    "https://cdn.jsdelivr.net/gh/ickc/markdown-latex-css/css/_table.min.css",
    "https://cdn.jsdelivr.net/gh/ickc/markdown-latex-css/fonts/fonts.min.css",
]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
    "myst_parser",
]
source_suffix = [".md", ".rst"]
master_doc = "index"
project = 'SO:UK Data Centre'
year = "2023"
author = "SO:UK Collaborators"
copyright = f"{year}, {author}"
version = release = "0.1.0"

pygments_style = "solarized-light"
html_theme = "furo"

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

# sphinxcontrib.apidoc
apidoc_module_dir = '../src/souk_data_centre'
apidoc_separate_modules = True
apidoc_module_first = True
