#!/usr/bin/env python3
import sys
from collections import Counter


def main():
	"""
	Main function to process log files and generate a CSV file with the top occurring errors.

	:return: None
	"""
	if len(sys.argv) < 2:
		print("Usage: python top-errors.py <log_file>")
		return

	log_file = sys.argv[1]

	# Read the contents of the log file into a list
	with open(log_file, 'r') as file:
		log_entries = [line.strip() for line in file.readlines() if line.strip()]

	# Strip the timestamp part from each filtered entry
	filtered_entries = [filter_entries(entry) for entry in log_entries]

	# Count occurrences of each unique error
	error_counts = Counter(filtered_entries)

	# Sort errors by occurrence count in descending order
	top_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:10]

	# Output CSV data
	csv_file = log_file +'.csv'
	with open(csv_file, 'w', newline='') as output_csv:
		print('Error,Count')
		output_csv.write('Error,Count\n')
		for error, count in top_errors:
			if error is None:
				continue
			output_csv.write(f'"{error}","{count}"\n')
			print(f'"{error}","{count}"')

	print(f'\nCSV file \'{csv_file}\' has been generated successfully.', file=sys.stderr)


def filter_entries(entry):
	"""
	Filters the given entry string and returns only the PHP error messages.

	:param entry: A string containing an entry.
	:return: The PHP error message extracted from the entry, or None if no PHP error message is found.
	"""
	return entry.split('] ', 1)[1] if len(entry.split('] ', 1)) > 1 and "PHP" in entry else None


if __name__ == "__main__":
	main()
