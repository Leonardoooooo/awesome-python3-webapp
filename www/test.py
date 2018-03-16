import www.orm, logging, asyncio

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def test():
    try:
        print('program start')
        yield from www.orm.create_pool(loop, user='root', password='tuniu520', db='chen')
        from www.models import User
        u = User(name='Test', email='test2@example.com', passwd='111111', image='about:blank')
        yield from u.save()
        print('program end')
    except BaseException as e:
        logging.exception(e)


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
