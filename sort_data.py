def sort_data(notes):
    notes.sort(key=lambda note: note['date'])
    return notes