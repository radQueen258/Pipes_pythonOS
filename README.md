# Process Communication via Pipes

This project demonstrates inter-process communication in Linux using pipes, system calls, and a basic producer-consumer architecture. The program consists of two main components:

1. **Generator**: A program that generates random arithmetic expressions.
2. **Controller**: A program that orchestrates communication between the generator, a calculator (`bc`), and the terminal using Unix pipes.

---

## Project Structure

- **generator.py**: Produces arithmetic expressions and writes them to a pipe.
- **controller.py**: Manages inter-process communication, processes expressions, and outputs results.

---

## Requirements

### System Requirements

- **Linux-based OS**: The code uses system calls like `fork()`, `pipe()`, and `execve()` which are specific to Linux.
- **Python 3**: Both programs are written in Python 3.

### Dependencies

- **bc**: A command-line calculator required by the controller. Install it using:
  ```bash
  sudo apt-get install bc
  ```

### Python Libraries

The following libraries are part of Python's standard library and do not require additional installation:
- `os`
- `signal`
- `sys`
- `random`
- `time`

---

## How to Run the Program

### Step 1: Setup

1. Clone or download the project files.
2. Ensure both `controller.py` and `generator.py` are in the same directory.

### Step 2: Make `generator.py` Executable

Run the following command to make the generator script executable:
```bash
chmod +x generator.py
```

### Step 3: Execute the Controller

Run the `controller.py` script using the Python interpreter or make it executable:

- Using Python:
  ```bash
  python3 controller.py
  ```

- Direct execution:
  ```bash
  chmod +x controller.py
  ./controller.py
  ```

### Step 4: View Output

The controller will:
1. Generate random arithmetic expressions using the generator.
2. Send these expressions to `bc` for computation.
3. Print the results in the format:
   ```
   X O Y = RESULT
   ```

---

## Example Output

```text
5 + 3 = 8
7 * 2 = 14
3 - 1 = 2
8 / 4 = 2
6 + 7 = 13
...
```

If the program receives a `SIGUSR1` signal, it will output:
```
Processed: S lines
```
Where `S` is the number of expressions processed so far.

---

## Debugging & Testing

### Redirect Output to File

To manage large output:
```bash
./controller.py > output.txt
```

### Limit Expression Count for Testing

To reduce the number of expressions generated, modify the range in `generator.py`:
```python
# Modify this line in generator.py
N = random.randint(10, 20)  # Reduced range for testing
```

---

## Known Issues

- **FileNotFoundError**: If `generator.py` is not executable, the controller will raise an error. Ensure it has the correct permissions and includes a shebang (`#!/usr/bin/env python3`) at the top of the file.
- **Missing `bc`**: Ensure `bc` is installed; otherwise, the program will fail when attempting to execute it.

---

## Dependencies Recap

1. `generator.py` must be executable or invoked with `python3`.
2. The `bc` calculator must be installed.

---

## Authors

This project was developed as part of an Operating Systems homework assignment. It demonstrates how to use Linux system calls for inter-process communication.
