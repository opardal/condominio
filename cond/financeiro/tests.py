from django.test import TestCase

# Create your tests here.

from .models import Despesa


class DespesaModelTests(TestCase):

    def test_sem_valor(self):
        with self.assertRaises(ValueError):
            d = Despesa(nome='Teste', valor='Teste')
            d.save()

