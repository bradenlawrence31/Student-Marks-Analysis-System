import numpy as np


# =============================================================================
# STUDENT MARKS ANALYSIS SYSTEM
# A simple project demonstrating NumPy arrays and statistical operations
# =============================================================================

def create_student_data():
    """
    Create and return a 2D NumPy array containing student marks.

    Structure: Each row represents a student, each column represents a subject.
    Subjects: [Math, Physics, Chemistry, English, Computer Science]
    """
    # Sample data: 5 students with marks in 5 subjects
    marks = np.array([
        [85, 78, 92, 88, 90],  # Student 1
        [76, 82, 79, 85, 88],  # Student 2
        [92, 95, 89, 91, 94],  # Student 3
        [68, 72, 75, 70, 73],  # Student 4
        [88, 85, 87, 89, 86]  # Student 5
    ])

    # Student names corresponding to each row
    student_names = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

    # Subject names corresponding to each column
    subjects = np.array(['Math', 'Physics', 'Chemistry', 'English', 'Computer'])

    return marks, student_names, subjects


def calculate_student_statistics(marks):
    """
    Calculate statistics for each student across all subjects.

    Parameters:
    marks (ndarray): 2D array of shape (n_students, n_subjects)

    Returns:
    tuple: (averages, maximums, minimums, std_devs) - all 1D arrays
    """
    # Calculate average marks for each student (axis=1 means row-wise)
    averages = np.mean(marks, axis=1)

    # Calculate maximum mark for each student
    maximums = np.max(marks, axis=1)

    # Calculate minimum mark for each student
    minimums = np.min(marks, axis=1)

    # Calculate standard deviation for each student
    std_devs = np.std(marks, axis=1)

    return averages, maximums, minimums, std_devs


def rank_students(student_names, averages):
    """
    Rank students based on their average marks (highest to lowest).

    Parameters:
    student_names (ndarray): Array of student names
    averages (ndarray): Array of average marks

    Returns:
    tuple: (ranked_names, ranked_averages, ranks)
    """
    # argsort gives indices that would sort the array
    # [::-1] reverses the array to get descending order
    sorted_indices = np.argsort(averages)[::-1]

    # Reorder names and averages based on sorted indices
    ranked_names = student_names[sorted_indices]
    ranked_averages = averages[sorted_indices]

    # Create rank array (1, 2, 3, ...)
    ranks = np.arange(1, len(student_names) + 1)

    return ranked_names, ranked_averages, ranks


def display_results(student_names, marks, averages, maximums, minimums, std_devs, subjects):
    """
    Display all analysis results in a formatted manner.
    """
    print("=" * 80)
    print("STUDENT MARKS ANALYSIS SYSTEM".center(80))
    print("=" * 80)

    # Display original data
    print("\n📚 SUBJECT-WISE MARKS")
    print("-" * 80)
    print(f"{'Student':<15}", end="")
    for subject in subjects:
        print(f"{subject:<12}", end="")
    print()
    print("-" * 80)

    for i, name in enumerate(student_names):
        print(f"{name:<15}", end="")
        for mark in marks[i]:
            print(f"{mark:<12.2f}", end="")
        print()

    # Display student statistics
    print("\n📊 STUDENT-WISE STATISTICS")
    print("-" * 80)
    print(f"{'Student':<15}{'Average':<12}{'Maximum':<12}{'Minimum':<12}{'Std Dev':<12}")
    print("-" * 80)

    for i, name in enumerate(student_names):
        print(f"{name:<15}{averages[i]:<12.2f}{maximums[i]:<12.2f}"
              f"{minimums[i]:<12.2f}{std_devs[i]:<12.2f}")

    # Display rankings
    print("\n🏆 STUDENT RANKINGS (by Average)")
    print("-" * 80)
    ranked_names, ranked_averages, ranks = rank_students(student_names, averages)
    print(f"{'Rank':<8}{'Student':<15}{'Average':<12}")
    print("-" * 80)

    for i in range(len(ranks)):
        # Add medal emojis for top 3
        medal = "🥇" if ranks[i] == 1 else "🥈" if ranks[i] == 2 else "🥉" if ranks[i] == 3 else "  "
        print(f"{ranks[i]:<8}{ranked_names[i]:<15}{ranked_averages[i]:<12.2f} {medal}")

    # Display class statistics
    print("\n📈 CLASS STATISTICS")
    print("-" * 80)
    print(f"Total Students:        {len(student_names)}")
    print(f"Class Average:         {np.mean(averages):.2f}")
    print(f"Highest Average:       {np.max(averages):.2f}")
    print(f"Lowest Average:        {np.min(averages):.2f}")
    print(f"Class Std Deviation:   {np.std(averages):.2f}")

    # Subject-wise analysis
    print("\n📝 SUBJECT-WISE CLASS AVERAGES")
    print("-" * 80)
    subject_averages = np.mean(marks, axis=0)  # axis=0 means column-wise
    for i, subject in enumerate(subjects):
        print(f"{subject:<15}: {subject_averages[i]:.2f}")

    print("\n" + "=" * 80)


def main():
    """
    Main function to run the Student Marks Analysis System.
    """
    # Step 1: Create student data
    marks, student_names, subjects = create_student_data()

    # Step 2: Calculate statistics
    averages, maximums, minimums, std_devs = calculate_student_statistics(marks)

    # Step 3: Display results
    display_results(student_names, marks, averages, maximums,
                    minimums, std_devs, subjects)

    # Bonus: Save results to file
    print("\n💾 Saving results to 'student_analysis.txt'...")

    # Create a structured array for easy saving
    with open('student_analysis.txt', 'w') as f:
        f.write("STUDENT MARKS ANALYSIS RESULTS\n")
        f.write("=" * 50 + "\n\n")

        for i, name in enumerate(student_names):
            f.write(f"Student: {name}\n")
            f.write(f"  Average: {averages[i]:.2f}\n")
            f.write(f"  Maximum: {maximums[i]:.2f}\n")
            f.write(f"  Minimum: {minimums[i]:.2f}\n")
            f.write(f"  Std Dev: {std_devs[i]:.2f}\n\n")

    print("✅ Results saved successfully!")


# =============================================================================
# BONUS: Interactive Mode
# =============================================================================

def interactive_mode():
    """
    Allow users to input their own student data.
    """
    print("\n🎓 INTERACTIVE MODE")
    print("-" * 80)

    n_students = int(input("How many students? "))
    n_subjects = int(input("How many subjects? "))

    # Initialize arrays
    marks = np.zeros((n_students, n_subjects))
    student_names = []
    subjects = []

    # Get subject names
    print("\nEnter subject names:")
    for j in range(n_subjects):
        subjects.append(input(f"  Subject {j + 1}: "))
    subjects = np.array(subjects)

    # Get student data
    print("\nEnter student data:")
    for i in range(n_students):
        name = input(f"\nStudent {i + 1} name: ")
        student_names.append(name)

        print(f"Enter marks for {name}:")
        for j in range(n_subjects):
            marks[i, j] = float(input(f"  {subjects[j]}: "))

    student_names = np.array(student_names)

    # Calculate and display results
    averages, maximums, minimums, std_devs = calculate_student_statistics(marks)
    display_results(student_names, marks, averages, maximums,
                    minimums, std_devs, subjects)


# =============================================================================
# Run the program
# =============================================================================

if __name__ == "__main__":
    print("\n Welcome to Student Marks Analysis System (NumPy Edition)")
    print("\nChoose mode:")
    print("1. Demo Mode (pre-loaded data)")
    print("2. Interactive Mode (enter your own data)")

    choice = input("\nEnter choice (1 or 2): ")

    if choice == "1":
        main()
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid choice! Running demo mode...")
        main()