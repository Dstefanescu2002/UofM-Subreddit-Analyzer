import json
import numpy as np



def link(posts: np.ndarray, comments: np.ndarray) -> dict:
    """
    posts[:,0] are post ids
    posts[:,1] are post entities (first one that appears)

    comments[:,0] are parent ids
    comments[:,1] are self ids
    comments[:,2] are comment entities (parent's or first one that appears)
    """
    
    linking = {}
    first_level = {}

    # initialize posts in data structure
    for p in posts:
        linking[p[0]] = {"entity":p[1], "children":{}}
    
    # link top-level comments to posts
    for c in comments:
        # if the parent is a post, then I am a top level comment, proceed
        if c[0] in linking: 

            # get entity of parent if I have no entity
            entity = linking[c[0]]["entity"] if c[2] == "NONE" else c[2] 

            # set new entity in the source array
            c[2] = entity 

            # add the comment to the dictionary
            linking[c[0]]["children"][c[1]] = {"entity":entity,"children":{}} 

            # mark this comment as being a top-level comment
            first_level[c[1]] = c[0] 

    # link second-level comments to top-level comments
    for c in comments:
        if c[0] in first_level:
            post = first_level[c[0]]
            entity = linking[post]["children"][c[0]]["entity"] if c[2] == "NONE" else c[2]
            c[2] = entity
            linking[post]["children"][c[0]]["children"][c[1]] = {"entity":c[2]}
    return linking

# posts = [1,2,3]
# comments = [[1,4],[1,9],[2,5],[3,6],[4,7],[5,8]]
# linking = link(posts,comments)
# print(linking)

# json_output = json.dumps(linking, indent=4)
# print(json_output)