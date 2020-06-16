class FreqNode:
	def __init__(self, c, f):
		self.char = c;
		self.freq = f;
		self.left = None;
		self.right = None;
		self.parent = None;
		self.sibling = None;		

class Tree:
	def __init__(self, root):
		self.root = FreqNode('~', root); #root is going to be the root freq

def read_file():
	ifile = open('huff.txt', 'r');
	
	dic = {};
	arr = [];

	while(1):
		c = ifile.read(1);
		
		if not c:
			break;
		
		if (dic.get(c)):
			dic[c] += 1;
		else:
			if (c == '\n'):
				dic['/'] = 1;
			else:
				dic[c] = 1;

	ifile.close();

	for key in dic:
		entry = FreqNode(key, dic[key]);
		arr.append(entry);

	return arr;		
	
def sort_array(a):
	i = 0;
	while (i < len(a)):
		j = i + 1;
		while (j < len(a)):
			if (a[j].freq < a[i].freq):
				temp = a[i];	
				a[i] = a[j];
				a[j] = temp;
			j += 1;
		i += 1;
	
	return a;

def print_array(a):
	for i in range(len(a)):
		print(a[i].char),
		print(" "),
		print(a[i].freq)

def create_tree(a):
	arr = [];

	while (len(a) != 1):

		left = a.pop(0);
		right = a.pop(0);

		left.sibling = right;
		right.sibling = left;
	
		TreeRoot = Tree(right.freq + left.freq);
		TreeRoot.root.left = left;
		TreeRoot.root.right = right;
	
		left.parent = TreeRoot.root;
		right.parent = TreeRoot.root;

		arr.append(TreeRoot);

		a.append(TreeRoot.root);
		a = sort_array(a);
	return arr;		

def print_tree(root, code_arr, top):

	if (root.left):
		code_arr[top] = 0;
		print_tree(root.left, code_arr, top + 1);

	if (root.right):
		code_arr[top] = 1;
               	print_tree(root.right, code_arr, top + 1);

	if (not root.right and not root.left):
		print(root.char), 
		print(": "),
		print_arr(code_arr, top);
		
def print_arr(arr, size):
	for i in range(size):
		print(arr[i]),
	print("\n");

array = read_file();
sort_array(array);
print_array(array);
rt_arr = create_tree(array);
tr_root = rt_arr[len(rt_arr) - 1];
code_array = [None]*100;
print_tree(tr_root.root, code_array, 0);
