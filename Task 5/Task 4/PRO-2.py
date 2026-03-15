def manual_split(line, delimiter):
    parts = []
    current = ""
    for char in line:
        if char == delimiter:
            parts.append(current)
            current = ""
        else:
            current += char
    parts.append(current)
    return parts

def read_student_data(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = manual_split(line, ',')
                if len(parts) == 3:
                    try:
                        name = parts[0]
                        hours = float(parts[1])
                        subject = parts[2]
                        data.append({'name': name, 'hours': hours, 'subject': subject})
                    except ValueError:
                        continue
    except FileNotFoundError:
        return None
    return data

def calculate_student_totals(data):
    totals = {}
    for entry in data:
        name = entry['name']
        hours = entry['hours']
        if name in totals:
            totals[name] += hours
        else:
            totals[name] = hours
    return totals

def calculate_subject_totals(data):
    totals = {}
    for entry in data:
        subject = entry['subject']
        hours = entry['hours']
        if subject in totals:
            totals[subject] += hours
        else:
            totals[subject] = hours
    return totals

def get_top_student(student_totals):
    top_name = None
    max_hours = -1
    for name, hours in student_totals.items():
        if hours > max_hours:
            max_hours = hours
            top_name = name
    return top_name, max_hours

def get_top_subject(subject_totals):
    top_subject = None
    max_hours = -1
    for subject, hours in subject_totals.items():
        if hours > max_hours:
            max_hours = hours
            top_subject = subject
    return top_subject

def main():
    data = read_student_data('students.txt')
    
    if data is None:
        print("Error: students.txt not found.")
        return
    if not data:
        print("Error: Empty or incorrectly formatted file.")
        return

    student_totals = calculate_student_totals(data)
    subject_totals = calculate_subject_totals(data)
    top_name, top_hours = get_top_student(student_totals)
    top_subject = get_top_subject(subject_totals)

    with open('summary.txt', 'w') as f:
        f.write("Total Hours Per Student:\n")
        for name, hours in student_totals.items():
            f.write(f"{name}: {hours}\n")
        
        f.write("\nTotal Hours Per Subject:\n")
        for subject, hours in subject_totals.items():
            f.write(f"{subject}: {hours}\n")
        
        f.write(f"\nTop Student: {top_name} with {top_hours} hours\n")
        f.write(f"Most Studied Subject: {top_subject}\n")

if __name__ == "__main__":
    main()