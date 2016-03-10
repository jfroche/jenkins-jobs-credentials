#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from testtools import TestCase
from testscenarios.testcase import TestWithScenarios
from tests.base import get_scenarios, BaseTestCase
from jenkins_jobs_credentials import properties


class TestCaseModuleProperties(TestWithScenarios, TestCase, BaseTestCase):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    scenarios = get_scenarios(fixtures_path)
    klass = properties.Properties
