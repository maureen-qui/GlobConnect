from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required
from app import app, db, bcrypt
from app.models import User, GroupCreationForm
from app.forms import RegistrationForm, LoginForm, CollaborationGroup

@app.route('/dashboard')
@login_required
def dashboard():
    # Load user's created and joined groups
    # ... your logic to retrieve data ...
    return render_template('manage_groups.html', created_groups=created_groups, joined_groups=joined_groups)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/manage_groups')
def manage_groups():
    # Simulated data, replace with your actual data retrieval logic
    created_groups = [
        {'id': 1, 'name': 'Tech Enthusiasts', 'description': 'Group for tech discussions'},
        # ...
    ]
    joined_groups = [
        {'id': 2, 'name': 'Creative Minds', 'description': 'Group for creative ideas'},
        # ...
    ]
    return render_template('manage_groups.html', created_groups=created_groups, joined_groups=joined_groups)

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    form = GroupCreationForm()

    if form.validate_on_submit():
        group = CollaborationGroup(
            name=form.group_name.data,
            description=form.group_description.data,
            creator_id=1  # Replace with the actual user ID of the creator
        )
        db.session.add(group)
        db.session.commit()
        # Redirect to a success page or another route
        return redirect(url_for('group_created'))

    return render_template('create_group.html', form=form)
