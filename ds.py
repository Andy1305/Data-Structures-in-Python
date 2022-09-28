from __future__ import annotations
from typing import Any



class Node:
	def __init__(self, data: Any):
		self.__data: Any = data
		self.__next: Node = None
		
	def set_data(self, data: Any) -> None:
		self.__data = data
		
	def get_data(self) -> Any:
		return self.__data
		
	def set_next(self, node: Node):
		self.__next = node
		
	def next(self) -> Node:
		return self.__next
		
		
class LinkedList:
	def __init__(self, head: Node = None):
		self.__head = head
		self.__size = 0 if self.__head == None else 1

	def size(self) -> int:
		return self.__size
		
	def _set_size(self, size: int) -> None:
		self.__size = size
		
	def is_empty(self) -> bool:
		return self.size() == 0
		
	def print(self) -> None:
		crt = self.__head
		for i in range(self.size()):
			print(crt.get_data(), end = " ")
			crt = crt.next()
			
		#while crt is not None:
		#	print(crt.get_data(), end = " ")
		#	crt = crt.next()
		print()
		
	def _get_head(self) -> Node:
		return self.__head
		
	def _set_head(self, head: Node):
		self.__head = head
		
	def __iter__(self):
		self.__crt = self.__head
		return self
			
	def __next__(self):
		if self.__crt:
			aux = self.__crt
			self.__crt = self.__crt.next()
			return aux.get_data()
		raise StopIteration
	
	def add_node(self, pos: int, new_data: Any) -> None:
		if (new_data == None) or (pos < 0):
			return
	
		node = Node(new_data)
		if self.__head == None:
			self.__head = node
			self.__size = 1
			return
			
		if pos == 0:
			node.set_next(self.__head)
			self.__head = node
			self.__size += 1
			return
			
		crt_node = self.__head
		for crt_pos in range(self.size() - 1):
			if crt_pos == pos - 1:
				break
			crt_node = crt_node.next()
				
		if crt_node.next() != None:
			node.set_next(crt_node.next())	
		crt_node.set_next(node)
		self.__size += 1
			
	def remove_node(self, pos: int) -> None:
		if (self.__head == None) or (pos < 0):
			return

		if pos == 0:
			aux = self.__head
			self.__head = self.__head.next()
			self.__size -= 1
			aux.set_next(None)
			data = aux.get_data()
			del aux
			return data
			
		crt_node = self.__head
		last_node = None
		for crt_pos in range(self.size() - 1):
			if crt_pos == pos - 1:
				break
			last_node = crt_node
			crt_node = crt_node.next()
			
		if crt_node.next() is not None:
			aux = crt_node.next()
			crt_node.set_next(aux.next())
			aux.set_next(None)
			data = aux.get_data()
			del aux
		else:
			last_node.set_next(None)
			data = crt_node.get_data()
			del crt_node
		self.__size -= 1
		return data
		
	def get_node(self, pos) -> Any:
		if (self.__head == None) or (pos < 0):
			return
			
		crt_node = self.__head
		for crt_pos in range(self.size()):
			if crt_pos == pos:
				break
			crt_node = crt_node.next()
		if crt_node is not None:
			return crt_node.get_data()
		return None
		
		
	def free(self):
		crt = self.__head
		while crt is not None:
			aux = crt
			crt = crt.next()
			aux.set_next(None)
			del aux
		self.__head = None
		self.__size = 0
		

class DLLNode(Node):
	def __init__(self, data: Any):
		super().__init__(data)
		self.__prev: DLLNode = None
		
	def set_prev(self, node: DLLNode) -> None:
		self.__prev = node
		
	def prev(self) -> DLLNode:
		return self.__prev


class CircularDoublyLinkedList(LinkedList):
	def __init__(self, head: DLLNode = None):
		super().__init__(head)
		if self._get_head() is not None:
			self._get_head().prev(self._get_head())
			self._get_head().next(self._get_head())

	def get_node(self, pos: int) -> DLLNode:
		if self.is_empty() or pos < 0:
			return
		
		pos = pos % self.size()
		crt_node = self._get_head()
		for i in range(self.size()):
			if pos == i:
				return crt_node
			crt_node = crt_node.next()
			
	def add_node(self, pos: int, new_data: Any):
		if new_data is None or pos < 0:
			return
		
		node = DLLNode(new_data)
		if self._get_head() is None:
			node.set_prev(node)
			node.set_next(node)
			self._set_head(node)
			self._set_size(1)
			return
			
		crt_node = self._get_head()
		for i in range(self.size()):
			if pos == i:
				break
			crt_node = crt_node.next()
		
		node.set_next(crt_node)
		node.set_prev(crt_node.prev())
		node.prev().set_next(node)
		node.next().set_prev(node)
		self._set_size(self.size() + 1)
		
		if pos == 0:
			self._set_head(node)
	
	def	remove_node(self, pos: int) -> None:
		if (self._get_head() == None) or (pos < 0):
			return
			
		crt_node = self._get_head()
		for crt_pos in range(self.size() - 1):
			if crt_pos == pos:
				break
			crt_node = crt_node.next()
			
		if pos == 0:
			self._set_head(crt_node.next())	
	
		crt_node.prev().set_next(crt_node.next())
		crt_node.next().set_prev(crt_node.prev())
		crt_node.set_prev(None)
		crt_node.set_next(None)
		del crt_node
		self._set_size(self.size() - 1)
		
	def free(self):
		crt = self._get_head()
		while crt is not None:
			aux = crt
			crt = crt.next()
			aux.set_next(None)
			aux.set_prev(None)
			del aux
		self._set_head(None)
		self._set_size(0)
		
		
		
class Entry:
	def __init__(self, key: int, value: Any):
		self.__key = key
		self.__value = value
		
	def get_key(self) -> int:
		return self.__key
		
	def get_val(self) -> int:
		return self.__value
		
	def set_val(self, value: Any) -> None:
		self.__value = value
		
	def __str__(self):
		return f"({self.__key}, {self.__value})"

class HashMap:
	def __init__(self, max_size: int = 10):
		self.__max_size = max_size
		self.__buckets: [LinkedList] = [LinkedList() for _ in range(self.__max_size)]
		
	def __hash(self, key: Any) -> int:
		''' 
		This is just for ints and strings, but Python has the already built-in hash() function that
		calculates the hash of a built-in immutable type like int or string.
		For custom objects the __hash__ and __eq__ functions must be implemented.
		'''
		if isinstance(key, int):
			key = ((key >> 16) ^ key) * 0x45d9f3b
			key = ((key >> 16) ^ key) * 0x45d9f3b
			key = (key >> 16) ^ key
		#elif isinstance(key, str):
		#	puchar_a = (unsigned char*) a;
		#	hash_constant = 5381;
		#	while ((c = *puchar_a++))
		#		hash = ((hash << 5u) + hash) + c; /* hash * 33 + c */
		else:
			key = hash(key)
			
		return key % self.__max_size

	def has_key(self, key: Any) -> bool:
		idx = self.__hash(key)
		for entry in self.__buckets[idx]:
			if key == entry.get_key():
				return True
		return False
		
	def get(self, key: Any) -> Any:
		i = self.__hash(key)
		for entry in self.__buckets[i]:
			if key == entry.get_key():
				return entry.get_val()
		return None
		
	def put(self, key: Any, value: Any) -> None:
		i = self.__hash(key)
		for entry in self.__buckets[i]:
			if key == entry.get_key():
				entry.set_val(value)
				return
		self.__buckets[i].add_node(self.__buckets[i].size(), Entry(key, value))
		
	def remove(self, key: Any) -> None:
		i = self.__hash(key)
		for idx, entry in enumerate(self.__buckets[i]):
			if key == entry.get_key():
				self.__buckets[i].remove_node(idx)
				return
				
	def redim(self):
		"Resize the hashmap when it becomes too crowded, easy to do"
		pass
		
	def print(self) -> None:
		if hasattr(self, '_HashMap__buckets'):
			for i, bucket in enumerate(self.__buckets):
				print(f"{i}: ", end = '')
				bucket.print()
		else:
			print("HashMap is empty.")

	def free(self) -> None:
		# [delattr(attr) for attr in self.__dict__]
		for bucket in self.__buckets:
			bucket.free()
		del self.__buckets
		
		
class Stack:
	def __init__(self):
		self.__ll = LinkedList()
	
	def size(self) -> int:
		return self.__ll.size()
		
	def is_empty(self) -> bool:
		return self.__ll.is_empty()
	
	def push(self, val: Any) -> None:
		self.__ll.add_node(self.size(), val) 
		
	def pop(self) -> Any:
		return self.__ll.remove_node(self.size() - 1)
		
	def peek(self) -> Any:
		return self.__ll.get_node(self.size() - 1)
		
	def empty(self) -> None:
		self.__ll.free()
		
	def free(self) -> None:
		self.empty()
		del self.__ll
		
	def check_brackets(self, brackets: str):
		if len(brackets) % 2 != 0:
			print("Unbalanced brackets")
			return
		for b in brackets:
			if b in ['(', '[', '{']:
				self.push(b)
			elif b in [')', ']', '}']:
				if not self.is_empty():
					pop_b = self.pop()
					if not ((pop_b == '(' and b == ')') or (pop_b == '[' and b == ']') or (pop_b == '{' and b == '}')):
						print("Unbalanced brackets")
						return
				else:
					print("Unbalanced brackets")
					return
		print("Balanced brackets")
		
class Queue:
	def __init__(self, max_size = 10):
		self.__max_size = max_size
		self.__size = 0
		self.__head = self.__tail = -1 # they both should start from 0 and the tail should point after the last element
		self.__buff = [None for _ in range(max_size)]
	
	def size(self) -> int:
		return self.__size
		
	def is_empty(self) -> bool:
		return self.size() == 0
	
	def enqueue(self, val: Any) -> None:
		if self.size() == self.__max_size:
			#raise MemoryError("The queue is full!")
			print("The queue is full!")
			return
		if self.is_empty():
			self.__head = 0
		if not (self.__head == self.__tail and self.is_empty()):
			self.__tail = (self.__tail + 1) % self.__max_size
		self.__buff[self.__tail] = val
		self.__size += 1
		
	def dequeue(self) -> Any:
		if self.is_empty():
			return None
		head = self.__buff[self.__head]
		#self.__buff[self.__head] = None
		if self.size() > 1: # the queue has only one element, so no need to increment
			self.__head = (self.__head + 1) % self.__max_size
		self.__size -= 1
		return head
		
	def front(self) -> Any:
		return self.__buff[self.__head] if not self.is_empty() else None
		
	def print(self):
		print(self.__head, self.__tail, self.__buff)
		
	def empty(self) -> None:
		self.__head = self.__tail = -1
		
	def free(self) -> None:
		self.empty()
		del self.__buff
		
		
class LGraph:
	"List graph implementation"
	def __init__(self, nr_nodes: int = 10):
		self.__nr_nodes = nr_nodes
		self.__friends = [LinkedList() for _ in range(nr_nodes)]
		
	def add_edge(self, node1: int, node2: int) -> None:
		self.__friends[node1].add_node(self.__friends[node1].size(), node2)
		self.__friends[node2].add_node(self.__friends[node2].size(), node1)
		
	def remove_edge(self, node1: int, node2: int) -> None:
		for i, node in enumerate(self.__friends[node1]):
			if node == node2:
				self.__friends[node1].remove_node(i)
				break
		for i, node in enumerate(self.__friends[node2]):
			if node == node1:
				self.__friends[node2].remove_node(i)
				break
				
	def has_edge(self, node1: int, node2: int) -> None:
		for i, node in enumerate(self.__friends[node1]):
			if node == node2:
				self.__friends[node1].remove_node(i)
				return True
		return False
		
	def bfs(self, root: int):
		q = Queue()
		q.enqueue(root)
		visited = []
		while not q.is_empty():
			
			crt = q.dequeue()
			#q.print()
			#print(crt, end = ' ')
			for friend in self.__friends[crt]:
				if friend not in visited:
					q.enqueue(friend)
					visited.append(crt)
		print()
		
	def bfs_rec(self, root: int, visited: list):
		if root in visited:
			return
		visited.append(root)
		for friend in self.__friends[root]:
			if friend not in visited:
				print(friend)
				
		for friend in self.__friends[root]:
			if friend not in visited:
				self.bfs_rec(friend, visited)
		
	def print(self) -> None:
		for i, l in enumerate(self.__friends):
			print(f"{i}: ", end = '')
			l.print()
	
	def free(self) -> None:
		for l in self.__friends:
			l.free()
		del self.__friends
		
class MGraph:
	"Matrix graph implementation"
	def __init__(self, nr_nodes: int = 10):
		self.__nr_nodes = nr_nodes
		self.__friends = [[0] * nr_nodes for _ in range(nr_nodes)]
		
	def add_edge(self, node1: int, node2: int) -> None:
		self.__friends[node1][node2] = self.__friends[node2][node1] = 1
		
	def remove_edge(self, node1: int, node2: int) -> None:
		self.__friends[node1][node2] = self.__friends[node2][node1] = 0
				
	def has_edge(self, node1: int, node2: int) -> None:
		return self.__friends[node1][node2] == self.__friends[node2][node1] == 1
		
	def dfs(self, root: int) -> None:
		s = Stack()
		visited = []
		s.push(root)
		
		while not s.is_empty():
			has_friend = False # True if the node has any unvisited friends left
			crt_node = s.peek()
			if crt_node not in visited:
				print(crt_node)
				visited.append(crt_node)
			for friend, is_friend in enumerate(self.__friends[crt_node]):
				if is_friend == 1 and friend not in visited:
					s.push(friend)
					has_friend = True
					break
			if not has_friend:
				s.pop()
				
	def dfs_rec(self, root: int, visited: list) -> None:
		if root in visited:
			return
		
		print(root)
		visited.append(root)
		for friend, is_friend in enumerate(self.__friends[root]):
			if is_friend == 1:
				self.dfs_rec(friend, visited)
				
	def print(self) -> None:
		print("  ", list(range(self.__nr_nodes)))
		for i, l in enumerate(self.__friends):
			print(f"{i}: {l}")
	
	def free(self) -> None:
		del self.__friends


class TNode:
	def __init__(self, info: Any = None):
		self.__info = info
		self.__left: Tree = None
		self.__right: Tree = None
		
	def get_info(self) -> Any:
		return self.__info
	
	def set_info(self, info: Any) -> None:
		self.__info = info
		
	def left(self) -> TNode:
		return self.__left
		
	def set_left(self, node: TNode) -> None:
		self.__left = node
		
	def right(self) -> TNode:
		return self.__right
		
	def set_right(self, node: TNode) -> None:
		self.__right = node


class Tree:
	def __init__(self, root: TNode = None):
		self.__root = root
		
	def _get_root(self) -> TNode:
		return self.__root
		
	def _set_root(self, root: TNode) -> None:
		self.__root = root
		
	def insert(self, info: Any) -> None:
		if self.__root is None:
			self.__root = TNode(info)
			return
		
		new_node = TNode(info)
		q = Queue()
		q.enqueue(self.__root)
		
		while not q.is_empty():
			node = q.dequeue()
			
			if node.left() is None:
				node.set_left(new_node)
				return
			if node.right() is None:
				node.set_right(new_node)
				return
			q.enqueue(node.left())
			q.enqueue(node.right())
			
	def height(self) -> None:
		def height(node: TNode, level: int = 0) -> int:
			if node is None:
				return -1
			return 1 + max(height(node.left()), height(node.right()))
		print("Height:", height(self.__root))
		
	def print_level(self, level: int = 0) -> None:
		def print_level(node: TNode, crt_lvl: int) -> None:
			if node is None:
				return
			if crt_lvl == level:
				print(node.get_info(), end = ' ')
				return
			print_level(node.left(), crt_lvl + 1)
			print_level(node.right(), crt_lvl + 1)
		
		print(f"Level {level}:", end = ' ')	
		print_level(self.__root, 0)
		print()
		
	def level_leaves(self) -> None:
		def leaf_level(node: TNode) -> bool:
			if node.left() is not None and node.right() is not None:
				return leaf_level(node.left()) and leaf_level(node.right())
			if node.left() == node.right() == None:
				return True
			return False
		print("{}".format(("All the leaves are level.", "The leaves are not level.")[not leaf_level(self.__root)]))
		
	def lca(self, node1: int, node2: int) -> None:
		def lca(node: TNode) -> bool:
			if node is None:
				return False
			if node.get_info() == node1 or node.get_info() == node2:
				return True
			
			found1 = lca(node.left())
			found2 = lca(node.right())
			
			if found1 and found2 or (found1 or found2 and node1 == node2):
				print(f"LCA ({node1}, {node2}): {node.get_info()}")
				return False
			return found1 or found2
		lca(self.__root)
		
		
	def print(self, option = 1) -> None:
		def print_inorder(node) -> None:
			if not node:
				return
			print_inorder(node.left())
			print(node.get_info())
			print_inorder(node.right())
			
		def print_preorder(node) -> None:
			if not node:
				return
			print(node.get_info())
			print_preorder(node.left())
			print_preorder(node.right())
			
		def print_postorder(self, node) -> None:
			if not node:
				return
			print_postorder(node.left())
			print_postorder(node.right())
			print(node.get_info())
			
		if option == 1:
			print_inorder(self.__root)
		if option == 2:
			print_preorder(self.__root)
		if option == 3:
			print_postorder(self.__root)
		
	def free(self) -> None:
		def free_aux(node: TNode) -> None:
			if not node:
				return

			self.free_aux(node.left())
			self.free_aux(node.right())
			
			del node
		
		free(self.__root)
		del self.__root
		
class BST(Tree):
	def __init__(self, root: TNode = None):
		super().__init__(root)
		
	def get_min(self, node: TNode) -> int:
		while node.left():
			node = node.left()
		return node.get_info()
		
	def get_max(self, node: TNode) -> int:
		while node.right():
			node = node.right()
		return node.get_info()
		
	def insert(self, info: Any) -> None:
		if self._get_root() is None:
			super().insert(info)
			return
		parent = crt = self._get_root()
		while crt:
			parent = crt
			if info == crt.get_info(): # node already in
				return
			if info > crt.get_info():
				crt = crt.right()
			else:
				crt = crt.left()
		parent.set_left(TNode(info)) if parent.get_info() >= info else parent.set_right(TNode(info))
		
	def remove(self, info: Any) -> None:
		def remove(node: TNode) -> TNode:
			aux = None # the child of the current node
			if node is None:
				return None
			if node.get_info() > info:
				aux = remove(node.left())
				if node.left() is not None and node.left().get_info() == info:
					node.set_left(aux)
				return None
			if node.get_info() < info:
				aux = remove(node.right())
				if node.right() is not None and node.right().get_info() == info:
					node.set_right(aux)
				return None
			if node.get_info() == info:
				if node.left() is None:
					return node.right()
				if node.right() is None:
					return node.left()
				# it means the node has 2 children
				# replace with the closest value
				closest = self.get_max(node.left())
				self.remove(closest)
				node.set_info(closest)
				# remove the node aux was replaced with
			return None
		
		if self._get_root().get_info() == info:
			if self._get_root().left() == self._get_root().right() == None:
				self.free()
				return
			if self._get_root().left() is None:
				self._set_root(self._get_root().right())
			else:
				self._set_root(self._get_root().left())
			return
		remove(self._get_root())
		
class Heap:
	def __init__(self):
		self.__heap = []
		
	def parent(self, pos: int) -> Any:
		return (pos - 1) // 2
		
	def set_parent(self, pos: int, info: Any) -> None:
		self.__heap[self.get_parent(pos)] = info
		
	def left(self, pos: int) -> Any:
		return (2 * pos) + 1
		
	def set_left(self, pos: int, info: Any) -> None:
		self.__heap[self.left(pos)] = info
		
	def right(self, pos: int) -> Any:
		return (2 * pos) + 2
		
	def set_right(self, pos: int, info: Any) -> None:
		self.__heap[self.right(pos)] = info
		
	def top(self) -> Any:
		return self.__heap[0]
		
	def pop(self) -> Any:
		self.__heap[0] = self.__heap[-1]
		self.__heap.pop()

		crt = 0
		while crt < len(self.__heap):
			# get the smallest child
			smallest = None
			
			if self.left(crt) >= len(self.__heap) and self.right(crt) >= len(self.__heap):
				return
			elif self.left(crt) >= len(self.__heap):
				smallest = self.right(crt)
			elif self.right(crt) >= len(self.__heap):
				smallest = self.left(crt)
			elif self.__heap[self.left(crt)] <= self.__heap[self.right(crt)]:
				smallest = self.left(crt)
			else:
				smallest = self.right(crt)
			if self.__heap[crt] > self.__heap[smallest]:
				self.__heap[crt], self.__heap[smallest] = self.__heap[smallest], self.__heap[crt]
				crt = smallest
			else:
				break
		
	def insert(self, info: Any) -> None:
		self.__heap.append(info)
		if len(self.__heap) == 1:
			return
		crt = len(self.__heap) - 1
		while crt > 0 and self.__heap[crt] < self.__heap[self.parent(crt)]:
			self.__heap[crt], self.__heap[self.parent(crt)] = self.__heap[self.parent(crt)], self.__heap[crt]
			crt = self.parent(crt)

	def print(self) -> None:
		print(self.__heap)
		

class TreapNode(TNode):
	from random import randint
	def __init__(self, info: Any = None):
		super().__init__(info)
		self.__priority = self.randint(0, 100)
		#print(self.__priority)
		
	def priority(self) -> int:
		return self.__priority
		
	def rotate_right(self) -> None:
		if self.left() is None:
			print("Error: left node is NULL")
			return
		
		# interchange the info (current node with its left node)
		tmp = self.get_info()
		self.set_info(self.left().get_info())
		self.left().set_info(tmp)
		
		# left subtree
		left = self.left() # save the left child
		self.set_left(self.left().left())
		
		# right subtree
		left.set_left(left.right()) # move the right node into left
		left.set_right(self.right())      # set the right node to be the right node of the original node (self)
		self.set_right(left)			# set the right node to the new one (former left)
		
	def rotate_left(self) -> None:
		if self.right() is None:
			print("Error: left node is NULL")
			return
		
		# interchange the info (current node with its right node)
		tmp = self.get_info()
		self.set_info(self.right().get_info())
		self.right().set_info(tmp)
		
		# left subtree
		right = self.right() # save the right child
		self.set_right(self.right().right())
		
		# right subtree
		right.set_right(right.left()) # move the left node into right
		right.set_left(self.left())      # set the right node to be the left node of the original node (self)
		self.set_left(right)			# set the left node to the new one (former right)
		
class Treap(BST):
	def __init__(self, root: TreapNode = None):
		super().__init__(root)
		
	def insert(self, info: Any) -> None:
		def insert(node: TreapNode) -> TreapNode:
			if node is None:
				return TreapNode(info)

			if node.get_info() == info:
				return None
			if node.get_info() > info:
				new_node = insert(node.left())
				if node.left() is None:
					node.set_left(new_node)
				# rotate to keep priority
				if node.priority() < new_node.priority():
					node.rotate_right()
					return node
			else: # less than
				new_node = insert(node.right())
				if new_node is None:
					return None
				if node.right() is None:
					node.set_right(new_node)
				if node.priority() < new_node.priority():
					node.rotate_left()
					return node
			return None
		
		if self._get_root() is not None:
			insert(self._get_root())
		else:
			self._set_root(TrieNode(info))
		
	def remove(self, info: Any) -> None:
		def remove(node: TreapNode, parent: TreapNode) -> TreapNode:
			if node is None:
				return
				
			if node.get_info() > info:
				remove(node.left(), node)
			elif node.get_info() < info:
				remove(node.right(), node)
			elif node.left() is None and node.right() is None:
				# del node
				if parent.left() is not None and parent.left().get_info() == node.get_info():
					parent.set_left(None)
					return
				if parent.right() is not None and parent.right().get_info() == node.get_info():
					parent.set_right(None)
					return
			elif node.left() is not None:
				node.rotate_right()
				remove(node.right(), node)
			elif node.right() is not None:
				node.rotate_left()
				remove(node.left(), node)
			elif node.left().priority() > node.right().priority():
				node.rotate_right()
				remove(node.right(), node)
			else:
				node.rotate_left()
				remove(node.left(), node)
		
		remove(self._get_root(), None)
		

class TrieNode:
	def __init__(self, info: Any = None):
		self.__info = info
		self.__kids = [None] * 26
		
	def info(self) -> Any:
		return self.__info
		
	def set_info(self, info: Any) -> None:
		self.__info = info
		
	def kid(self, pos: str = 'a') -> Any:
		pos = ord(pos) - ord('a')
		return self.__kids[pos]
		
	def kids(self) -> [TrieNode]:
		return self.__kids
		
	def set_kid(self, pos: str = 'a', delete: bool = False) -> None:
		pos = ord(pos) - ord('a')
		if delete:
			self.__kids[pos] = None
		else:	
			self.__kids[pos] = TrieNode()
		
	def has_kids(self):
		return len([filter(lambda x: x is not None, self.__kids)]) != 0
		

class Trie:
	def __init__(self):
		self.__root = TrieNode('')
		
	def insert(self, key: str, info: Any):
		def insert(key: str, node: TrieNode):
			if key == "":
				node.set_info(info)
				return
			next_node = node.kid(key[0])
			if next_node is None:
				node.set_kid(key[0])
			insert(key[1:], node.kid(key[0]))
		insert(key, self.__root)
		
	def search(self, key: str) -> Any:
		def search(key: str, node: TrieNode) -> Any:
			if node is None:
				return
			if key == "":
				return print(node.info())
			search(key[1:], node.kid(key[0]))
		search(key, self.__root)
			
	def remove(self, key: str):
		def remove(key: str, node: TrieNode) -> None:
			if node is None:
				return True
			if key == "":
				if node.info() is not None:
					# we've reached the end of the word (key)
					node.set_info(None)
					return not node.has_kids() # can't delete if still has kids
				return False # the key exists but it contains no value, which means it's just a prefix for another key
			
			if remove(key[1:], node.kid(key[0])):
				# the kid can be deleted
				node.set_kid(key[0], True)
				
				# check if the current node has any other kids left or is the end of another key
				if (not node.has_kids()) and (node.info() is None):
					return True
				
			return False
			
				
		remove(key, self.__root)
			
	def print(self) -> None:
		def print_aux(node: TrieNode, key: list = '') -> None:
			for i, kid in enumerate(node.kids()):
				if kid is not None:
					print_aux(kid, key + chr(ord('a') + i))
			if node.info() is not None and node.info() != "":
				print(f"{key}: {node.info()}")	
		print_aux(self.__root)
			
	def free(self) -> None:
		def free(node: TrieNode) -> None:
			for i, kid in enumerate(self.kids()):
				if kid is not None:
					free(kid)
					node.set_kid(chr(ord('a') + i), True)
		free(self.__root)
		self.__root = None
		
class Labs:
	def __init__(self):
		#self.lab2()
		#self.lab3()
		#self.lab4()
		#self.lab5()
		#self.lab6()
		#self.lab8()
		#self.lab9()
		#self.lab10()
		self.lab11()
		
	def lab2(self) -> None:
		ll = LinkedList()
		ll.add_node(3, 10)
		ll.add_node(1, 11)
		ll.add_node(2, 12)
		ll.add_node(3, 13)
		ll.add_node(0, 8)
		ll.add_node(1, 7)
		ll.add_node(23, 100)
		ll.print()
		
		ll.remove_node(0)
		ll.remove_node(1)
		ll.remove_node(53)
		ll.print()
		
		ll.free()
		ll.print()
		
	def lab3(self) -> None:
		dll = CircularDoublyLinkedList()
		dll.add_node(0, 1)
		dll.add_node(1, 2)
		dll.add_node(2, 3)
		dll.add_node(3, 4)
		dll.add_node(4, 23)
		dll.print()
		print(dll.get_node(101).get_data())
		dll.remove_node(0)
		dll.remove_node(1)
		dll.remove_node(100)
		dll.print()
		dll.free()
		dll.print()
		
	def lab4(self) -> None:
		hm = HashMap()
		hm.put(123, 'a')
		hm.put(3, 'b')
		hm.put(3, 'c')
		hm.put('545', 'd')
		hm.put('asa', 'e')
		hm.put('fgfd', 'f')
		hm.print()
		print(hm.has_key(123), hm.has_key('asd'), hm.has_key('545'))
		print(hm.get(123), hm.get('asa'), hm.get(77)) 
		hm.remove(123)
		hm.remove('545')
		hm.print()
		hm.free()
		hm.print()
		
	def lab5(self) -> None:
		print("Stack:")
		s = Stack()
		print(s.is_empty())
		s.push(1), s.push(2), s.push(3), s.push(4)
		print(s.size())
		print(s.pop())
		print(s.pop())
		print(s.peek())
		s.empty()
		print(s.size())
		s.push(1)
		print(s.peek())
		s.free()
		#print(s.peek())
		print("\n\nQueue:")
		q = Queue(4)
		print(q.is_empty())
		q.enqueue(1), q.enqueue(2), q.enqueue(3), q.enqueue(4)
		print(q.size())
		print(q.dequeue())
		print(q.dequeue())
		print(q.front())
		#q.empty()
		print(q.size())
		q.enqueue(13)
		q.enqueue(13)
		print(q.size())
		print(q.front())
		print(q.dequeue())
		print(q.dequeue())
		print(q.front())
		q.free()
		print("\n\nBrackets:")
		ss = Stack()
		ss.check_brackets("(()")
		
	def lab6(self):
		g = LGraph()
		g.add_edge(0, 1), g.add_edge(0, 2)
		g.add_edge(1, 3), g.add_edge(1, 4)
		g.add_edge(2, 5), g.add_edge(2, 6)
		g.bfs(0)
		g.bfs_rec(0, [])
		g.print()
		print(g.has_edge(0, 1))
		g.remove_edge(0, 1)
		print(g.has_edge(0, 1))
		g.print()
		
		g = MGraph()
		g.add_edge(0, 1), g.add_edge(0, 2)
		g.add_edge(1, 3), g.add_edge(1, 4)
		g.add_edge(2, 5), g.add_edge(2, 6)
		g.print()
		print(g.has_edge(0, 1))
		g.dfs(0)
		g.dfs_rec(0, [])
		g.remove_edge(0, 1)
		print(g.has_edge(0, 1))
		g.print()
		
	def lab8(self):
		t = Tree()
		t.insert(1)
		t.insert(2)
		t.insert(3)
		t.insert(4)
		t.insert(5)
		t.insert(6)
		t.insert(7)
		t.insert(8)
		t.print()
		t.height()
		t.print_level(3)
		t.level_leaves()
		t.lca(4, 4)
	
	def lab9(self):
		t = BST()
		t.insert(1)
		t.insert(5)
		t.insert(3)
		t.insert(4)
		t.insert(2)
		t.insert(6)
		t.insert(8)
		t.insert(7)
		#t.print()
		t.remove(3)
		#t.print()
		
		h = Heap()
		h.insert(1)
		h.insert(2)
		h.insert(3)
		h.insert(0)
		h.pop()
		h.print()
		
	def lab10(self):
		t = Treap()
		t.insert(7)
		t.insert(5)
		t.insert(9)
		#t.print()
		t.remove(7)
		t.print()
		
	def lab11(self):
		t = Trie()
		t.insert("key", 3)
		t.insert("keys", 4)
		t.insert("abc", 22)
		t.insert("abcxyz", 43)
		t.insert("abczyx", 55)
		t.print()
		t.search("abcxyz")
		t.remove("abcxyz")
		t.print()
		t.free()

def main():
	Labs()
	
main()
