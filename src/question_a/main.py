from question_a import get_person_category

def main():
    while True:
        try:
            age = int(input("Enter the person's age (or -1 to quit): "))
            if age == -1:
                print("Goodbye!")
                break
            category = get_person_category(age)
            print(f"The person is a {category}.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
