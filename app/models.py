from db import db
from app import app

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100))
    email = db.Column(db.String(30), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    # role = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

# class Role(db.Model):
#     __tablename__ = "roles"

#     id = db.Column(db.Integer, primary_key=True)

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(18), nullable=False)
    proposals = db.relationship('Proposal', backref=db.backref("customer", cascade='all,delete'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class Proposal(db.Model):
    __tablename__ = "proposals"

    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date_of_proposals = db.Column(db.DateTime, nullable=False)
    num_of_roofs = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    geocoordinates = db.Column(db.String(80), nullable=False)
    sketchup_model = db.Column(db.String(60), nullable=True)
    status = db.Column(db.String(20), nullable=False)
    roofs = db.relationship("Roof", backref=db.backref("proposal", cascade='all,delete'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Proposal {self.customer}'

class Roof(db.Model):
    __tablename__ = "roofs"

    id = db.Column(db.Integer, primary_key= True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposals.id'))
    pv_panel = db.Column(db.Integer, nullable=True)
    pv_panel_qty = db.Column(db.Integer, nullable=True)
    pv_mount = db.Column(db.Integer, nullable=True)
    pv_cable = db.Column(db.Integer, nullable=True)
    add_construction_qty = db.Column(db.Integer, nullable=True)
    add_construction_price = db.Column(db.Integer, nullable=True)
    azimuth = db.Column(db.Integer, nullable=False)
    angle = db.Column(db.Integer, nullable=False)
    solar_data = db.relationship("SolarYearData", backref=db.backref('roof', cascade='all,delete'))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Roof {self.id}>'

class SolarYearData(db.Model):
    __tablename__ = "solaryeardatas"

    id = db.Column(db.Integer, primary_key = True)
    roof_id = db.Column(db.Integer, db.ForeignKey('roofs.id'))
    monthly = db.relationship('SolarMonthData', backref=db.backref("year", cascade='all,delete'))
    energy = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<SolarYearData {self.energy}>'

class SolarMonthData(db.Model):
    __tablename__ = "solarmonthdatas"

    id = db.Column(db.Integer, primary_key = True)
    year_id = db.Column(db.Integer, db.ForeignKey('solaryeardatas.id'))
    month = db.Column(db.String(15))
    energy_perday = db.Column(db.Integer, nullable=True)
    energy = db.Column(db.Integer)
    hourly = db.relationship('SolarHourData', backref=db.backref("month", cascade='all,delete'))

    def __repr__(self):
        return f'<SolarMonthData {self.energy}>'

class SolarHourData(db.Model):
    __tablename__ = "solarhourdatas"

    id = db.Column(db.Integer, primary_key = True)
    month_id = db.Column(db.Integer, db.ForeignKey('solarmonthdatas.id'))
    hour = db.Column(db.Integer)
    energy = db.Column(db.Integer)

    def __repr__(self):
        return f'<SolarHourData {self.energy}>'