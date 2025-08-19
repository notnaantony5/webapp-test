from database import session_maker, PostModel

def main():
    with session_maker() as session:
        posts = session.query(PostModel).all()
        print(posts)

if __name__ == "__main__":
    main()
