# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

#Added a method parameter with value post
form = """
<form method = "get" action = "/testform">
    <input type='text' name='q'>
    <br>
    <input type='password' name='r'>
    <br>
    <label>
        one
        <input type = "radio" name="q" value="one">
    </label>
    <label>
        two
        <input type = "radio" name="q" value="two">
    </label>
    <label>
        three
        <input type = "radio" name="q" value="three">
    </label>
    <label>
        four
        <input type = "radio" name='q' value='four'>
    </label>
    <label>
        five
        <input type = "radio" name='q' value='five'>
    </label>
    <br>
    <select name='r'>
        <option value='1'>One</option>
        <option value='2'>Two</option>
        <option value='3'>Three</option>
    </select>
	<br>
	<input type = "submit">
</form>"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

class TestHandeler(webapp2.RequestHandler):
    def get(self):
        q = self.request.get("q")
        self.response.out.write(q)
        #Below line of code is good for debugging
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/testform',TestHandeler)
], debug=True)
