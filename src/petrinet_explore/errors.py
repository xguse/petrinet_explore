#!/usr/bin/env python
"""Provide error classes for petrinet_explore."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class Petrinet_exploreError(Exception):

    """Base error class for petrinet_explore."""


class ValidationError(Petrinet_exploreError):

    """Raise when a validation/sanity check comes back with unexpected value."""
