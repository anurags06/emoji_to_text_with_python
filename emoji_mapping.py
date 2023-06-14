emoji_mapping = {
    '😊': ':)',
    '❤️': '<3',
    '👍': ':thumbs_up:',
    '🤔': ':thinking_face:',
    '😂': ':joy:',
    '🎉': ':tada:',
    # Add more emoji mappings as needed
}

def convert_emoji_to_text(text):
    converted_text = ''
    for char in text:
        if char in emoji_mapping:
            converted_text += emoji_mapping[char]
        else:
            converted_text += char
    return converted_text

def main():
    input_text = input("Enter a string containing emojis: ")
    converted_text = convert_emoji_to_text(input_text)
    print("Converted text:", converted_text)

if __name__ == '__main__':
    main()
