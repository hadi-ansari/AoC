def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    devices = {}

    for l in lines:
      splitted_line = l.split()
      device_name =  splitted_line[0][0:-1]
      outputs = splitted_line[1:]
      devices[device_name] = outputs

    input_file.close()

    return devices