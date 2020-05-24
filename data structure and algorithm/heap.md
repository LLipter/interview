# Heap and Heap Sort

A Heap is a special Tree-based data structure in which the tree is a **complete binary tree**. Generally, Heaps can be of two types:

 - **Max-Heap**: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
 - **Min-Heap**: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

# Insert / Heapify Algorithm

 1. Put the new elements at the end of the array(heap).
 2. Compare the value of this child node with its parent.
 3. If value of parent is less than child, then swap them. (maintain heap propertity)
 4. Repeat step 2 & 3 until Heap property holds.

![](https://www.tutorialspoint.com/data_structures_algorithms/images/max_heap_animation.gif)

Time complexity: $O(\log n)$

# Deletion Algorithm

1. Remove root node.
2. Move the last element of last level to root.
3. Compare the value of this node with its children.
4. If value of parent is less than child, then swap them.
5. Repeat step 3 & 4 until Heap property holds.

![](https://www.tutorialspoint.com/data_structures_algorithms/images/max_heap_deletion_animation.gif)

Time complexity: $O(\log n)$

# Heap Construction Algorithm

Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.

~~~
BUILD-HEAP(A) 
    heapsize := size(A); 
    for i := floor(heapsize/2) downto 1 
        do HEAPIFY(A, i); 
    end for 
END
~~~

Time complexity: $O(n)$

# HeapSort Algorithm

Heap Sort Algorithm for sorting in increasing order:

1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

Time Complexity: $O(n \log n)$.

# References

1. [Heap Data Structures](https://www.tutorialspoint.com/data_structures_algorithms/heap_data_structure.htm)
2. [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/)
3. [Time Complexity of building a heap](https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/)