import sys
from datetime import timedelta

def print_expected_call_message(additional_message):
    print(f"""{additional_message}
Expected application call:
python3 regex_text.py [searched phrase] [left_padding] [right_padding]
Example call:
python3 regex_text.py "I don't know" 2 3""")



def handle_arguments():
    if not (arg_len := len(sys.argv)) == 4:
        print_expected_call_message(f'Expected two arguments, got {arg_len-1}.')
        exit()
    try:
        phrase = sys.argv[1]
        padding_left, padding_right = [timedelta(int(number)) for number in sys.argv[2:4]]
        return([phrase, padding_left, padding_right])
    except:
        print_expected_call_message(f'An error has occured.')
        exit()
