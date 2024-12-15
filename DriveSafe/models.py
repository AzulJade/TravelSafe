# from DriveSafe import db
# from DriveSafe import bcrypt

# class User(db.Model):
#     id = db.Column(db.Integer(),primary_key=True)
#     balance = db.Column(db.Integer(), nullable=False, default=0)
#     dob = db.Column(db.DateTime(), nullable= False)
#     username = db.Column(db.String(), nullable=False)
#     email = db.Column(db.String(), nullable=False)
#     password = db.Column(db.String(), nullable = False)
#     historyID = db.relationship('History', backref='travelled_by', lazy = True)

#     @property
#     def password(self):
#         return self.password
    
#     @password.setter
#     def password(self, plain_text_password):
#         self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

#     def check_password_correction(self, attempted_password):
#         return bcrypt.check_password_hash(self.password_hash, attempted_password)
#         #returns either true or false


# class History(db.Model):
#     record_id = db.Column(db.Integer(), primary_key=True)
#     date = db.Column(db.DateTime(), nullable=False)
#     cost = db.Column(db.Integer(), nullable=False)
#     driver_id =  driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
#     driver = db.relationship('Driver', backref='driven_by', lazy = True)
#     # user_id = db.relationship('User', backref='traveller', lazy = True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
#     cost_id = db.relationship('Cost', backref='amount', lazy = True)


# class Driver(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     route_id = db.relationship('Route', backref="driven_route", lazy=True)
#     username = db.Column(db.String(), nullable=False)
#     password = db.Column(db.String(), nullable=False)
#     driver_id = db.Column(db.String()) #TODO

#     @property
#     def password(self):
#         return self.password
    
#     @password.setter
#     def password(self, plain_text_password):
#         self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


# class Route(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     cost_id = db.relationship('Cost', backref = "is_costed", lazy = True)
#     route_name = db.Column(db.String(), nullable=False)


# class Cost(db.Model):
#     cost_id = db.Column(db.Integer(), primary_key=True)
#     start_location_id = db.Column(db.Integer(), db.ForeignKey('location.id'), nullable= False)
#     end_location_id = db.Column(db.Integer(), db.ForeignKey('location.id'), nullable = False)
#     price = db.Column(db.Integer(), nullable=False)
#     start_location = db.relationship('Location', foreign_keys=[start_location_id], backref="costs_start")
#     end_location = db.relationship('Location', foreign_keys=[end_location_id], backref="costs_end")


# class Location(db.Model):
#     id = db.Column(db.Integer(), primary_key = True)
#     location = db.Column(db.String(), nullable=False)


# class Trip(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     route_id = db.Column(db.String())
#     # driver_id = db.Column(db.Integer(), db.ForeighnKey(''), nullable= False)
