from apps.models import Model


class Loan(Model):
    __table__ = 'loans'
    __primary_key__ = 'loanid'
