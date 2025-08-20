def file_read_write():
    # Step 1: Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Step 3: Ask user how to modify the content
        print("\nChoose a modification option:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Reverse text")
        print("4. Add line numbers")
        print("5. Replace a word")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            modified_content = content.upper()
        elif choice == "2":
            modified_content = content.lower()
        elif choice == "3":
            modified_content = content[::-1]
        elif choice == "4":
            modified_content = ""
            for i, line in enumerate(content.splitlines(), start=1):
                modified_content += f"{i}: {line}\n"
        elif choice == "5":
            word_to_replace = input("Enter the word to replace: ")
            replacement = input("Enter the replacement word: ")
            modified_content = content.replace(word_to_replace, replacement)
        else:
            print("Invalid choice. No modifications applied.")
            modified_content = content

        # Step 4: Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(
            f"\nFile read successfully. Modified content saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
file_read_write()


# Enter the filename to read: calculate_discount.py

# Choose a modification option:
# 1. Convert to UPPERCASE
# 2. Convert to lowercase
# 3. Reverse text
# 4. Add line numbers
# 5. Replace a word
# Enter your choice (1-5): 1

# File read successfully. Modified content saved as 'modified_calculate_discount.py'.
