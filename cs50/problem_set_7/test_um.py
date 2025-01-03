from um import count

def main():
    test_case()
    test_seperate_word_um()
    test_um_inside_word()

def test_case():
    assert count("UM, what do you mean?") == 1
    assert count("can you uM perhaps Ummmm come closer?") == 2
def test_seperate_word_um():
    assert count("hello um what is this?") == 1

def test_um_inside_word():
    assert count("yummy") == 0

if __name__ == '__main__':
    main()