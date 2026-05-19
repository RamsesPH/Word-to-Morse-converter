"""
main.py — Command-line interface for the Morse code encoder.
"""

from morse import encode_to_morse


def main():
    message = input("Enter your message: ")
    print(f"\nYour message is: {message}\n")

    encoded = encode_to_morse(message)
    print("Morse code:")
    print(encoded)


if __name__ == "__main__":
    main()
