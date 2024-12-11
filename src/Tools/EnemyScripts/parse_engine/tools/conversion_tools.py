
class enemy_data:
    def __init__(self, type, nodes):
        self.type = type
        self.nodes = nodes




class tools:
    @staticmethod
    def char_array_to_array(char_array, seperator_start, seperator_end):
        # Initialize the buffer that has the elements written to
        buffer = []
        # Initialize the current index
        index = 0
        while True:
            string = ""
            # Detect square brackets and dump contents into string variable
            if seperator_start in char_array[index]:
                string += char_array[index] + ","
                while  seperator_end not in char_array[index]:
                    index += 1
                    #Adds commas as they are needed for future processing
                    string += char_array[index] +","
            # Strips leading and trailing commas as they are unneeded and add complexity
            string = string.strip(",")
            buffer.append(string)
            # Checks if it is done
            if index >= len(char_array)-1:
                return buffer
            index += 1

    @staticmethod
    def char_array_to_enemy_data(char_array, index):

        # Sets the extracted data to the char_array and extracts the enemy type as well as the nodes in string format
        data_extracted = char_array
        data_extracted = tools.char_array_to_array(data_extracted, '[', ']')[index]

        # Splits the data based off the position of the commas
        data_seperated = data_extracted.split(",")

        # Removes brackets and other unnecessary characters
        type = data_seperated[0].strip("[],{}()")
        nodes = tools.char_array_to_array(data_seperated[1:], '(', ')')
        buffer = []

        # Converts the nodes from strings to float arrays
        for i in nodes:
            i = i.strip("()[]").split(",")
            buffer.append([float(i[0]), float(i[1])])

        nodes = buffer

        return enemy_data(type, nodes)