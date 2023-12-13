def add_note(notes, new_note):
    max_id = max(note['id'] for note in notes) if notes else 0
    new_note['id'] = max_id + 1
    notes.append(new_note)