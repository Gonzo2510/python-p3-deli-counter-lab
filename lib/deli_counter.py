katz_deli = []

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")

    elif len(line) > 0:
        count = 1
        names = ''
        for person in line:
            katz_deli.append(person)
            names += f' {count}. {person}'
            count += 1

        numbered_line = f'The line is currently:{names}'
        print(numbered_line)

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    position = len(katz_deli)
    print(f'Welcome, {new_person}. You are number {position} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    elif len(katz_deli) > 0:
        first_person = katz_deli[0]  
        print(f'Currently serving {first_person}.')
        katz_deli.pop(0)


line(["Jacob", "Isabel", "Aaron", "Joe"])