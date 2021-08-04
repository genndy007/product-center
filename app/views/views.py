from flask_admin.contrib.sqla import ModelView

class FilterAddressesView(ModelView):
    # column_editable_list = ['date', 'amount', ]
    # form_args = dict(
    #     status=dict(query_factory=Expense.status_filter),
    #     category=dict(query_factory=Expense.type_filter),
    # )
    # column_filters = ['date','amount','category','status']
    column_filters = ['country', 'city', 'street']

