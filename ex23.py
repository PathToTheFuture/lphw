import sys # import the entire system module

script, encoding, error = sys.argv  # take the command-line arguments encoding and error and pass them in when running ex23.py script

def main(language_file, encoding, errors): # define the function main
    line = language_file.readline() # Reads a line of the language_file and set it equal to line

    if line: # if statement
        print_line(line, encoding, errors) # calls the funtion print_line to print the line of the file
        return main(language_file, encoding, errors) # Creates a loop becauses as long as file is true it will keep returning main


def print_line(line, encoding, errors): # define the functon print_line
    next_lang = line.strip() # sripes the \n on the line string
    raw_bytes = next_lang.encode(encoding, errors = errors) # encodes each the line of the languages.txt that is passed into it raw_bytes<next_lang<line.strip<language_file
    cooked_string = raw_bytes.decode(encoding, errors = errors) # decodes each line of the languages.txt that is passed into it cooked_string<raw_bytes<...

    print(raw_bytes, "<===>", cooked_string) # prints raw encoding <===> decoded text


languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
