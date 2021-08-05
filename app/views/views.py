from flask_admin.contrib.sqla import ModelView

class FilterAddressesView(ModelView):
    column_filters = ['country', 'city', 'street']

