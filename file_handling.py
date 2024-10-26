

# Step 1: Create a new file named "my_file.txt" in write mode and write three lines of text
with open("my_file.txt", 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("Here is the second line with a number: 42\n")
    file.write("This is the third line with more text.\n")

# Step 2: Read the contents of "my_file.txt" and display them on the console
with open("my_file.txt", 'r') as file:
    content = file.read()
    print("Contents of 'my_file.txt' after initial write:\n")
    print(content)

# Step 3: Open "my_file.txt" in append mode and add three additional lines of text
with open("my_file.txt", 'a') as file:
    file.write("Appending the fourth line with text.\n")
    file.write("The fifth line has a number: 12345\n")
    file.write("Finally, the sixth line wraps it up.\n")

# Step 4: Read the updated contents of "my_file.txt" and display them on the console
with open("my_file.txt", 'r') as file:
    updated_content = file.read()
    print("\nContents of 'my_file.txt' after appending:\n")
    print(updated_content)
