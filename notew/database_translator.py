import time
from .tools.note_class import Note
import .database_manager as database

# data modeling
def model_data():
	data = []
	for item in database.raw_load:
		identity, content, unixstamp = item
		item = Note(identity, content, unixstamp)
		data.append(item)
	return data

# loads all data
full_log = []
modeled_data = model_data()

for index, item in enumerate(modeled_data):
	content = item.content
	fmt = f"\t{str(index + 1)}{" " * 5}{content}"
	full_log.append(fmt)

# database speakers
identity_from_index = lambda index : modeled_data[index -1].identity

def delete_note(note_index):
	database.delete_data(identity_from_index(note_index))

def update_note(note_index, new_content):
	database.update_data(new_content, identity_from_index(note_index))