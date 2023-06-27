#    the CSRF protection is disabled on a form:

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = False # Sensitive

    name = TextField('name')
    submit = SubmitField('submit')