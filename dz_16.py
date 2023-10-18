from flask import Flask, render_template

app = Flask(__name__)

@app.route('/page1')
def page1():
    return render_template('page.html', background_color='red')

@app.route('/page2')
def page2():
    return render_template('page.html', background_color='blue')

@app.route('/page3')
def page3():
    return render_template('page.html', background_color='green')

@app.route('/page4')
def page4():
    return render_template('page.html', background_color='yellow')

#if __name__ == '__main__':

app.run()
