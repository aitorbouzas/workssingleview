import logging

from server.core import db

part_file_extensions = {
    'application/pdf': 'pdf',
    'text/html': 'html',
    'text/plain': 'txt'
}


def commit():
    try:
        db.session.commit()
    except Exception as eException:
        logging.error(eException)
        db.session.rollback()
    finally:
        db.session.close()


# CREATE, UPDATE, DELETE transactions
def add_sqlalchemy_object(sqlalchemy_object, commit_=False):
    return _save_sqlalchemy_object(sqlalchemy_object, commit_=commit_, refresh=True)


def update_sqlalchemy_object(sqlalchemy_object, commit_=False):
    return _save_sqlalchemy_object(sqlalchemy_object, commit_=commit_)


def _save_sqlalchemy_object(sqlalchemy_object, commit_=False, refresh=False):
    try:
        db.session.add(sqlalchemy_object)
        db.session.flush()
        if commit_:
            db.session.commit()
        if refresh:
            db.session.refresh(sqlalchemy_object)
    except Exception as eException:
        db.session.rollback()
        raise eException

    return sqlalchemy_object


def delete_sqlalchemy_object(sqlalchemy_object):
    try:
        db.session.delete(sqlalchemy_object)
    except Exception as eException:
        db.session.rollback()
        raise eException

    return True
