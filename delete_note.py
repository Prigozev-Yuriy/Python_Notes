def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note["id"] != note_id]
    for note in notes:
        if note['id'] > note_id:
            note['id'] -= 1