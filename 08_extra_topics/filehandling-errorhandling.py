# ============================================================
# FILE HANDLING + ERROR HANDLING
# ============================================================
#
# File handling allows Python to:
# - Create files
# - Read files
# - Write to files
# - Append data to files
#
# Error handling allows us to handle errors/exceptions
# without crashing the entire program.
#
# Common file modes:
#
# "r" -> Read
# "w" -> Write (creates/overwrites the file)
# "a" -> Append (adds data at the end)
# "x" -> Create a new file
#
# ============================================================


# ============================================================
# 1. WRITE TO A FILE
# ============================================================

file = open("example.txt", "w")

try:
    # Write data into the file.
    file.write("Hello Sahil!")

finally:
    # The finally block always runs, whether an error occurs
    # or not.
    #
    # We close the file here to release the file resource.
    file.close()


# ============================================================
# 2. USING "with" - RECOMMENDED WAY
# ============================================================
#
# Instead of manually opening and closing the file, we can use
# the "with" statement.
#
# Python automatically closes the file when the "with" block
# finishes, even if an error occurs.
# ============================================================

with open("example.txt", "w") as file:

    # "w" mode overwrites the existing file content.
    file.write("Hello Sahil Bro!")


# ============================================================
# 3. READING A FILE
# ============================================================

try:

    # Open the file in read mode.
    with open("example.txt", "r") as file:

        # Read the entire file.
        content = file.read()

        print("File Content:")
        print(content)

except FileNotFoundError:
    # This error occurs when the file doesn't exist.
    print("Error: File not found.")


# ============================================================
# 4. APPENDING TO A FILE
# ============================================================
#
# "a" mode adds new content to the end of the file.
# It does NOT remove the existing content.
# ============================================================

with open("example.txt", "a") as file:

    file.write("\nLearning Python File Handling")


# Read the file again to see the appended content.
with open("example.txt", "r") as file:

    content = file.read()

    print("\nUpdated File Content:")
    print(content)


# ============================================================
# 5. HANDLING DIFFERENT FILE ERRORS
# ============================================================

try:

    # Trying to read a file that may not exist.
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:

    print("Error: example.txt does not exist.")

except PermissionError:

    print("Error: You don't have permission to access the file.")

except Exception as e:

    # General exception handler.
    #
    # 'e' contains the actual error message.
    print(f"Something went wrong: {e}")


# ============================================================
# 6. TRY / EXCEPT / ELSE / FINALLY
# ============================================================
#
# try     -> Code that might cause an error
# except  -> Handles the error
# else    -> Runs only when NO error occurs
# finally -> Always runs
# ============================================================

try:

    with open("example.txt", "r") as file:

        content = file.read()

except FileNotFoundError:

    print("File does not exist.")

else:

    # This runs only if the file was successfully read.
    print("\nFile read successfully!")
    print(content)

finally:

    # This always runs.
    print("File handling operation completed.")


# ============================================================
# IMPORTANT
# ============================================================
#
# Older/manual approach:
#
#     file = open("example.txt", "r")
#
#     try:
#         content = file.read()
#
#     finally:
#         file.close()
#
#
# Recommended approach:
#
#     with open("example.txt", "r") as file:
#         content = file.read()
#
#
# The "with" statement automatically handles closing the file.
#
# Therefore, for normal file handling, prefer:
#
#     with open(...) as file:
#
# ============================================================