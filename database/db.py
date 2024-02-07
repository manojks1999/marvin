import sqlite3


class NotFoundError(Exception):
    pass

class SQLite():
    def __init__(self, file='application.db'):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file, isolation_level=None)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        print("Closing the connection")
        self.conn.close()


def get_db_history(user_id):
    try:
        result  = None
        with SQLite() as cur:
            cur.execute("SELECT data, created_at FROM history WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
            result = cur.fetchall()
            if result is None or len(result) == 0:
                raise NotFoundError(f'Unable to find history with user id {user_id}.')
            return result
    except NotFoundError as not_found_error:
        print(f"Error in getting histrory: {not_found_error}")
        return []
    except Exception as error:
        print(f"Error in getting histrory: {error}")
        raise error

def add_history(user_id, data):
    try:
        with SQLite() as cur:
            cur.execute("INSERT INTO history(user_id, data) VALUES (?, ?)", (user_id, data))
    except Exception as error:
        print(f"Error in adding history: {error}")
        raise error
        