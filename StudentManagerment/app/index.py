from app import app, controller, dao, login
from app.admin import *

app.add_url_rule('/', 'index', controller.index)
app.add_url_rule('/logout', 'logout', controller.logout_my_user)
app.add_url_rule('/login', 'login', controller.user_login, methods=['get', 'post'])


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
