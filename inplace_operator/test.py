
logger = get_logger()


def test_operator():
    logger.info('test_operator start')
    i = 2
    logger.info('i:{}'.format(i))
    i += 1
    logger.info('i:{}'.format(i))
    i -= 1
    logger.info('i:{}'.format(i))
    i *= 2
    logger.info('i:{}'.format(i))
    i <<= 2
    logger.info('i:{}'.format(i))
    i >>= 2
    logger.info('i:{}'.format(i))
    i |= 2
    logger.info('i:{}'.format(i))
    i ^= 2
    logger.info('i:{}'.format(i))
    i &= 4
    logger.info('i:{}'.format(i))
    i //= 2
    logger.info('i:{}'.format(i))
    i /= 2
    logger.info('i:{}'.format(i))
    i %= 3
    logger.info('i:{}'.format(i))
    i **= 2
    logger.info('i:{}'.format(i))
    logger.info('test_operator stop')


def case1():
    logger.info('This is the case1')


def case2():
    logger.info('This is the case2')


def case3():
    logger.info('This is the case3')


def default():
    logger.info('No such case')


def run():
    logger.info("this is a python plugin to demo switch.")
    switch = {'case1': case1,
              'case2': case2,
              'case3': case3,
              }

    i = 0
    while i < 10:
        randnum = random.randint(1, 10)
        choice = "case" + str((randnum % 4))
        switch.get(choice, default)()
        i += 1

    logger.info("pythonplugin_001 - not export data ")


run()
test_operator()


