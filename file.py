def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", 'w')

    file.write("Company, Position, Location, URL\n")

    for job in jobs:
        file.write(f"{job['Company']}, {job['Position']},{job['Location']}, {job['URL']}\n")

    file.close()