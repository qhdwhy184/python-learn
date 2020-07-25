import sys
from math import *


def test(**kwargs):
    print('plugin:{}'.format(kwargs['record_message']))


def prepare_msg():
    return 'huihui msg.'


test(record_message=prepare_msg())
