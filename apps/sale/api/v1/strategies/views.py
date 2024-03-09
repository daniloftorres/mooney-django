from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class calculateSaleTransactionItem ():
    # get all SaleTransactionItem with sum menus discount
    # update SaleTransaction
    # # total_amount
    # # total_discount_amount
    # # net_amount
    # # tax_amount
    # # return SaleTransaction
    pass


class SaleTransactionNew():
    # create SaleTransactio in status creating
    pass


class AddSaleTransactionItem():
    # adiciona item no SaleTransactionItem
    # self.calculateSaleTransactionItem
    # retonar Json Venda Complet Com novos Valores
    pass


class UpdateSaleItem():
    # atualiza item no SaleTransactionItem
    # self.calculateSaleTransactionItem
    # retonar Json Venda Completo Com novos Valores
    pass


class RemoveSaleItem():
    # remove item no SaleTransactionItem
    # self.calculateSaleTransactionItem
    # retonar Json Venda Completo Com novos Valores
    pass


class AddPaymentMethodSaleTransaction():
    # adiciona PaymentMethod no PaymentMethodSaleTransaction
    # self.calculatePaymentMethodSaleTransaction()
    # retonar Json Venda Completo Com novos Valores (Foco Valor Devido)
    pass


class RemovePaymentMethodSaleTransaction():
    # adiciona PaymentMethod no PaymentMethodSaleTransaction
    # self.calculatePaymentMethodSaleTransaction()
    # retonar Json Venda Completo Com novos Valores (Foco Valor Devido)
    pass
