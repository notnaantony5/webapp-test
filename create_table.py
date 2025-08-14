from sqlite3 import connect

def main():
    conn = connect("test.sqlite3")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE posts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT,
        created_at TEXT,
        CONSTRAINT posts_title UNIQUE (title)
    )""")

if __name__ == "__main__":
    main()