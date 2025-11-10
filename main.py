def move_n_dir(passos, lado):
	passos = 5
	lado = East
	for i in range(5):
		move(East)
	
move_n_dir(5, East)



def plantar_madeira():
	while True:
		for i in range(get_world_size()):
			for x in range(get_world_size()):
				if get_entity_type() == Entities.Bush:
					if can_harvest():
						harvest()
						till()
						plant(Entities.Bush)
						move(East)
					else:
						move(North)
				elif get_entity_type() == Entities.Bush:
					till()
					plant(Entities.Bush)
					move(East)
				elif get_entity_type() == Entities.Grass:
					till()
					plant(Entities.Bush)
					move(East)
				elif get_entity_type() == till():
					plant(Entities.Bush)
					move(East)


		
plantar_madeira()

