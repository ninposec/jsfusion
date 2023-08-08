import os
import argparse
from jsbeautifier import beautify_file

def beautify_and_save(input_path, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for root, _, files in os.walk(input_path):
        for filename in files:
            if filename.endswith('.js'):
                input_file_path = os.path.join(root, filename)
                beautified_code = beautify_file(input_file_path)

                output_file_path = os.path.join(output_directory, filename.replace('.js', '_beautified.txt'))

                # Save beautified code to the output text file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(beautified_code)

                print(f'Beautified {input_file_path} and saved to {output_file_path}')

def main():
    parser = argparse.ArgumentParser(description='Convert JavaScript files to beautified text files')
    parser.add_argument('--path', required=True, help='Path to the folder containing JS files')
    parser.add_argument('--out', required=True, help='Path to the output folder')
    args = parser.parse_args()

    beautify_and_save(args.path, args.out)

if __name__ == '__main__':
    main()
