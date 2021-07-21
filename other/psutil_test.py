import psutil
import time


class TestPSUtil:
    def get_network(self):
        recv1 = psutil.net_io_counters().bytes_recv / 1024
        sent1 = psutil.net_io_counters().bytes_sent / 1024
        time.sleep(1)
        recv2 = psutil.net_io_counters().bytes_recv / 1024
        sent2 = psutil.net_io_counters().bytes_sent / 1024
        recv = recv2 - recv1
        sent = sent2 - sent1
        res = [
            "input:" + str(round(recv, 2)) + " " + "kb/s",
            "output: " + str(round(sent, 2)) + " " + "kb/s",
        ]
        # print(' '.join(res))
        # ['input:0.08 kb/s', 'output: 0.05 kb/s']

        return res

    def test_get_network(self):
        while True:
            print(self.get_network())
