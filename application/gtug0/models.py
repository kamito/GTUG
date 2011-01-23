# -*- coding: utf-8 -*-
# gtug0.models

import logging
import base64

from google.appengine.ext import db

# Create your models here.

class LoginUser(db.Model):
  user       = db.UserProperty(required=True);
  client_id  = db.StringProperty()
  token      = db.StringProperty()
  tokened_at = db.DateTimeProperty()

  @classmethod
  def search_user(self, user):
    """ search login user """
    gql = LoginUser.gql("WHERE user = :user", user=user)
    login_user = gql.get()
    if login_user == None:
      email = user.email()
      client_id  = base64.b64encode(email)
      login_user = LoginUser(user=user, client_id=client_id)
      login_user.put()

    return login_user


  @classmethod
  def get_loggedin_user(self):
    q = LoginUser.all()
    users = q.fetch(10)
    return users 


  def update_token(self, token):
    """ update channel token """
    self.token = token
    self.put()
    return self

