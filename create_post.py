from database import session_maker, PostModel

def main():
    with session_maker() as session:
        post = PostModel(title="Пример1",content="1")
        post2 = PostModel(title="Пример2",content="2")
        session.add(post)
        session.add(post2)
        session.commit()


if __name__ == "__main__":
    main()
