#Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:
#a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
##b. determinar si un número está cargado en el árbol o no;
#c. eliminar tres valores del árbol;
#d. determinar la altura del subárbol izquierdo y del subárbol derecho;
#e. determinar la cantidad de ocurrencias de un elemento en el árbol;
#f. contar cuántos números pares e impares hay en el árbol.

import random
from tree import BinaryTree 

#creo y cargo el arbol binario
tree = BinaryTree()
for _ in range(1000):
    num = random.randint(1, 100)
    tree.insert(num)

#a. Realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;

print("Preorden:")
tree.pre_order()
print("\nInorden:")
tree.in_order()
print("\nPostorden:")
tree.post_order()
print("\nPor nivel:")
tree.by_level()

#b. Determinar si un número está cargado en el árbol o no;

number_to_search = int(input("\nIngrese un número para buscar en el árbol: "))

def search_number(root, number):
    if root is None: 
        return False
    if root.value == number:
        return True
    elif number < root.value:
        return search_number(root.left, number)
    else:
        return search_number(root.right, number)
    
print(f"El número {number_to_search} {'está' if search_number(tree.root, number_to_search) else 'no está'} en el árbol.")

#c. Eliminar tres valores del árbol;
for val in [number_to_search, random.randint(1, 100), random.randint(1, 100)]:
    deleted_value, other_values = tree.delete(val)
    if deleted_value is not None:
        print(f"El valor {deleted_value} ha sido eliminado del árbol.")
    else:
        print(f"El valor {val} no se encontró en el árbol para eliminar.")
print("\nÁrbol después de las eliminaciones (Inorden):")
tree.in_order()

#d. Determinar la altura del subárbol izquierdo y del subárbol derecho;

def height(node):
    if node is None:
        return -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1
left_subtree_height = height(tree.root.left)
right_subtree_height = height(tree.root.right)
print(f"\nAltura del subárbol izquierdo: {left_subtree_height}")
print(f"Altura del subárbol derecho: {right_subtree_height}")

#e. Determinar la cantidad de ocurrencias de un elemento en el árbol;
#cada vez que se inserta un valor ya existente, se incrementa un contador en ese nodo.

def insert(self, value, other_values=None): #inserta un nuevo valor en el árbol. Si el valor ya existe, incrementa un contador en ese nodo.
    def __insert(root, value, other_values):
        if root is None:
            return BinaryTree.__nodeTree(value, {"count": 1})
        elif value == root.value:
            root.other_values["count"] += 1
        elif value < root.value:
            root.left = __insert(root.left, value, other_values)
        else:
            root.right = __insert(root.right, value, other_values)

        root = self.auto_balance(root)
        self.update_hight(root)
        return root

    self.root = __insert(self.root, value, other_values)

def count_occurrences(root, number):  #contar las ocurrencias de un número en el árbol.
    if root is None:
        return 0
    if root.value == number:
        return root.other_values.get("count", 1)
    elif number < root.value:
        return count_occurrences(root.left, number)
    else:
        return count_occurrences(root.right, number)

occurrences = count_occurrences(tree.root, number_to_search)
print(f"\nEl número {number_to_search} aparece {occurrences} veces en el árbol.")

#F. Contar cuántos números pares e impares hay en el árbol.

def count_even_odd(root):
    if root is None:
        return (0, 0)
    left_even, left_odd = count_even_odd(root.left)
    right_even, right_odd = count_even_odd(root.right)
    if root.value % 2 == 0:
        return (left_even + right_even + 1, left_odd + right_odd)
    else:
        return (left_even + right_even, left_odd + right_odd + 1)
even_count, odd_count = count_even_odd(tree.root)
print(f"\nCantidad de números pares en el árbol: {even_count}")
print(f"Cantidad de números impares en el árbol: {odd_count}")
