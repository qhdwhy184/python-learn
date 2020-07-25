import gevent
# from gevent import kill
import greenlet
import signal


def run_forever():
    print("1. run_forever")
    gevent.sleep(1)
    print("2. run_forever")


if __name__ == '__main__':
    print("1. __main__")
    print('gevent is coming from %s' % gevent.__file__)
    # gevent.signal(signal.SIGQUIT, kill)
    thread = gevent.spawn(run_forever)
    pool = gevent.get_hub().destroy(True)
    pool.shutdown()
    thread.join()
    print("2. __main__")
