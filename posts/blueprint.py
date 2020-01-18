from flask import Blueprint, jsonify
from flask import render_template
from models import Post, Tag
from flask import request
from .forms import PostForm, YdForm
from app import db
from flask import redirect
from flask import url_for
from flask_security import login_required
from bs4 import BeautifulSoup
import requests
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/yd_forms_parser', methods=['POST', 'GET'])
def yd_forms_parser():
    form = YdForm()

    if request.method == 'POST':

        Nmin = request.form['Nmin']
        Nmax = request.form['Nmax']
        Ncur = request.form['Ncur']
        user_requests = request.form['user_requests']
        results = {}
        results['result'] = ''
        # Очищаем пользовательсикие запросы от \n, \r и пустых
        temp = user_requests.split('\n')
        requests_clear = []
        for r in range(0, len(temp)):
            if temp[r] != '' and temp[r] != '\r':
                requests_clear.append(temp[r].replace('\r', ''))

        for N in range(int(Nmin), int(Nmax)+1):
            Ncur = N
            url = f'https://forms.yandex.ru/surveys/{N}/'
            html = requests.get(url)
            soup = BeautifulSoup(html.text, 'html.parser')
            
            if soup.find('h1') is not None:
                title = soup.find('h1').text
                print(title)
                for r_с in requests_clear:
                    if r_с.lower() in title.lower():
                        results['result'] += url + '\n'
                        print(results)

                        return jsonify(results)

        # form.Nmin.data = Nmin
        # form.Nmax.data = Nmax
        # form.Ncur.data = Ncur
        # form.user_requests.data = user_requests
        #
        # form.results.data = results
        # return render_template('posts/yd_forms_parser.html', form=form)
    return render_template('posts/yd_forms_parser.html', form=form)


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('PORBLEMS')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        # post.title = request.form['title']
        # post.body = request.form['body']
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():

    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
