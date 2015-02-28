
import os
import web
from web import form
from PyGlow import PyGlow
pyglow = PyGlow()
# Define the pages (index) for the site
urls = ('/', 'index')
render = web.template.render('templates')

app = web.application(urls, globals())

# Define the buttons that should be shown on the form
my_form = form.Form(
 form.Button("btn", id="btnR", value="R", html="Red", class_="btnRed"),
 form.Button("btn", id="btnG", value="G", html="Fade", class_="btnGreen"),
 form.Button("btn", id="btnO", value="0", html="-Off-", class_="btnOff")
)

# define what happens when the index page is called
class index:
    # GET us used when the page is first requested
    def GET(self):
        form = my_form()
        return render.index(form, "Raspberry Pi Python Remote Control")

    # POST is called when a web form is submitted
    def POST(self):
        # get the data submitted from the web form
        userData = web.input()

        # Determine which colour LedBorg should display
        if userData.btn == "R":
           print "RED"
           pyglow.color("red", 255)
        elif userData.btn == "G":
             print "GREEN"
             os.system("sudo python /var/www/pyserver/fade.py")
        elif userData.btn == "0":
             pyglow.all(0)
	     os.system("pkill -f fade.py")
	     pyglow.all(0)
             print "Lamp Off"
        else:
             print "Do nothing else - assume something fishy is going on..."


        # reload the web form ready for the next user input
        raise web.seeother('/')
# run
if __name__ == '__main__':
    app.run()
