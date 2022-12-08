from app import app, controller

app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/login', 'login', controller.login, methods=['get', 'post'])

if __name__ == '__main__':
    app.run(debug=True)
