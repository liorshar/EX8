from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def cv_Page():
    flag=True
    if flag:
        return render_template('cv.html')
    else:
        return redirect(url_for('movies_templates'))

@app.route('/assignment8')
def movies_templates():
    #DB
    return render_template('assignment8.html', MoviesList=('The Ugly Truth','The Curious Case of Benjamin Button','The Avengers','X-Men'))

if __name__ == '__main__':
    app.run()
