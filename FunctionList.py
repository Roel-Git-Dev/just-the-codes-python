def Stack_Helper(given_string):
    current_pointer =  0
    previous_pointer = -1
    tester_list = []

    for index,item in enumerate(given_string):
      if len(tester_list) > 0:
          if tester_list[previous_pointer] + item in ["()","[]","<>","{}"]:
              tester_list.pop(previous_pointer)
              current_pointer =  previous_pointer
              previous_pointer -=  1
              continue
      tester_list.insert(current_pointer,item)
      previous_pointer =  current_pointer
      current_pointer += 1
    return tester_list
