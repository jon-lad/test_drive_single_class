class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self._title = title
        self._contents = contents
        self._current_chunk = 0
        self._chunk_size = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self._title}: {self._contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self._contents.split()
        return len(words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        words = self._contents.split()
        return int(len(words) / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        #Check the size of the chunks hasent changed if it has
        #return the first chunk again
        chunk_size = wpm * minutes
        if self._chunk_size != chunk_size:
            self._current_chunk = 0

        words = self._contents.split()

        #Set the attribute
        self._chunk_size = chunk_size
        chunk_quantity = len(words) / chunk_size
        chunk_start = self._current_chunk * chunk_size
        chunk_end = chunk_start + chunk_size

        if self._current_chunk < chunk_quantity -1:
            chunk = words[chunk_start:chunk_end]
            self._current_chunk += 1
        else:
            chunk = words[chunk_start:]
            self._current_chunk = 0

        return " ".join(chunk)
