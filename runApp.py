from mainApp import app
from mainApp2 import app2
import multiprocessing


def run_app():
    app.run(debug=True, port=5000, threaded=True)


def run_app2():
    app2.run(debug=True, port=5001, threaded=True)


if __name__ == '__main__':
    # app.run(debug=True, threaded=True)  # enable debug to debug frequent changes without restarting application

    p1 = multiprocessing.Process(target=run_app)
    p2 = multiprocessing.Process(target=run_app2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
