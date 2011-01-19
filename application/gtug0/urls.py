# -*- coding: utf-8 -*-
# gtug0.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('gtug0/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'gtug0/index': 'gtug0.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='gtug0.views.root.index'),
  )
]

