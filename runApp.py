from mainApp import app  # this is the main app process
from AudioRecordService import app1
from frameCaptureService import app2
import multiprocessing

from preview import app3


def main_app():
    app.run(debug=True, port=5000, threaded=True)


def audio_capture():
    app1.run(debug=True, port=5001, threaded=True)


def frame_capture():
    app2.run(debug=True, port=5002, threaded=True)


def run_preview():
    app3.run(debug=True, port=5003, threaded=True)


if __name__ == '__main__':
    # app.run(debug=True, threaded=True)  # enable debug to debug frequent changes without restarting application

    p1 = multiprocessing.Process(target=main_app)
    p2 = multiprocessing.Process(target=audio_capture)
    #p3 = multiprocessing.Process(target=frame_capture)
    # p4 = multiprocessing.Process(target=run_preview)

    p1.start()
    p2.start()
    #p3.start()
    # p4.start()

    p1.join()
    p2.join()
    #p3.join()
    # p4.join()

    # @app.route('/startPreview', methods=['POST'])
    # def start_preview():
    #     p1.start()
    #     p1.join()
    #
    #
    # @app.route('/stopPreview', methods=['POST'])
    # def stop_preview():
    #     p1.terminate()
