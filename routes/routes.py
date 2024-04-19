### ========== Import Library ========== ###
from model.model import Blog             ###
from serializer.serializer import *      ### 
from config.config import *              ###
from fastapi import APIRouter            ###
from controllers import controllers      ###
### ========== Import Library ========== ###


### ========== Define Router ========== ###
endPoints = APIRouter()                 ###
### ========== Define Router ========== ###


### ======================= Define Operator ====================== ###
                                                                   ### 
# initial status                                                   ###     
@endPoints.get("/")                                                ### 
def home_entry():                                                  ### 
    return controllers.home()                                      ###     
                                                                   ### 
# create a new blog                                                ###
@endPoints.post('/blog')                                           ###     
def create_blog(blog: Blog):                                       ### 
    return controllers.create(blog)                                ### 
                                                                   ### 
# get all blogs                                                    ### 
@endPoints.get("/all/blog")                                        ### 
def get_all_blogs():                                               ### 
    return controllers.getAll()                                    ### 
                                                                   ### 
# get blog by id                                                   ### 
@endPoints.get("/blog/{id}")                                       ### 
def get_blog_by_id(id: str):                                       ### 
    return controllers.getId(id)                                   ###     
                                                                   ### 
# update blog by id                                                ### 
@endPoints.put('/blog/{id}')                                       ### 
def update_blog_by_id(id: str, blog: Blog):                        ### 
    return controllers.update(id, blog)                            ### 
                                                                   ### 
# delete blog by id                                                ### 
@endPoints.delete('/blog/{id}')                                    ###     
def delete_blog_by_id(id: str):                                    ### 
    return controllers.delete(id)                                  ### 
### ======================= Define Operator ====================== ###
