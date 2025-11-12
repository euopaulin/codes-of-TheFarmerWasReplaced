from chapeu import chapeu
def plantar_colheita():
	blocos = 11
	madeira = Entities.Bush
	solo_arado = Grounds.Soil
	arvore = Entities.Tree
	solo2 = Grounds.Grassland
	
	def voltar():
		for _ in range(blocos):
			move(East)
			
	for y in range(11):
		for x in range(blocos):
			if can_harvest():
				harvest()
				till()
				plant(Entities.Dead_Pumpkin)
			elif get_ground_type() == solo_arado or solo2:
				till()
				plant(arvore)
			else:
				pass

			move(East)
		voltar()
		move(South)

plantar_colheita()