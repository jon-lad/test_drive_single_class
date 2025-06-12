from lib.diary_entry import DiaryEntry

"""
Given a diary entry
we can return a formatted diary entry
"""
def test_diary_formatting():
    diary_entry = DiaryEntry("Today", "I tested a class")

    actual = diary_entry.format()

    expected = "Today: I tested a class"

    assert actual == expected

"""
Given a diary entry
count the words in the entry
"""
def test_count_words():
    diary_entry = DiaryEntry("Today", "I tested a class")

    actual = diary_entry.count_words()

    expected = 4

    assert actual == expected 

"""
Given a diary entry
Get estimate of reading time
"""
def test_reading_time():
    text = "word"
    text += " word" * 599
    diary_entry = DiaryEntry("Today", text)

    actual = diary_entry.reading_time(200)

    expected = 3

    assert actual == expected

"""
Given a diary entry
Get a chunk of words that could be read in a set amont of time
"""
def test_reading_first_chunk():
    text = "a"
    text += " a" * 9
    text += " b" * 10
    text += " c" * 10

    diary_entry = DiaryEntry("Today", text)

    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = "a"
    chunk_text += " a" * 9

    expected = chunk_text

    assert actual == expected 

"""
Given a diary entry
Get a chunk of words that could be read in a set amont of time
"""
def test_reading_last_chunk():
    text = "a"
    text += " a" * 9
    text += " b" * 10
    text += " c" * 7

    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = "c"
    chunk_text += " c" * 6

    expected = chunk_text

    assert actual == expected 

"""
Given a diary entry
Get a first chunk if called to go past last chunk
"""
def test_reading_over_last_chunk():
    text = "a" + " a" * 9 + " b" * 10 + " c" * 7
    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(10, 1)

    chunk_text = "a" + " a" * 9

    expected = chunk_text

    assert actual == expected

"""
Given reading chunk called with new wpm
return the first chunk
"""
def test_reading_with_differnt_wpm():

    text = "a" + " a" * 9 + " b" * 10 + " c" * 7

    diary_entry = DiaryEntry("Today", text)

    diary_entry.reading_chunk(10, 1)
    actual = diary_entry.reading_chunk(20, 1)

    chunk_text = "a" + " a" * 9 + " b" * 10

    expected = chunk_text

    assert actual == expected
