import threading


class MyThread(threading.Thread):
    def __init__(self, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        # 2. Determine thread exit mechanism

    def run(self):
        # 3. Replace pass with run method implementation
        pass


def __main__():
    # 1. Create objects of ARP and ICMP class. Use ICMP provided in helper.py module

    # 4. Create MyThread objects for ARP and ICMP send_data methods

    # 5. Start threads

    input()

    # 6. After any input exit run method

    # 7. Wait for threads to exit


if __name__ == "__main__":
    __main__()
