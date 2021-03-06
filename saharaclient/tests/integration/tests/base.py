# Copyright (c) 2014 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import testtools

import saharaclient.tests.integration.tests.clidriver as clidriver
import saharaclient.tests.integration.tests.utils as utils


class ITestBase(testtools.TestCase):
    def setUp(self):
        super(ITestBase, self).setUp()

        # The client is for readonly operations to check results
        self.util = utils.Utils()
        self.cli = clidriver.CLICommands()
