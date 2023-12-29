import json

def check_jsonl_format(file_name):
    non_json_lines = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                line = line.strip()
                try:
                    json.loads(line)
                except json.JSONDecodeError:
                    non_json_lines.append(line_num)

        if non_json_lines:
            print("The following lines are not in JSONL format:")
            for line_num in non_json_lines:
                print(f"Line {line_num}: {lines[line_num - 1]}")
        else:
            print("All lines are in JSONL format.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input.txt' with your file name
check_jsonl_format("UAMH_training_data.jsonl")

def format_to_json(input_file, output_file):
    try:
        # Open the input file in read mode with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            # Read lines from the file
            lines = file.readlines()

            # Find lines with '{"messages"'
            message_lines = [line if '{"messages"' in line else line.strip() for line in lines]

            # Join lines preserving necessary newlines
            formatted_content = '\n'.join(message_lines)

            # Convert the formatted content to a dictionary
            formatted_dict = json.loads(formatted_content)

        # Write the dictionary content to a new JSON file
        with open(output_file, 'w', encoding='utf-8') as new_file:
            json.dump(formatted_dict, new_file, indent=4,
                      ensure_ascii=False)  # Write the dictionary in a formatted JSON style

        print(f"File formatted to JSON. New file '{output_file}' created.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def decode_mbcs_to_utf8(file_path):
    try:
        with open(file_path, 'rb') as file:
            encoded_content = file.read()

            # Decoding the content from mbcs to utf-8
            decoded_content = encoded_content.decode('mbcs')

        with open(file_path, 'w', encoding='utf-8') as file:  # Writing back to the same file
            file.write(decoded_content)

        print(f"File '{file_path}' has been decoded from 'mbcs' to 'utf-8'.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except Exception as e:
        print(f"An error occurred: {e}")


import chardet  # Library for automatic character encoding detection


def remove_anomalous_chars_and_blank_lines(file_path):
    try:
        # Detecting the file encoding
        with open(file_path, 'rb') as file:
            rawdata = file.read()
            detected_encoding = chardet.detect(rawdata)['encoding']

        # Decoding the content and removing anomalous characters and blank lines
        with open(file_path, 'r', encoding=detected_encoding, errors='replace') as file:
            lines = file.readlines()
            cleaned_lines = [line.strip() for line in lines if all(ord(c) < 128 for c in line.strip())]
            cleaned_content = '\n'.join(line for line in cleaned_lines if line)

        # Writing the cleaned content back to the file
        with open(file_path, 'w', encoding=detected_encoding) as file:
            file.write(cleaned_content)

        print(f"Anomalous characters and blank lines removed from '{file_path}'.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except Exception as e:
        print(f"An error occurred: {e}")


def decode_to_utf8(file_path):
    try:
        # Detecting the file encoding
        with open(file_path, 'rb') as file:
            rawdata = file.read()
            detected_encoding = chardet.detect(rawdata)['encoding']

        # Reading the file and decoding to utf-8
        with open(file_path, 'r', encoding=detected_encoding, errors='replace') as file:
            content = file.read()

        # Writing the decoded content back as utf-8
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"File '{file_path}' has been decoded to 'utf-8'.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'encoded_file.txt' with your file name encoded with mbcs
remove_anomalous_chars_and_blank_lines('grant_prop.txt')
decode_to_utf8('grant_prop.txt')
global api_key
api_key = "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"
