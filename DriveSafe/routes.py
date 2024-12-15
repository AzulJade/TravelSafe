from flask import render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from DriveSafe import app, db
from DriveSafe.forms import CustomerRegister, CustomerLogin
# from DriveSafe.models import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#forms
@app.route('/customer-registration')
def customer_registration():
    form = CustomerRegister()
    # if form.validate_on_submit():
    #     new_user = User(username=form.username.data, 
    #                     dob = form.date_of_birth.data,
    #                     password = form.password2.data,
    #                     email= form.email.data)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     login_user(new_user)
    #     flash(f'Success creating account! You are logged in as: {new_user.username}', category='success')

    #     return redirect(url_for('virtual_payment_page'))
    
    # if form.errors != {}:
    #     for error_message in form.errors.values():
    #         flash(f'There was an error in creating the user: {error_message}', category="danger")
    return render_template('customer-register.html', form=form)


@app.route('/customer-login')
def customer_login_page():
    form = CustomerLogin()
    # if form.validate_on_submit():
    #     attempted_user = User.query.filter_by(username=form.username.data).first()
    #     if attempted_user and attempted_user.check_password_correction(attempted_user=form.password.data):
    #         login_user(attempted_user)
    #         flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
    #         return redirect(url_for('virtual_payment_page'))
    #     else:
    #         flash('Username and password are not match! Please try again', category='danger')
    return render_template('customer-log-in.html', form=form)


@app.route('/avoid-travel-scams')
def avoid_travel_scams_page():
    return render_template('avoid-travel-scams.html')

@app.route('/journey-history')
def journey_history_page():
    return render_template('journey-history.html')

@app.route('/search-bar')
def search_bar_page():
    return render_template('search-bar.html')

@app.route('/legitimate-taxis')
def legitimate_taxis_page():
    return render_template('legitimate-taxis.html')

@app.route('/taxi-finder')
def taxi_finder_page():
    return render_template('taxi-finder.html')

@app.route('/secure-payments')
def secure_payments_page():
    return render_template('secure-payments.html')

@app.route('/realtime-alerts')
def realtime_alerts_page():
    return render_template('realtime-alerts.html')

@app.route('/recent-incidents')
def recent_incidents_page():
    return render_template('recent-incidents.html')

@app.route('/payment-security-info')
def payment_security_info_page():
    return render_template('payment-security-info.html')

@app.route('/notify-guidance')
def notify_guidance_page():
    return render_template('notify-guidance.html')

@app.route('/safety-tips')
def safety_tips_page():
    return render_template('safety-tips.html')

@app.route('/contact-support')
def contact_support_page():
    return render_template('contact-support.html')

@app.route('/est-travel-time')
def est_travel_time_page():
    return render_template('est-travel-time.html')

@app.route('/interactive-map')
def interactive_map_page():
    return render_template('interactive-map.html')

@app.route('/virtual-payment')
def virtual_payment_page():
    return render_template('virtual-payment.html')

@app.route('/crime-hotspots')
def crime_hotspots_page():
    return render_template('crime-hotspots.html')

@app.route('/regional-safety')
def regional_safety_page():
    return render_template('regional-safety.html')

@app.route('/about')
def about_page():
    return render_template('about.html')