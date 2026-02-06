import sys
import os

# Use realpath to resolve symlinks, ensuring we get the canonical path of this file.
# Since this file lives in Algorithms/env.py, we need to go up 1 level to reach the project root.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')))


