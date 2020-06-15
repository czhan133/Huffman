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

	while (len(a) != 0):

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

	return arr;

def print_tree(a):
	for i in range(len(a)):
		print("  "),
		print(a[i].root.char)
		print(" /  \ ")
		print(a[i].root.left.char),
		print("  "),
		print(a[i].root.right.char)	

array = read_file();
sort_array(array);
print_array(array);
arr = create_tree(array);
print_tree(arr);
