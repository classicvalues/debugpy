import os
import ptvsd
from flask import Flask
from flask import render_template


ptvsd_host = os.getenv('PTVSD_HOST', 'localhost')
ptvsd_port = os.getenv('PTVSD_PORT', '9879')
ptvsd.enable_attach((ptvsd_host, ptvsd_port))
ptvsd.wait_for_attach()


app = Flask(__name__)


@app.route("/")
def home():
    content = 'Flask-Jinja-Test'
    return render_template(
        "hello.html",
        title='Hello',
        content=content
    )


@app.route("/handled")
def bad_route_handled():
    try:
        raise ArithmeticError('Hello')
    except Exception:
        pass
    return render_template(
        "hello.html",
        title='Hello',
        content='Flask-Jinja-Test'
    )


@app.route("/unhandled")
def bad_route_unhandled():
    raise ArithmeticError('Hello')
    return render_template(
        "hello.html",
        title='Hello',
        content='Flask-Jinja-Test'
    )


@app.route("/exit")
def exit_app():
    from flask import request
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('No shutdown')
    func()
    return 'Done'