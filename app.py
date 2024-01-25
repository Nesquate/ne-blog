from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

# Home page, show post list
@app.route('/')
def page_home():
    return render_template('home.html')

# Independent page
@app.route('/pages/<page_id>')
def page_page(page_id):
    return render_template('page.html')

# Post page
@app.route('/post/<post_id>')
def page_post(post_id):
    return render_template('post.html')

# Category related page, including separate post list from special category
@app.route('/categories')
@app.route('/categories/<category_id>')
def page_categories(category_id):
    return render_template('categories.html')

# Tag related page, including separate post list from special tag
@app.route('/tags')
@app.route('/tags/<tag_id>')
def page_tags(tag_id):
    return render_template('tags.html')

# Login page, use basic form method
@app.route('/login', methods=['GET', 'POST'])
def page_login():
    return render_template('login.html')

# Admin page, TBD
@app.route('/admin')
@app.route('/admin/posts')
@app.route('/admin/posts/new')
@app.route('/admin/posts/edit')
@app.route('/admin/posts/delete')
@app.route('/admin/pages')
@app.route('/admin/pages/new')
@app.route('/admin/pages/edit')
@app.route('/admin/pages/delete')
@app.route('/admin/categories')
@app.route('/admin/categories/new')
@app.route('/admin/categories/edit')
@app.route('/admin/categories/delete')
@app.route('/admin/tags')
@app.route('/admin/tags/new')
@app.route('/admin/tags/edit')
@app.route('/admin/tags/delete')
@app.route('/admin/media')
@app.route('/admin/users')
@app.route('/admin/options')
def page_admin_home():
    return render_template('admin.html')
