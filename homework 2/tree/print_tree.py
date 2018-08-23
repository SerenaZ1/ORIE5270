import math


class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        """
        Get the value of the root node of a tree

        :return: (int)
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_height(self, root):
        """
        Get the height of the tree

        :param root: Node
        :return: (int)
        """
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def printTree(self, height):
        """
        print a tree, use '|' as separate sign

        :param height: (int)
        :return: list(height x (2 ** height - 1))
        """
        if self.root is None:
            return
        out_list = []
        queue = []
        queue.append(self.root)
        rs = []
        n = 2 << int(height - 1)
        sp_num = n / 2 - 1
        num = 1
        while num:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                num += 1
            else:
                queue.append(Node('|', None, None))
            if node.right is not None:
                queue.append(node.right)
                num += 1
            else:
                queue.append(Node('|', None, None))
            if node.value != '|':
                num -= 1
            rs.append(node)
        out = ''
        j = 0
        k = 1

        while rs:
            node = rs[0]
            rs = rs[1:]
            thres = math.log(k, 2)

            if j == thres:
                if j != 0:
                    # out += '\n'
                    out_list.append(out)
                sp = '|' * sp_num
                out = sp + str(node.value) + sp
                j += 1
                sp_num = (sp_num + 1) / 2 - 1
            else:
                out += '|' + sp + str(node.value) + sp

            k += 1
        add_slush_num = 2 ** height - 1 - len(out)
        out += '|'*add_slush_num
        out_list.append(out)
        for out in out_list:
            print out
        return [list(l) for l in out_list]


class Node(object):
    def __init__(self, value, left, right):
        """
        Node for a tree,

        ;param value: (float)
        ;param left: (Node)
        ;param right: (Node)
        """
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        """
        Get node value

        :return: (int)
        """
        return self.value
