from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import check_password_hash

# Create convention for SQLAlchemy naming
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class Catalogue(db.Model, SerializerMixin):
    __tablename__ = "catalogues"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    news = db.relationship('News', back_populates='catalogue')
    addcatalogues = db.relationship('AddCatalogue', back_populates='catalogue')

class AddCatalogue(db.Model, SerializerMixin):
    __tablename__ = "addcatalogues"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Text, nullable=False)
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogues.id'))
    catalogue = db.relationship('Catalogue', back_populates='addcatalogues')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='addcatalogues')

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    news = db.relationship('News', back_populates='user')
    addcatalogues = db.relationship('AddCatalogue', back_populates='user')

    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)

class News(db.Model, SerializerMixin):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    ticket_price = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogues.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    catalogue = db.relationship('Catalogue', back_populates='news')
    user = db.relationship('User', back_populates='news')