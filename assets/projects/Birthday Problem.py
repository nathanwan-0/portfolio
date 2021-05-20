import random

# Main function that calls two helper functions.
def test_birthday_problem():
    n_birthdays = int(input("\nEnter amount of birthdays: "))
    n_tests = int(input("Enter amount of tests: "))
    n_matches = run_tests(n_tests, n_birthdays)
    display_summary(n_tests, n_birthdays, n_matches)
    
# Creates a list of n randomly selected integers between 1 and 365 inclusive. Values represent birthdays. Returns this list.
def generate_birthdays(n):
    birthdays = []
    for i in range(0, n):
        selected_integers = random.randint(1,365)
        birthdays.append(selected_integers)
    return birthdays
    
# (birthdays) will be a list of integers where each integer represents a birthday. Returns True if any two birthdays are a match. Otherwise returns, False.
def matching_birthdays(birthdays):
    if len(birthdays) != len(set(birthdays)):
        return True
    else:
        return False
    
# Tests the birthday problem through performing the number of tests indicated by n_tests. For each test: 
# Calls the function generate_birthdays to generate a list of birthdays indicated by n_birthdays. 
# Calls the function matching_birthdays with the list of birthdays to determine if there is a matching birthday in the list. Keeps a running total of the amount of tests that found matches and return this value upon completion of all tests.
def run_tests(n_tests, n_birthdays):
    matched = 0
    for i in range(n_tests):
        birthdays = generate_birthdays(n_birthdays)
        if matching_birthdays(birthdays):
            matched += 1
    return matched
    
# Prints out the number of matches found when the given number of tests are run using the given number of birthdays indicated. Prints out the match rate as a percentage.
def display_summary(n_tests, n_birthdays, n_matches):
    print("Ran", n_tests, "tests with", n_birthdays, "birthdays each")
    print("Found matches", n_matches, "times")
    n_percentage = ((n_matches / n_tests) * 100)
    print(str(n_percentage) + "% of the tests had matching birthdays")