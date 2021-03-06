# -*- coding: utf-8 -*-
"""
gtug0.views
"""

import logging


from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

from gtug0.models import (LoginUser)

# Create your views here.

@login_required
def index(request):
  login_user = LoginUser.search_user(users.get_current_user())
  client_id  = login_user.client_id

  token = channel.create_channel(client_id)
  login_user.update_token(token)

  template_value = {
    "token": token
    }
  return render_to_response('gtug0/root/index.html', template_value)
