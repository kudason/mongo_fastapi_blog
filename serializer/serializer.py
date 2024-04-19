### ========== Convert Blog to dict() type ========== ###
def convertBlog(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "description": blog["description"],
        "content": blog["content"],
        "author": blog["author"]
    }


### ========== Convert a List of Blog to dict() type ========== ###
def convertBlogs(blogs) -> list:
    return [convertBlog(blog) for blog in blogs]