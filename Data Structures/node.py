

class Node:

    def __init__(self, value):
            self.right_child = None
            self.left_child = None
            self.data = value

    def binary_insert(self, node):
        # checks if there is a root
        if self.data:
            if self.data > node.data:
                # if there is a rot then checks if the node of the root is greater than that of node
                if self.left_child is None:
                    # If there is no left child then this node becomes left child
                    self.left_child = node
                    # print("Here is the new left child of Node({})".format(self.data), self.left_child.data)
                else:
                    # otherwise checks if there is a left child of the next node
                    self.left_child.binary_insert(node)
            elif self.data <node.data:
                # If the node of the root is not greater than that of the node
                if self.right_child is None:
                    # If there is no right child the node becomes right child
                    self.right_child = node
                    # print("Here is the new right child of Node({})".format(self.data), self.right_child)
                else:
                    # If there is a right child runs the function again to determine right child of next node
                    # print("This is the current right_child of Node({})".format(self.right_child.data),"And this is the new node Node({}) ".format(node))
                    self.right_child.binary_insert(node)

    def __str__(self):
        return "Node({}, {}, {})".format(self.left_child, self.data, self.right_child)

    @staticmethod
    def is_node(node):
        assert isinstance(node, Node) or node is None, "Must be type Node, instead has type {}".format(type(node))

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.data),
        if self.right_child:
            self.right_child.print_tree()
    @staticmethod
    def bfs(root):
        # checks if the given input is on the tree
        if root is None:
            return []
        # create an empty queue
        queue = []
        # add the root to the list
        queue.append(root)

        while len(queue)>0:
            # prints the first item of the list and removes it
            print(queue[0].data)
            node = queue.pop(0)
            # if a left child exists then it adds the left child of the node to the queue
            if node.left_child is not None:
                queue.append(node.left_child)
            # if a right child exists then it adds the right child of the node to the queue
            if node.right_child is not None:
                queue.append(node.right_child)


