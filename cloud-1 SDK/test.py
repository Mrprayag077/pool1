import webapp2
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            "<center><h1>Hello class, Welcome to Cloud Computing Lab Practical 1 :)</h1>")



app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
