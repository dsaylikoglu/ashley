from recorder import Recorder

class Record():
    def __init__(self):
        pass

    def record_voice(self, duration):
        rec = Recorder()
        np_data = rec.record(duration, output='out.wav')
        print(np_data)
        rec.close()
