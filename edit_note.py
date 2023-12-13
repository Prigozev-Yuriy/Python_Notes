
def edit_note(notes, note_id, new_title=None, new_body=None, new_date=None):
    for note in notes:
        if note['id'] == note_id:
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            if new_date:
                note['date'] = new_date
            break