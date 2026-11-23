def parse_data(file_path):
    file_content = open(file_path, mode="r")
    header = file_content.readline()
    
    main_data = []
    for f in file_content:
        fs = f.strip().split("\t")
        row_data = {
            "Name": fs[0], 
            "Age": fs[1], 
            "Gender": fs[2], 
            "Country": fs[3]
        }
        main_data.append(row_data)
    return main_data
