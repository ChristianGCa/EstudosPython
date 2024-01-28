from sklearn import tree

x = [[140, 1], [130, 1], [150, 0], [170, 0]]
y = [1, 1, 0, 0]

# Instanciando uma árvore para classificação
clf = tree.DecisionTreeClassifier()

# Treinando o algoritmo
clf = clf.fit(x, y)

# Pedindo para classificar qual é essa fruta
print(clf.predict([[125, 0]]))