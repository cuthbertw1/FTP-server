#!/usr/bin/python
import argparse as ap
import ftplib

def setup_parser() -> ap.ArgumentParser:
    parser = ap.ArgumentParser(
        add_help=True,
        description="This code does blah",
        usage="./lab9 SERVER_IP_ADD []",
        prog="FTP_FILE_DOWNLOADER"
    )

    parser.add_argument("FTP_SERVER_ID", action="store", metavar="SERVER_IP_ADD", type=str,
                        help="IP address of the FTP server")
    parser.add_argument("-l", "--fileType", action="store", dest="fileType",
                        help="Specify file type")
    parser.add_argument("-u", "--fileName", action="store", dest="fileName",
                        help="Specify file name")
    parser.add_argument("-d", "--fileExt", action="store", dest="fileExt",
                        help="Specify file extension")

    return parser

def download_file(ext: str):
    ftp = ftplib.FTP('10.2.59.137')
    ftp.login('student', 'student')
    ftp.cwd('/home/student')
    files = ftp.nlst()
    for file in files:
        print(file)

def upload_file(filename: str):
    pass

def execute_command():
    pass

def main():
    my_parser = setup_parser()

    try:
        args = my_parser.parse_args()
    except ap.ArgumentError as e:
        print("There was an error in the program. Check the provided arguments.")
        print(e)
        exit(1)

    if args.fileName:
        upload_file(args.fileName)

    if args.fileExt:
        download_file(args.fileExt)

    if args.fileType:
        execute_command()

    print("The program is done.... have a great day!")

if __name__ == '__main__':
    main()
