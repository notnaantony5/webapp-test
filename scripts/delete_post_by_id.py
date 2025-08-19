from database import session_maker, PostModel

def main():
    with session_maker() as session:
        session.query(PostModel).filter(PostModel.id == 2).delete()
        session.commit()


if __name__ == "__main__":
    main()
