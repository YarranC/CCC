# assume scripts named as j1.py, j2.py, etc
# the input the output of j*.py are in the folder j*/
# the input and output file names are like j*.**.in, and j*.**.out
# will compare the script output using the .in file with the content out .out files

import subprocess
import sys
import os
import glob
import os.path

def run_script_with_input(script_path, input_data):
    # Run the script with the provided input data
    process = subprocess.Popen([sys.executable, script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip(), stderr

def compare_output(script_path, input_file, expected_output_file):
    cur_dir = os.getcwd()
    os.chdir(os.path.join(cur_dir, script_path.split(".")[0]))
    # Read the input data from the input file
    with open(input_file, 'r') as infile:
        input_data = infile.read()

    # Read the expected output data from the expected output file
    with open(expected_output_file, 'r') as outfile:
        expected_output = outfile.read().strip()

    os.chdir(cur_dir)
    # Run the script and get the actual output
    actual_output, error = run_script_with_input(script_path, input_data)

    if error:
        print(f"Error running script with {input_file}:", error)
        return False

    # Print debug information
    print(f"Testing {input_file} against {expected_output_file}")
    print("Actual Output: ", repr(actual_output))
    print("Expected Output: ", repr(expected_output))

    # Compare the actual output with the expected output
    return actual_output == expected_output

def find_input_output_pairs(script_name):
    cur_dir = os.getcwd()
    os.chdir(os.path.join(cur_dir, script_name.split(".")[0]))
    base_name = script_name.split('.')[0]
    input_pattern = f'{base_name}.*.in'
    output_pattern = f'{base_name}.*.out'

    input_files = sorted(glob.glob(input_pattern))
    output_files = sorted(glob.glob(output_pattern))

    if len(input_files) != len(output_files):
        print(f"Error: The number of input files does not match the number of output files for {script_name}.")
        return []
    os.chdir(cur_dir)
    return list(zip(input_files, output_files))

# Example usage
if __name__ == "__main__":
    script_pattern = 'j*.py'
    script_files = sorted(glob.glob(script_pattern))
    print(script_files)
    
    all_tests_passed = True

    for script_file in script_files:
        print(f"\n*************Running tests for {script_file}**************")
        input_output_pairs = find_input_output_pairs(script_file)

        if not input_output_pairs:
            continue

        for input_file, output_file in input_output_pairs:
            try:
                result = compare_output(script_file, input_file, output_file)
                print(f"Result for {input_file} and {output_file}: {result}\n")
                if not result:
                    all_tests_passed = False
            except Exception as e:
                print(f"Exception occurred while testing {input_file} and {output_file}: {e}")
                all_tests_passed = False

    if all_tests_passed:
        print("\n*************All tests passed!*************")
    else:
        print("\n*************Some tests failed.*************")
