temperatures = [10, -20, -289, 100]


def writer(temps, file_path):

    with (file_path, 'w') as file:
        for t in temps:
            if t > -273.15:
                f = t * 9 / 5 + 32
                file.write("{}\n".format(str(f)))

writer(temperatures, "temps.txt")
