from chapeu import chapeu
def plantar_colheita():
	blocos = 15
	madeira = Entities.Bush
	solo_arado = Grounds.Soil
	arvore = Entities.Tree
	solo2 = Grounds.Grassland
	abobora = Entities.Dead_Pumpkin
	
	def voltar():
			move(East)
			
	for y in range(15):
		for x in range(blocos):
			if can_harvest():
				harvest()
				till()
				plant(abobora)
				if get_ground_type() == solo2:
					plant(abobora)
				elif get_ground_type() == solo_arado:
					till()
					till()
					till()
					plant(abobora)
				else:
					pass
			elif get_ground_type() == solo_arado or solo2:
				till()
				plant(arvore)
			else:
				pass

			move(East)
		voltar()
		move(South)

plantar_colheita()