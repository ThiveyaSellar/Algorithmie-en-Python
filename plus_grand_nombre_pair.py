def plus_grand_nombre_pair(liste):
	maximum = None
	for nombre in liste:
		if nombre % 2 == 0 :
			if maximum is None or nombre > maximum:
				maximum = nombre
	print(maximum)

ma_liste = [1, 5, 8, 3, 10, 7]
plus_grand_nombre_pair(ma_liste)
ma_liste = [1, 3, 5, 7]
plus_grand_nombre_pair(ma_liste)

