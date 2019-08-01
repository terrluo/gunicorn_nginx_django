#!/usr/bin/python
from django.test.runner import DiscoverRunner


class DJCETestSuiteRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        # have to do this here as the default test runner overrides EMAIL_BACKEND
        super(DJCETestSuiteRunner, self).setup_test_environment(**kwargs)
