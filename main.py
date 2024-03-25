#!/usr/bin/python
import argparse as ap
from socket import *
import ftplib
import os
# create the argument parser

def setup_parser()-> ap.ArgumentParser:
    # create the object
    parser = ap.ArgumentParser(
        add_help=True,
        description="This code does blah",
        usage="./lab9 SERVER_IP_ADD)[]",
        prog="FTP_FILE_DOWNLOADER"
    )

    # add help argument
    parser.add_argument("FTP_SERVER_ID", action="store", dest="ftp_ip", type=str)

    # add the options
    parser.add_argument("l", action="store", dest="fileType")
    parser.add_argument("u", action="store", dest="fileName")
    parser.add_argument("d", action="store", dest="fileExt")

    return parser


# download file
def download_file(ext:str):
    ftp= ftplib.FTP('10.2.59.137')
    ftp.login('student','student')
    ftp.cwd('/home/student')
    files=ftp.nlst()
    for file in files:
        print(file)


# upload file

def upload_file(filename:str):
    pass


def execute_command():
    cmd = "ls"
    # send the command to the FTP server, and have it return the results
    # nlist --- make sure you are in the required directory
    pass

def main():
    my_parser = setup_parser()

    # parser the variable/options
    try:
        args = my_parser.parse_args()
    except:
        print("There was an error int he program. Check the blah")
        exit(1)

    # call the required methods

    if args.filename:
        upload_file(args.filename)

    # since the options are not mutually exclusive, I am not using an else part
    if args.fileExt:
        download_file(args.fileExt)

    if args.fileType:
        execute_command()

    print("The program is done.... have a great day!")


main()

# if __name__ == '__main__':
#     main()
