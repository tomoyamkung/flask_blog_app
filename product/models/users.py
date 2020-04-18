from flask_login import UserMixin


class Usr(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
