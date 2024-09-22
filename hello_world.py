def main():

    # This is the target sum for our added numbers in the print_hello_world function
    required_number = 8

    # These two words will be combined and printed if the target sum is met
    first_word = "Hello"
    second_word = "world"

    # This function returns "Hello world" if the target sum is met; otherwise, it returns "Try again" 
    def print_hello_world():

        # Boolean for determining if the sum is met
        is_should_print = False
    
        # numbers to be added together
        first_test_number = 6
        second_test_number = 2

        # This tests to see if the two test numbers add up to the required number
        if first_test_number + second_test_number == required_number:

            # This will change the Boolean to True if the numbers add up to the target number
            is_should_print = True
        
        # Return statement for the correct sum
        if is_should_print:
            return f"{first_word} {second_word}"

        # Return statement for the incorrect sum
        else:
            return "Try again"

    print(print_hello_world())

main()