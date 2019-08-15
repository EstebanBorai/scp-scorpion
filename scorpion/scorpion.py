import os
import json

current_dir = os.getcwd()
config_file = f'{current_dir}/scorpion.json'
is_first_time = False

def get_config():
	try:
		with open(config_file, 'r') as config:
			return json.loads(config.read())
	except IOError:
		return init_config()

def init_config():
	is_first_time = True
	print('Creating a new "scorpion.json"\n')
	origin = input('Enter path of files to copy (relative): ')
	target = input('Enter path to copy files (absolute): ')
	user = input('Enter user to authenticate with: ')
	address = input('Enter address (IP) for target: ')

	with open(config_file, 'w') as new_config_file:
		new_config = {
			'user': user,
			'address': address,
			'origin': origin,
			'target': target,
		}

		json.dump(new_config, new_config_file, indent=2)
		return new_config

def print_config(config):
	for key in config:
		print(f'[SCORPION] :: {key} :: {config[key]}')

def prompt_launch_on_init():
	"""
		If this is the first time the user runs scorpion,
		ask before running
	"""

def start():
	"""
		Initializes files sharing
	"""
	config = get_config()
	print_config(config)

start()
