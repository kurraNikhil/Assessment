def reverse_file(studen_details):
  with open("student_details.txt", "r") as f:
    lines = f.read()
    print(lines[::-1])


if __name__ == "__main__":
  studen_details = "test.txt"
  reverse_file(studen_details)


