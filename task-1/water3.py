def initial_state():
    return (8, 0, 0)


def is_goal(s):
    if s == (4,4,0): return True
    else: return False


def successors(s):
    x, y, z = s
    suc_list = []
    if x != 0:
        if y != 5:
            suc_list.append([(x-(5-y), 5, z), 5-y])
        if z != 3:
            suc_list.append([(x-(3-z),y,3), 3-z])
    if y != 0:
        suc_list.append([(x+y, 0, z),y])
        if (3-z) > y:
            suc_list.append([(x,0,z+y),y])
        if (3-z) <= y:
            suc_list.append([(x,y-(3-z),3),3-z])
    if z >= (5-y):
        suc_list.append([(x,5,z-(5-y)), (5-y)])
    suc_list.append([(x+z,y,0),z])
    return suc_list
