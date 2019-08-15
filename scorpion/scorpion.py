import os
import json

current_dir = os.getcwd()
config_file = f'{current_dir}/scorpion.json'
is_first_time = False

def get_config():
	"""
		Attempt to gather configuration from the
		current working directory.
		If the file doesn't exists creates a new
		configuration file
	"""
	try:
		with open(config_file, 'r') as config:
			return json.loads(config.read())
	except IOError:
		return init_config()

def init_config():
	"""
		Creates a new `scorpion.json`
	"""
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

def log(line):
	print(f'[SCORPION]\t::\tRunning\t$ {line}')

def prompt_launch_on_init():
	"""
		Prompt user before running file transfer
		if config was created in this instance
	"""
	run_now = input('Enter "Y" to execute scorpion, any other key to abort.\n')
	return run_now.lower() == 'y'

def print_config(config):
	"""
		Prints loaded configuration
	"""
	for key in config:
		print(f'[SCORPION]\t::\t{key}\t::\t{config[key]}')

	if is_first_time:
		return prompt_launch_on_init()

def recreate(config):
	"""
		Removes files from the
		current target
	"""
	target = config.get('target')
	address = config.get('address')
	user = config.get('user')

	cmd_remove = f'ssh {user}@{address} rmdir {target}'
	cmd_create = f'ssh {user}@{address} mkdir -p {target}'
	log(cmd_remove)
	os.system(cmd_remove)
	log(cmd_create)
	os.system(cmd_create)

def copy_new_files(config):
	origin = config.get('origin')
	target = config.get('target')
	address = config.get('address')
	user = config.get('user')

	cmd_copy = f'scp -r {origin} {user}@{address}:{target}'
	log(cmd_copy)
	os.system(cmd_copy)

def start():
	"""
		Initializes files sharing
	"""
	config = get_config()
	run_now = print_config(config)

	if not is_first_time:
		recreate(config)
		copy_new_files(config)
	else:
		if is_first_time and run_now:
			recreate(config)
			copy_new_files(config)
		else:
			print('scorpion exited')
			return

start()
