notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

chord_steps = {
    "Major": [4, 7],
    "Minor": [3, 7],
    "Augmented fifth": [4, 8],
    "Minor fifth": [4, 6],
    "Major sixth": [4, 7, 9],
    "Minor sixth": [3, 7, 9],
    "Dominant seventh": [4, 7, 10],
    "Minor seventh": [3, 7, 10],
    "Major seventh": [4, 7, 11],
    "Diminished seventh": [3, 6, 10]
}

def get_chord_notes(key, chord_type):
    key = key.upper()
    
    if key not in notes:
        return f"Key '{key}' not recognized. Please enter a valid musical key."

    chord_type = chord_type.title()
    
    steps = chord_steps.get(chord_type)
    if steps is None:
        return f"Chord type '{chord_type}' not recognized. Please enter a valid chord type."

    start_index = notes.index(key)
    
    chord_notes = [key]  # Start with the root note
    for step in steps:
        note_index = (start_index + step) % len(notes)
        chord_notes.append(notes[note_index])
    
    return chord_notes

key = input("Enter the musical key (e.g., C, D#, F#): ").strip()
chord_type = input("Enter the chord type (e.g., Major, Minor, Dominant seventh): ").strip()

chord_notes = get_chord_notes(key, chord_type)
if isinstance(chord_notes, list):
    print("The notes in the", key.capitalize(), chord_type.title(), "chord are:", chord_notes)
else:
    print(chord_notes)
