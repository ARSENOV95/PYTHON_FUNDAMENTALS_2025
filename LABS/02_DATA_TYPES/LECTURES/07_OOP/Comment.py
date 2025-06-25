class Comment():
    def __init__(self,username,comment,likes = 0):
        self.username = username
        self.comment = comment
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.comment)
print(comment.likes)