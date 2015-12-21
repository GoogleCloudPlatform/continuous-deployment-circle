# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable
# law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and
# limitations under the License.

"""
This script runs an integration test against a deployed instance of our app.
Replace HOST with the URL your project will be deployed to.
"""

import urllib2
import logging

# The circle.yml deploys to version 1, which maps to this URL
HOST='https://1-dot-continuous-deployment-circle.appspot.com/'

# [START e2e]
response = urllib2.urlopen("{}/get_author/ulysses".format(HOST))
html = response.read()
assert(html == "James Joyce")
# [END e2e]


