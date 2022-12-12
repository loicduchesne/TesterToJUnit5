# USER SETUP

# Action needed:
# 1) Specify the tester file name (if in same directory) or the path (if in another directory) in 'file_name'.
# 2) Specify the new tester name in 'new_tester_name'.

# *Note: This will generate a new file in this working directory. Will not work if there is already a file of the same
# name.

file_name = 'A3_Minitester.java' # Recommended: file_name should not be the same as new_tester_name.
new_tester_name = 'CatCafeTest'  # E.g. CatCafeTest, DeckTest, SwarmOfHornetsTest, ...


# PROGRAM (*No need to configure anything else in here) ----------------------------------------------------------------
new_tester_data = []
original_tester = []

# Open original file
with open(file_name) as f:
    tester_data = f.readlines()
    for original_line in tester_data:
        original_tester.append(original_line)
f.close()

# Add JUnit5 import statements
new_tester_data.append('import org.junit.jupiter.api.Test;' + '\n')
new_tester_data.append('\n')

# Track open bracket pairs
bracket_count = 0
drop_bracket = False

# If it is the first test class in the file
first_class = True

for curr_line in original_tester:
    # bracket counter
    if bracket_count > 0:
        if '{' in curr_line:
            bracket_count += 1
        elif '}' in curr_line:
            bracket_count -= 1
            if bracket_count == 0:
                drop_bracket = True

    if drop_bracket:  # If a bracket needs to be ignored.
        drop_bracket = False
        continue
    elif 'public class' in curr_line:  # If it is the end tester statement.
        new_tester_data.append('}')
        break
    elif 'class' in curr_line:  # If it is one of the tester classes.
        if first_class:  # If it is the first tester class, add the parent class that groups all testers.
            new_tester_data.append('class ' + new_tester_name + ' {' + '\n')
            first_class = False

        tmp_arr = curr_line.split()
        new_tester_data.append('@Test' + '\n')
        new_tester_data.append('void ' + tmp_arr[1] + '()' + ' {' + '\n')
    elif '@Override' in curr_line:  # Ignore if there is an @Override statement.
        continue
    elif 'run' in curr_line:  # Ignore if there is a public void run statement & start bracket counter.
        bracket_count += 1
        continue
    else:  # Else just append the line.
        new_tester_data.append(curr_line)

# Open JUnit file
new_f = open(new_tester_name + '.java', 'x')
for new_line in new_tester_data:
    new_f.write(new_line)
new_f.close()