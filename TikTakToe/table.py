def print_table(content):
    line_with_pipe = "       |"
    line_without_pipe = line_with_pipe[:-1]
    line_with_underline_and_pipe = "_______|"
    line_with_underline_and_no_pipe = line_with_underline_and_pipe[:-1]
    row_number = 0
    for row in content:
        row_number += 1
        is_last_row = row_number == len(content)
        for times in range(len(row)):
            is_last_collumn = times == len(row)-1
            if is_last_collumn:
                print(line_without_pipe, end="")
            else:
                print(line_with_pipe, end="")
        print("")

        for times in range(len(row)):
            is_last_collumn = times == len(row)-1
            with_pipe = f"   {row[times]}   |"
            without_pipe = with_pipe[:-1]
            if is_last_collumn:
                print(without_pipe, end="")
            else:
                print(with_pipe, end="")
        print("")

        for times in range(len(row)):
            is_last_collumn = times == len(row)-1
            if is_last_collumn and not is_last_row:
                print(line_with_underline_and_no_pipe, end="")
            elif is_last_collumn and is_last_row:
                print(line_without_pipe, end="")
            elif is_last_row and not is_last_collumn:
                print(line_with_pipe, end="")
            else:
                print(line_with_underline_and_pipe, end="")
        print("")
