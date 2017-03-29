
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################
# Model definitions

class User(db.Model):
    """User table"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    fname = db.Column(db.String(64), nullable=True)
    lname = db.Column(db.String(64), nullable=True)
    subscription = db.Column(db.String(5),nullable=False)

    def __repr__(self):
            """info dispalyed when printed"""
            return '\n<User ID: =%s Email: =%s Password: =%s First Name: =%s Last Name: =%s> Subscription: =%s>' % (self.user_id, self.email, self.password, self.fname, self.lname, self.subscription)


class Order(db.Model):
    """Orders"""
    __tablename__ = "orders"

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    order_id = db.Column(db.String(5), autoincrement=True, primary_key=True)
    item_code = db.Column(db.String(5)), db.ForeignKey('items.item_code')

     # Defining relationships to user
    users = db.relationship("User",
                           backref=db.backref("orders",
                                              order_by=user_id))
    items = db.relationship("Items",
                           backref=db.backref("items",
                                              order_by=item_code))


    def __repr__(self):
            """info dispalyed when printed"""
            return '\nUser ID: =%s Order Id: =%s Item Code: =%s ' % (self.user_id, self.item_code)



class Item(db.Model):
    """Associative table orders & user"""
    __tablename__ = "items"

    item_code = db.Column(db.String(5), primary_key=True)
    item_name = db.Column(db.String(40))



    def __repr__(self):
        """info dispalyed when printed"""
        return '\n<Item Code: =%s Item Name: =%s>' % (self.item_code, self.item_name)



##############################################################################
# Helper functions

def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///reroute'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # from server import app
    # connect_to_db(app)
    # print "Connected to DB."

    def connect_to_db(app, db_uri=None):
        """Connect our application to our database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///reroute'
