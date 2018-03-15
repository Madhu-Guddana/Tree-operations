
class Node(object):
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

def top_bottom_view(root):
    if not root: return []

    dict = {}
    dict[0] = root
    Q = [(root, 0)]
    ["abc"].pop()
    while Q:
        item = Q.pop()
        hlength = item[1]
        item = item[0]

        if item.left:
            Q.insert(0,(item.left, hlength -1))
            # For Top view, following codition is required, for bottom view, it need to be commented.
            #if hlength-1 not in dict:
            dict[hlength -1] = item.left
        if item.right:
            Q.insert(0,(item.right, hlength +1))
            #if hlength+1 not in dict:
            dict[hlength +1] = item.right
    keys = dict.keys()
    keys.sort(reverse=False)

    print " ".join([str(dict[key].data) for key in keys])

def print_level_order(root):
    Q = []
    if not root: return
    Q.insert(0,root)
    while Q:
        item = Q.pop()
        print item.data
        if item.left:
            Q.insert(0, item.left)
        if item.right:
            Q.insert(0, item.right)

def print_spiral_level_order(root):
    if not root:
        return
    # Following are stacks not Queues.
    Q1 = []
    Q2 = []
    Q1.append(root)

    while Q1 or Q2:
        while Q1:
                item = Q1.pop()
                print item.data
                if item.right: Q2.append(item.right)
                if item.left: Q2.append( item.left)
        while Q2:
                item = Q2.pop()
                print item.data
                if item.left: Q1.append(item.left)
                if item.right: Q1.append(item.right)

def print_boarder(root):
    def print_left(root):
        while(root):
            if root.left:
                print root.data
                root = root.left
            elif root.right:
                print root.data
                root = root.right
            else:
                root = None

    def print_right(root):
        if not root or not root.right:
            return
        root = root.right
        stack = []
        while(root):
            if root.right:
                stack.append(str(root.data))
                root = root.right
            elif root.left:
                stack.append(str(root.data))
                root = root.left
            else:
                root = None
        print " ".join(stack)

    def print_bottom(root):
        if not root:
            return
        if not root.left and not root.right:
            print root.data
        print_bottom(root.left)
        print_bottom(root.right)

    print_left(root)
    print_bottom(root)
    print_right(root)

def decodeHuff(root , s):
   output = []
   temp = root
   for i in s:
       if not (temp.left or temp.right):
           output.append(temp.data)
           temp = root
       if i == 0:
           temp = temp.left
       else:
           temp = temp.right
   print " ".join(temp)
   
def printTree(root):
    buf = []
    output = []
    if not root:
        print '$'
    else:
        buf.append(root)
        count = 1
        nextCount = 0
        while count > 0:
            node = buf.pop(0)
            if node:
                output.append(node.data)
                count -= 1
            else:
                output.append('$')
            if node and node.left:
                buf.append(node.left)
                nextCount += 1
            else:
                buf.append(None)
            if node and node.right:
                buf.append(node.right)
                nextCount += 1
            else:
                buf.append(None)
            if count == 0:
                print output
                output = []
                count = nextCount
                nextCount = 0
        # print the remaining all empty leaf node part
        for i in range(len(buf)):
            output.append('$')
        print output


def swap_node(root, k, level=1):
    if not root:
        return
    if (level+1) % k == 0:
        root.left, root.right = root.right, root.left
    swap_node(root.left, k, level+1)
    swap_node(root.right, k, level+1)

""" Create following Binary Tree
         1
       /  \
      2    3
       \
        4
         \
          5
           \
            6*/
"""

def is_bst(root, min_allowed, max_allowed):
    if not root:
        return True
    if not min_allowed < root.data < max_allowed:
        return False
    return is_bst(root.left, min_allowed, root.data) and \
           is_bst(root.right, root.data, max_allowed)

def LCA(root, key1, key2):
    def find_path(root, key, path):
        if root:
            path.append(root)
            if root.data == key:
                return True
            if find_path(root.left, key, path):
                return True
            if find_path(root.right, key, path):
                return True
            path.pop()
        return False
    path1 = []
    path2 = []
    if not find_path(root, key1,path1) or  not find_path(root, key2, path2):
        print path1
        print path2
        return False

    i = 0
    length = min(len(path1), len(path2))
    while i <length :
        if path1[i]!= path2[i]:
            break
        i +=1
    print path1[i - 1].data

def print_diagonal(root):
    queue = []
    temp = root
    while(temp):
        queue.append(temp)
        temp = temp.right

    while (queue):
        item = queue.pop(0)
        if item.left:
            queue.append(item.left)
            if item.left.right:
                queue.append(item.left.right)
        print item.data

def vertical_height(root):
    dict = {}
    def fill_dict(root, distance):
        if not root:
            return
        if distance in dict:
            dict[distance].append(root.data)
        else: dict[distance] = [root.data]
        fill_dict(root.left, distance-1)
        fill_dict(root.right, distance+1)
    fill_dict(root, 0)
    keys = sorted(dict.keys())
    for key in keys:
        print dict[key]

def level_order(root):
    if not root: return
    print root.data
    LQ, RQ = [root.left],[root.right]
    LtoR = True
    while LQ or RQ:
        Q = LQ if LtoR else RQ
        item = Q.pop(0)
        if not item: return
        print item.data
        Q += [item.left, item.right] if LtoR else [item.right, item.left]
        LtoR = not LtoR
def expression_tree(root):
    if not root:
        return
    if not root.left or root.right:
        return  root.data

    return eval("%s %s %s" % (root.left, root.data, root.right))

root=Node(1);
root.left=Node(2);
root.right=Node(3);
root.left.left=Node(4);
root.left.right=Node(5);
root.right.left=Node(6);
root.right.right=Node(7);
printTree(root)


