import argparse
import sys
from managers import database_manager as database
from managers import database_translator as translator

# sets parser and adds arguments
parser = argparse.ArgumentParser(description="Notes & Tasker App")
parser.add_argument("-n", "--new", type=str, dest="new_note", help="Adds a new note")
parser.add_argument("-d", "--delete", type=int, dest="delete_note", help="Deletes a note")
parser.add_argument("-u", "--update", type=int, dest="update_note", help="Updates a note content")
parser.add_argument("-c", "--content", type=str, dest="new_content", required="--update" in sys.argv)

args = parser.parse_args()

def show_all():
	for item in translator.full_log:
		print(item)

if __name__ == '__main__':
	show_all()

	if argument := args.new_note:
		database.add_data(argument)
		show_all()

	if argument := args.delete_note:
		translator.delete_note(argument)
		show_all()
	
	if argument := args.update_note:
		translator.update_note(argument, args.new_content)
		show_all()
