from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

engine = create_engine('postgresql+psycopg2://postgres:12345678@localhost/postgres')


def log_pg_stat_activity():
    '''Log, write or send through Sentry pg_stat_activity'''
    debug_conn = engine.connect()
    for process in debug_conn.execute('''
        SELECT pid, application_name, state, query FROM pg_stat_activity;
    ''').fetchall():
        print(process)

@contextmanager
def connection():
    conn = engine.connect()
    try:
        yield conn
    except OperationalError as ex:
        log_pg_stat_activity()
        raise


@contextmanager
def transaction():
    with connection() as conn:
        with conn.begin() as trans:
            try:
                yield conn
            except OperationalError as ex:
                if 'deadlock detected' in ex.args[0]:
                    log_pg_stat_activity()
                    # Log exception
                    print(ex)
                    trans.rollback()
                else:
                    raise
