from arvore import BinaryTree
from gerador import generate_random_list

treee = BinaryTree()

listCode = generate_random_list(120)
print(listCode)

for i in listCode:
    treee.insert(i)


print("Preorder:")
treee.print_preorder()

print("Inorder:")
treee.print_inorder()

print("Postorder:")
treee.print_postorder()
