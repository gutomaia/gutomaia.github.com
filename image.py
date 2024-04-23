import argparse
import sys
from PIL import Image
VALID_TYPES = ['favicon', 'profile']


def create_favicon(input, output):
    logo = Image.open(input)    
    logo.save(output, format='ICO', sizes=[(40, 40)])


def create_profile(input, output):
    logo = Image.open(input)    
    logo.save(output, format='PNG', sizes=[(200, 200)])


def main(argv):
    parser = argparse.ArgumentParser(description='Process some files.')
    
    parser.add_argument('file', metavar='FILE', type=str, help='The input file')
    
    parser.add_argument('-o', '--output', metavar='OUTPUT_FILE', type=str, help='Output file name')
    
    parser.add_argument('-t', '--type', metavar='TYPE', type=str, choices=VALID_TYPES, required=True,
                        help='Type of the file. Choose from: ' + ', '.join(VALID_TYPES))

    try:
        args = parser.parse_args(argv)

        input = args.file
        output = args.output
        type = args.type

        # Now you can use these variables in your code as needed
        print("Input file:", input)
        print("Output file:", output)
        print("File type:", type)
        if type == 'favicon':
            create_favicon(input, output)
        elif type =='profile':
            create_profile(input, output)

    except argparse.ArgumentError as e:
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
