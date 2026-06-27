import numpy as np


def compute_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    minimum = np.min(data)
    maximum = np.max(data)
    total = np.sum(data)
    return mean, median, std_dev, minimum, maximum, total


def display_report(data, mean, median, std_dev, minimum, maximum, total):
    print("\n" + "=" * 40)
    print("       STATISTICS DASHBOARD")
    print("=" * 40)
    print(f"  Total Numbers  : {len(data)}")
    print(f"  Sum            : {total:.2f}")
    print(f"  Mean           : {mean:.2f}")
    print(f"  Median         : {median:.2f}")
    print(f"  Std Deviation  : {std_dev:.2f}")
    print(f"  Minimum        : {minimum:.2f}")
    print(f"  Maximum        : {maximum:.2f}")
    print("=" * 40)


def get_input_from_user():
    print("Enter numbers separated by spaces:")
    raw = input("> ").strip()
    values = raw.split()
    data = []
    for v in values:
        try:
            data.append(float(v))
        except ValueError:
            print(f"Skipping invalid value: {v}")
    return data


def get_input_from_file():
    filename = input("Enter filename (e.g. data.txt): ").strip()
    try:
        with open(filename, "r") as file:
            raw = file.read().split()
        data = []
        for v in raw:
            try:
                data.append(float(v))
            except ValueError:
                print(f"Skipping invalid value: {v}")
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def main():
    print("=" * 40)
    print("    NumPy Statistics Dashboard")
    print("=" * 40)

    while True:
        print("\n1. Enter numbers manually")
        print("2. Load numbers from a file")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            data = get_input_from_user()

        elif choice == "2":
            data = get_input_from_file()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if len(data) == 0:
            print("No valid numbers found. Please try again.")
            continue

        data = np.array(data)
        mean, median, std_dev, minimum, maximum, total = compute_statistics(data)
        display_report(data, mean, median, std_dev, minimum, maximum, total)


main()