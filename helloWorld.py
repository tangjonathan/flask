from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'

@app.route('/test')
def testing():
    return 'test'

@app.route('/square/<int:num>')
def f(num):
  # No conversion of x needed.
  return str(num**2)


def factors(num):
  return [x for x in range(1, num+1) if num%x==0]

@app.route('/factors/<int:n>')
def factors_display(n):
	return render_template(
		"factors.html",  # name of template
		number=n,  # value for `number` in template
		factors=factors(n) # value for `factors` in template
	)

@app.route('/factors_raw/<int:n>')
def factors_display_raw_html(n):
	factors_list = factors(int(n))
	# First we put the stuff at the top, adding "n" in there
	html = "<body><h1> The factors of "+str(n)+" are</h1>"+"\n"+"<ul>"

	# for each factor, we make a <li> item for it
	for f in factors_list:
		html += "<li>"+str(f)+"</li>"+"\n"
	html += "</ul> </body>" # the close tags at the bottom
	return html

if __name__ == '__main__':
  app.run(host='0.0.0.0')
