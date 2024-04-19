### ============= Import Library ============= ###
from config.config import *                    ###
from serializer.serializer import *            ### 
from fastapi import HTTPException, status      ###
from bson import ObjectId                      ### 
### ============= Import Library ============= ###


### ================ Define function ================== ###
def home():
    return {
        "status": "ok",
        "message": "My fastapi is running"
    }

def create(blog):
    blogsCollection.insert_one(dict(blog))
    return {
        "status": "Ok",
        "message": "Data inserted successful!"
    }

def getAll():
    blogs = blogsCollection.find()
    convertedBlogs = convertBlogs(blogs)
    return {
        "status": "Ok",
        "data": convertedBlogs
    }

def getId(id):
    blog = blogsCollection.find_one({"_id": ObjectId(id)})

    if blog is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found blog with id {id} :((")
    
    convertedBlog = convertBlog(blog)

    return {
            "status": "Ok",
            "data": convertedBlog
        }

def update(id, blog):
    blog_ = blogsCollection.find_one({"_id": ObjectId(id)})

    if blog_ is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found blog with id {id} :((")

    blogsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(blog)}
    )

    return {
        "status": "Ok",
        "message": "Data has been updated successfully!"
    }

def delete(id):
    blog_ = blogsCollection.find_one({"_id": ObjectId(id)})

    if blog_ is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found blog with id {id}")

    blogsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "status": "Ok",
        "message": "blog has been deleted successfully!"
    }
### ================ Define function ================== ###
