# -*- coding: utf-8 -*-
# home.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('home/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'home/index': 'home.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='home.views.index'),
  )
]

