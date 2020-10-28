from flask import Blueprint
from flask import render_template
from werkzeug.utils import redirect

from experiment.forms import CallbackForm, RequestForm

experiment = Blueprint('experiment', __name__, template_folder='templates')


@experiment.route('/thx')
def thx():
    return render_template('experiment/thx.html')


@experiment.route('/', methods=['GET', 'POST'])
def index():
    callback_form = CallbackForm()
    request_form = RequestForm()

    if callback_form.validate_on_submit():
        return render_template('experiment/index.html', callback_form=callback_form, request_form=request_form)
    if request_form.validate_on_submit():
        return redirect('thx')

    return render_template('experiment/index.html', callback_form=callback_form, request_form=request_form)
