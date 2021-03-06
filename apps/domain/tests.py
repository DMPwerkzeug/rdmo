from django.test import TestCase
from django.utils import translation

from apps.core.test_mixins import *

from .models import *


class DomainTestCase(TestCase):
    fixtures = [
        'testing/accounts.json',
        'testing/domain.json'
    ]


class DomainTests(TestListViewMixin, DomainTestCase):

    list_url_name = 'domain'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')


class AttributeEntityTests(TestModelAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:entity'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = AttributeEntity.objects.first()


class AttributeTests(TestModelAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:attribute'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = Attribute.objects.first()


class OptionTests(TestModelAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:option'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = Option.objects.first()


class RangeTests(TestListAPIViewMixin, TestRetrieveAPIViewMixin, TestUpdateAPIViewMixin, TestDeleteAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:range'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = Range.objects.first()


class ConditionTests(TestModelAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:condition'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = Condition.objects.first()


class VerboseNameTests(TestListAPIViewMixin, TestRetrieveAPIViewMixin, TestUpdateAPIViewMixin, TestDeleteAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:verbosename'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
        self.instance = VerboseName.objects.first()


class ValueTypeTests(TestListAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:valuestype'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')


class RelationTests(TestListAPIViewMixin, DomainTestCase):

    api_url_name = 'domain:relation'

    def setUp(self):
        translation.activate('en')
        self.client.login(username='admin', password='admin')
