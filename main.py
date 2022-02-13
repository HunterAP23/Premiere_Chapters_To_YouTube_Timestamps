import regex as re

from argparse import RawTextHelpFormatter
from pathlib import Path

from gooey import Gooey, GooeyParser

@Gooey(
    program_name="Adobe Premiere Chapter Markers to YouTube Timestamps Converter",
    default_size=(1280, 720),
    advanced=True,
    navigation="TABBED",
)
def parse_arguments():
    """Parse input arguments."""

    main_help = "Convert Adobe Premiere Chapter Markers to YouTube Timestamps"
    parser = GooeyParser(description=main_help, formatter_class=RawTextHelpFormatter)

    input_help = "Adobe Premiere Chpater Marker text file(s)."
    parser.add_argument(
        "Input",
        help=input_help,
        nargs="*",
        widget="MultiFileChooser",
        gooey_options={
            "default_dir": str(Path(__file__).parent),
            "wildcard":
                "Plaintext files (*.txt)|*.txt|"
                "All files (*.*)|*.*",
            "validator": {
                "test": "Path(item).exists() and Path(item).is_file() for r in user_input",
                "message": "Must include at least one existing file.",
            },
        },
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    for item in args.Input:
        print("Reading in {}".format(item))
        data = []
        first_line = True
        with open(item, "r", encoding="utf-16-le") as filedata:
            for line in filedata.readlines():
                # Skip first line that's just a header
                if first_line:
                    first_line = False
                    continue
                # Split into "Asset Name, In Point, Description"
                splitter = " ".join(line.strip("\t\n").split("\t\t\t")[1:]) + "\n"
                # Grab the old timestamps
                timestamps_old = splitter.split(" ")[0]
                # Remove the last section of the timestamps used for the frames
                timestamps_new = ":".join(timestamps_old.split(":")[:-1])
                # Replace the old time stamps with the new ones
                splitter = splitter.replace(timestamps_old, timestamps_new)
                # Add the fixed line to the list
                data.append(splitter)
        print("Parsed {}".format(item))

        if data[-1].split(":")[0] == "00":
            for i in range(len(data)):
                data[i] = ":".join(data[i].split(":")[1::])
        
        print("Reformatted {}".format(item))

        with open(item, "w", encoding="utf-16-le") as filedata:
            filedata.writelines(data)
        print("Finished writing changes to {}".format(item))
    print("Program completed.")
    
