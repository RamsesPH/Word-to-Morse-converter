from morse import encode_to_morse


def test_single_letter():
    assert encode_to_morse("A") == "/.-"


def test_word():
    assert encode_to_morse("SOS") == "/... /--- /..."


def test_sentence_with_space():
    assert encode_to_morse("HELLO WORLD") == (
        "/.... /. /.-.. /.-.. /--- /// "
        "/.-- /--- /.-. /.-.. /-.."
    )


def test_numbers():
    assert encode_to_morse("123") == "/.---- /..--- /...--"


def test_unknown_character():
    assert "/?" in encode_to_morse("HELLO!")

