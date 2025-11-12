from chapeu import chapeu
for ciclo in range(1):
	def grama():
		blocos = 12
		solo_arado = Grounds.Soil
		solo2 = Grounds.Grassland
		plantas = [Entities.Bush, Entities.Carrot, Entities.Sunflower, Entities.Pumpkin]

		def voltar():
			for _ in range(blocos):
				if get_pos_x() == 5:
					move(West)
				else:
					move(East)

		for y in range(12):
			for x in range(blocos):
				if can_harvest():
					harvest()
					for p in plantas:
						if get_entity_type() == solo_arado:
							plant(plantas[3])
							move(East)
						else:
							till()
							plant(plantas[3])
				elif get_ground_type() == solo_arado or solo2:
					plant(plantas[3])

				move(East)
			voltar()
			move(South)

grama()