def move_n_dir():
	while True:
		plata_atual = get_entity_type()
		grama = Entities.Grass
		madeira = Entities.Bush
		madeira2 = Entities.Tree
		girassol = Entities.Sunflower
		passos = 6
		for i in range(6):
			#Se o solo estiver com grama ou madeira o drone irá pegar
			#e preparar o solo para plantar girassol
			if (plata_atual == grama or madeira2)and(can_harvest()):
				harvest()
				till()
				plant(madeira2)
				move(North)
				if get_entity_type() == Grounds.Grassland:
					plant(madeira2)
					move(North)
				elif can_harvest()==madeira2:
					harvest()
					till()
					plant(Entities.Bush)
			elif plata_atual == madeira and can_harvest():
				harvest()
				till()
				plant(madeira)
			else:
				move(South)
		#for i in range(6):
			#if (plata_atual==madeira2)or(		
move_n_dir()
