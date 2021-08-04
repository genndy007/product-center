from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


admin = Admin(app, name='product-center', template_mode='bootstrap3')

app.run()