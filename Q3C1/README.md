# Question 3/Challenge 1: Log File Parsing

- Used a set to store the IP addresses because it handles the uniqueness of elements.
- Added an extra function that uses collections, that handles uniqueness as well and also can count the number of repetition for each IP, if needed.
- Also, added _is_valid(ip) that checks if the IP address is valid.
- The function open and processes the file given as the argument to our script:
```console
python parser.py SampleLogFile.txt
```
_Note that you can change the logging level (INFO, DEBUG)_
