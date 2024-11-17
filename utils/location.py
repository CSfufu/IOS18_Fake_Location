import ast

def parse_loc(content):
    coord = ast.literal_eval("[{}]".format(content))
    coord[0]["lat"] = float(coord[0]["lat"])
    coord[0]["lng"] = float(coord[0]["lng"])
    return coord
