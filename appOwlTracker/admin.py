from django.contrib import admin
from .models.user import User
from .models.movements_recorded import Movements_Recorded
from .models.bank_accounts import Bank_Accounts
from .models.categories_section import Categories_Section

admin.site.register(User)
admin.site.register(Movements_Recorded)
admin.site.register(Bank_Accounts)
admin.site.register(Categories_Section)
