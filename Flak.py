from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    name = ''
    food = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        food = request.form.get('food')
    return render_template("index.html", name = name, food = food)




if __name__ == '__main__':
    app.run()
else:
    print("NO")
