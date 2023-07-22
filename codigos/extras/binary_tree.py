class BinaryTree:
    def __init__(self, deep, default_value = None):
        self._deep = deep
        self._tree = self._create_tree(deep, default_value)
        self._current_node = 0
    
    def _create_tree(self, deep, default_value):
        if deep <= 0:
            return []
        size = 2 ** deep - 1
        tree = [default_value] * size
        return tree

    def _index_left_child(self, index):
        return 2 * index + 1

    def _index_right_child(self, index):
        return 2 * index + 2

    def _index_father(self, index):
        return (index - 1) // 2

    def reset(self):
        self._current_node = 0

    def go_left(self):
        left_child = self._index_left_child(self._current_node)
        if left_child < len(self._tree):
            self._current_node = left_child

    def go_right(self):
        right_child = self._index_right_child(self._current_node)
        if right_child < len(self._tree):
            self._current_node = right_child

    def go_parent(self):
        if self._current_node > 0:
            self._current_node = self._index_father(self._current_node)

    def go_root(self):
        self._current_node = 0

    def set_value(self, value):
        self._tree[self._current_node] = value
    
    def get_value(self):
        return self._tree[self._current_node]
    
    def get_node_index(self):
        return self._current_node
    
    def is_node_leaf(self):
        index_left = self._index_left_child(self._current_node)
        index_right = self._index_right_child(self._current_node)

        return index_left >= len(self._tree) and index_right >= len(self._tree)

    def __str__(self):
        return str(self._tree)
        
# Example
tree = BinaryTree(3, 0)
tree.go_left()
tree.set_value(2)
tree.go_root()
tree.go_right()
tree.set_value(3)
tree.go_root()
print(tree)