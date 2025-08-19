from database import session_maker, PostModel

def main():
    with session_maker() as session:
        post = session.query(PostModel
            ).filter(PostModel.id == 2
                ).filter(
                    ).first()
        print(post)

if __name__ == "__main__":
    main()
