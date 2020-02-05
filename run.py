from mvc import app
from werkzeug.serving import run_simple


if __name__ == "__main__":
    # app.run(debug=True, use_reloader=True)
    run_simple('localhost', 5000, app, use_reloader= True, use_debugger = True)