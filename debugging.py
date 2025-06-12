from lib.diary_entry import DiaryEntry

text = "a"
text += " a" * 9
text += " b" * 10
text += " c" * 7

diary = DiaryEntry("Title", text)

diary.reading_chunk(10, 1)
diary.reading_chunk(10, 1)
diary.reading_chunk(10, 1)
diary.reading_chunk(10, 1)