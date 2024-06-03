from flask import render_template, request, redirect, url_for, flash
from ..models.user import db, User
from flask_login import login_user, logout_user, current_user, login_required
from app import bcrypt
from ..forms.auth import RegistrationForm, LoginFrom

def dashboard():
  user = User.query.filter_by(email=current_user.email, phone=current_user.phone).first()
  return render_template('sections/users/dashboard.html',user=user)

def submit():
  form = RegistrationForm()
  if form.validate_on_submit():
    Username = form.Username.data
    email = form.email.data
    phone = form.phone.data
    password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

    user = User.query.filter_by(Username=Username).first()
    if user:
      flash('Username already exists.','danger')
      return redirect(url_for('web.submit'))
    
    new_user = User(Username=Username, email=email, phone=phone, password=password)
    try:
      db.session.add(new_user)
      db.session.commit()
      flash('User added successfully!','success')
      return redirect(url_for('web.index'))
    except Exception as e:
      db.session.rollback()
      
  return
