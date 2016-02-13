from catalog import app

from flask import session

from wtforms import Form
from wtforms.csrf.session import SessionCSRF

class BaseForm(Form):
    """Base form for the application. Nothing special here for now..."""
    pass

class CSRFForm(BaseForm):
    """Base form with cross site request forgery (CSRF) configuration.
    
    This form uses session-based CSRF, which stores the token in session.
    Calling the form's validate function validates the CSRF token.
    
    See: http://wtforms.readthedocs.org/en/latest/csrf.html 
    """
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']

        @property
        def csrf_context(self):
            return session