from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

class YdForm(Form):
    Nmin = StringField('Nmin')
    Nmax = StringField('Nmax')
    Ncur = StringField('Ncur')
    user_requests = TextAreaField('Искомые слова')
    results = TextAreaField('Результат', id='results')
