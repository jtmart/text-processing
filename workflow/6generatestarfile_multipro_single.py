import pandas as pd
import multiprocessing


def script(thread_name, thread_number, thread_limit, g_num_files, meta, path_in, path_out):
    print(thread_name + "starting")
    cols = meta.columns
    target = thread_number
    while target < len(meta.index):
        cumulative_vars = "****"
        for index in range(0, len(cols)):
            cumulative_vars += " *{index_value}_{cell_value}".format(index_value=index + 1,
                                                                     cell_value=meta[str(cols[index])][target]) # generates a cumulative summary of all the attributes in the given row

        cumulative_vars += "\n"
        temp_in_path = path_in + meta.id[target] + ".txt"
        temp_out_path = path_out + meta.id[target] + ".txt"
        with open(temp_out_path, 'w', encoding="utf-8") as file_out:
            lines = []
            with open(temp_in_path, 'r', encoding="utf-8") as file_in:
                for line in file_in:
                    lines.append(str(line))
                file_in.close()

            file_out.write(cumulative_vars)
            file_out.writelines(lines)
            file_out.close()

        g_num_files.value -= 1
        print(thread_name, "files left ", g_num_files.value)
        target += thread_limit


if __name__ == "__main__":
    input_path = r"/data/Rdatasets/current/dips/f-beta1-3p/"  # put your input directory here (don't forget the '.')
    output_path = r"/data/Rdatasets/current/dips/o-csvs/ir-b13p/"  # put your output path here (don't forget the '.')
    t_limit = int(input("how many threads do you want? \n"))
    processes = []
    filename = r"/data/Rdatasets/current/dips/o-csvs/b13metapure.csv"
    main_df = pd.read_csv(r"/data/Rdatasets/current/dips/o-csvs/b13metapure2.csv")
    num_file = multiprocessing.Value("i", len(main_df.index))

    for i in range(0, t_limit):
        name = "PROCESS " + str(i) + ": "
        process = multiprocessing.Process(target=script,
                                          args=(name, i, t_limit, num_file, main_df, input_path, output_path,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("all processes finished")
