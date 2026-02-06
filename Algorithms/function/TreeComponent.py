class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
        # Right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root

def print_tree(root):
    if not root:
        print("Empty Tree")
        return
        
    def get_height(node):
        return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
    height = get_height(root)
    # Use valid spacing to avoid overlap
    width = 2 ** (height + 1)
    
    lines = []
    
    def draw(node, level, pos, space):
        if not node:
            return
            
        line = lines[level] if level < len(lines) else [" "] * width
        if level >= len(lines):
            lines.append(line)
            
        val_str = str(node.val)
        # Center the value at pos
        start = max(0, pos - len(val_str) // 2)
        end = min(width, start + len(val_str))
        line[start:end] = list(val_str)
        
        if node.left:
            draw(node.left, level + 1, pos - space, space // 2)
        if node.right:
            draw(node.right, level + 1, pos + space, space // 2)
            
    # Initialize lines
    for _ in range(height):
        lines.append([" "] * width)
        
    # Start checking from center, initial space depends on height
    # space should be 2^(height-2) for level 0 to level 1 step
    initial_space = 2 ** (height - 2) if height > 1 else 1
    draw(root, 0, width // 2, initial_space)
    
    for line in lines:
        print("".join(line))
        
    # Also print level order traversal for copy-pasting
    print("\nLevel Order: ", end="")
    if not root:
        print("[]")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    print(result)