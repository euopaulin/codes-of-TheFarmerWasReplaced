for ciclo in range(1):
	def plant_cenoura():
		blocos = 12
		solo_arado = Grounds.Soil
		solo2= Grounds.Grassland
		plantas = [Entities.Bush, Entities.Carrot, Entities.Sunflower]
		
		def voltar():
			for _ in range(blocos):
				if get_pos_x() == 0:
					move(West)
				else:
					move(East)
					
				
		for y in range(12):
			for x in range(blocos):
				if can_harvest():
					harvest()
					if get_entity_type() == solo_arado:
						plant(plantas[1])
						move(East)
				elif get_ground_type() == solo_arado or solo2:
					plant(plantas[1])
					use_item(Items.Water)
				elif get_ground_type() == solo2:
					plant((plantas[1]) or (plantas[2]))
					use_item(Items.Water)
				move(East)
			voltar()
			move(South)
			
	plant_cenoura()
import main