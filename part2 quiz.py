class Binusmaya:
    def __init__(self):
        self.lecturers = [
            {
                'name': 'Mr. John',
                'subject': 'Language Arts',
                'id': '2899018766'
            },
            {
                'name': 'Mrs. Carly',
                'subject': 'Media Science',
                'id': '2891023351'
            },
            {
                'name': 'Mr. Kyle',
                'subject': 'Design Media',
                'id': '2091876626'
            },
        ]
        self.classes = ['L1AC', 'L1BC', 'L1CC']
        self.schedules = []

    def profile_lecturer(self):
        print(self.lecturers)

    def add_lecturer(self):
        name = input("Enter lecturer name: ")
        subject = input("Enter lecturer subject: ")
        lecturerID = input("Enter lecturer ID: ")
        for lecturer in self.lecturers:
            if lecturer['subject'] == subject:
                print("Lecturer for subject {} already exists.".format(subject))
                return
        lecturer_data = {'name': name, 'subject': subject, 'lecturerID': lecturerID}
        self.lecturers.append(lecturer_data)
        print("Lecturer added: {}".format(lecturer_data))

    def remove_lecturer(self):
        lecturerID = input("Enter lecturer ID to remove: ")
        for lecturer in self.lecturers:
            if lecturer['lecturerID'] == lecturerID:
                self.lecturers.remove(lecturer)
                print("Lecturer with ID {} removed.".format(lecturerID))
                return
        print("Lecturer with ID {} not found.".format(lecturerID))

    def add_class(self):
        class_code = input("Enter class code: ")
        if class_code in self.classes:
            print("Class code {} already exists.".format(class_code))
            return
        self.classes.append(class_code)
        print("Class code {} added.".format(class_code))

    def remove_class(self):
        class_code = input("Enter class code to remove: ")
        if class_code in self.classes:
            self.classes.remove(class_code)
            print("Class code {} removed.".format(class_code))
            return
        print("Class code {} not found.".format(class_code))

    def add_schedule(self):
        class_code = input("Enter class code: ")
        time = input("Enter time: ")
        subject = input("Enter subject: ")
        for lecturer in self.lecturers:
            if lecturer['subject'] == subject:
                lecturer_name = lecturer['name']
                schedule_tuple = (time, class_code, subject, lecturer_name)
                self.schedules.append(schedule_tuple)
                print("Schedule added: {}".format(schedule_tuple))
                return
        print("No lecturer found for subject {}.".format(subject))


def start():
    binus = Binusmaya()
    while True:
        print(f"1. List of Lecturers")
        print(f"2. Add Lecturer")
        print(f"3. Remove Lecturer")
        print(f"4. Add Class")
        print(f"5. Remove Class")
        print(f"6. Add Schedule")
        print(f"7. Quit")

        choice = input("Select the option you desire:")

        if choice == "1":
            binus.profile_lecturer()
        elif choice == "2":
            binus.add_lecturer()
        elif choice == "3":
            binus.remove_lecturer()
        elif choice == "4":
            binus.add_class()
        elif choice == "5":
            binus.remove_class()
        elif choice == "6":
            binus.add_schedule()
        elif choice == "7":
            break
        else:
            print("Please reenter the choice.")


if __name__ == '__main__':
    start()

