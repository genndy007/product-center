from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.database.database import Base, engine, db_session
from app.models.models import ProductModel, AddressModel


Base.metadata.create_all(bind=engine)


app = Flask(__name__)


admin = Admin(app, name='product-center')
admin.add_view(ModelView(ProductModel, db_session))
admin.add_view(ModelView(AddressModel, db_session))


app.run()