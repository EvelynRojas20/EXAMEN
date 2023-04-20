from logica.modelos import usuarios as u

def create_user(nick_name,description):
    user= u.User(nick_name=nick_name, description=description)
    try:
        u.session.add(user)
        u.session.commit()
        return "sucessfull created user {user.nick_name}"
    except Exception as error:
        u.session.rollback()
        raise Exception(error)