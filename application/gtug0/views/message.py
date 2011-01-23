# -*- coding: utf-8 -*-
"""
gtug0.views
"""

import logging
import base64
import datetime
import simplejson as json

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
  render_to_response, render_json_response,
  reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

from gtug0.models import (LoginUser)


# Create your views here.

@login_required
def update(request):
  message = request.form.get("message")
  logging.debug(message)

  login_user = LoginUser.search_user(users.get_current_user())
  client_id  = login_user.client_id

  data = {
    "data": {
      "user": login_user.user.nickname(),
      "updated_at": str(datetime.datetime.now()),
      "message": message
      }
    }

  login_users = LoginUser.get_loggedin_user()
  for u in login_users:
    u_id = u.client_id
    channel.send_message(u_id, json.dumps(data))

  return render_json_response(data)

