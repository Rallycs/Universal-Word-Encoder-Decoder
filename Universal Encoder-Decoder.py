# Universal Encoder/Decoder by Rallycs

def main():
    print("=== Universal Encoder/Decoder===")
    print(" Avialable numbering systems: text, ascii, binary, hex, octal")
    print("-------------------------------------------------------------------")

    #Gathing input/output formats
    input_format = input("Enter the input type: ").strip().lower()
    output_format = input("Enter the output type: ").strip().lower()

    # Gathering input text/format to convert
    print(f"\nEnter your {input_format} below:")
    print("If using numbering systems, seperate each bit with spaces. (ex. )\n")
    data = input("Your input: ").strip()

    try:
        result = convert(data, input_format, output_format)
        print("\n Converted!")
        print(f"{output_format} : {result}")
    except Exception as e:
        print("\n Conversion Failed!")
        print(f"Error: {e}")

# Converter Functions

def text_to_ascii(text):
    return [ord(char) for char in text]

def ascii_to_text(ascii_list):
    return ''.join(chr(int(a)) for a in ascii_list)

def ascii_to_hex(ascii_list):
    return [format(int(a), 'x') for a in ascii_list]

def hex_to_ascii(hex_list):
    return [int(h, 16) for h in hex_list]

def ascii_to_octal(ascii_list):
    return [format(int(a), 'o') for a in ascii_list]

def octal_to_ascii(octal_list):
    return [int(o, 8) for o in octal_list]

def ascii_to_binary(ascii_list):
    return [format(int(a), 'b') for a in ascii_list]

def binary_to_ascii(binary_list):
    return [int(b, 2) for b in binary_list]

# Conversion Function

def convert(data, input_format, output_format):
    if isinstance(data, str) and input_format != "text":
        data = data.strip().split()

    # Convert to text

    if input_format == "text":
        text = data
    elif input_format == "ascii":
        text = ascii_to_text(data)
    elif input_format == "hex":
        text = ascii_to_text(hex_to_ascii (data))
    elif input_format == "octal":
        text = ascii_to_text(ascii_to_octal(data))
    elif input_format == "binary":
        text = ascii_to_text(ascii_to_binary(data))
    else:
        raise ValueError("Invalid Input Format!")
    
    #Convert text to output

    if output_format == "text":
        return text
    elif output_format == "ascii":
        return ' '.join(map(str, text_to_ascii(text)))
    elif output_format == "hex":
        return ' '.join(ascii_to_hex(text_to_ascii(text)))
    elif output_format == "octal":
        return ' '.join(ascii_to_octal(text_to_ascii(text)))
    elif output_format == "binary":
        return ' '.join(ascii_to_binary(text_to_ascii(text)))
    else:
        raise ValueError("Invalid Output Format!")


if __name__ == "__main__":
    main()


