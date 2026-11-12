"""Sphinx configuration for GEOMETOR • lemoine."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.lemoine as module  # noqa: E402
from geometor.lemoine.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_french_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "lemoine"
repo_name = "lemoine"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.lemoine.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.lemoine.sphinx_ext")  # noqa: F405

register_french_book_track()
configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

project = "GEOMETOR • lemoine"
author = "Émile Lemoine"
copyright = "1902 C. Naud (Collection Scientia No. 18) • Digital Edition GEOMETOR"

html_static_path = ["_static"]

autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/lemoine/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/lemoine/index.rst")  # noqa: F405
