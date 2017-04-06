import datetime
from bottle import route, run, template, static_file, error, post, request

servers = []
user_types = []

@route('/')
def index():
    message = "Automated-testing.info"
    now_time = datetime.datetime.now()
    cur_hour = now_time.hour
    return template('page_template', cur_hour=cur_hour,  msg=message)


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,
                       root=r'D:\books\_Python_\bottle_example\user_maker\static')


@route('/images/<filename>')
def send_image(filename):
    return static_file(filename,
                       root=r'D:\books\_Python_\bottle_example\user_maker\image',
                       mimetype='image/png')


@route('/create_user')
def user_create():
    return template('user_forms', servers=servers, user_types=user_types)


@post('/create_user')
def user_create():
    user_type = request.forms.get('user_type')
    server = request.forms.get('server')
    return "<p>User: {}; Server: {}</p>".format(user_type, server)


def define_servers():
    return ['AUTOTEST_ART', 'AUTOTESTS_MAPS']


def define_user_types():
    return ['press', 'clan_creator']

@error(404)
@error(403)
def mistake(code):
    return 'Error on page'

if __name__ == "__main__":
    user_types = define_user_types()
    servers = define_servers()
    run(host='localhost', port=8080)