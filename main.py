#!/usr/bin/python
import argparse as ap
import ftplib
import os.path


def setup_parser() -> ap.ArgumentParser:
    parser = ap.ArgumentParser(
        add_help=True,
        description="This code allows the transfer of files via FTP",
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

def download_file(ext: str,ip_addr):

    try:
        ftp = ftplib.FTP(ip_addr)

        ftp.login('ftpuser', 'student')
        ftp.cwd('/home/ftpuser/cit383F2023')

        files = ftp.nlst()
        for file in files:
            if file.endswith(ext):
                print("downloading"+file)
                save_path=os.path.join(os.getcwd(),file)
                with open(save_path,'wb') as f:
                    ftp.retrbinary('RETR '+file,f.write)
                print(file+"downloaded successfully")
    except ftplib.error_perm as e:
        print('ftp error: ',e)
    except Exception as e:
        print("Error: ",e)
def upload_file(filename:str, ip_addr):

    try:
        with open(filename, 'rb') as file:          # checks to see if file exists
            pass
    except(FileNotFoundError):
        print("Error: file does not exist")
        return


    remote_dir = 'cit383F2023'
    ftp = None

    try:

        ftp = ftplib.FTP(ip_addr)                                   #ftp connection
        ftp.login('ftpuser', 'student')
        ftp.cwd(remote_dir)

        with open(filename, 'rb') as file:
            ftp.storbinary('STOR ' + filename, file)        # upload

        print(filename + ' uploaded successfully')
    except Exception as e:
        print("Error " + str(e))

    finally:
        if ftp is not None:
            ftp.quit()              #close connection

def execute_command(ip_addr):

    try:
        ftp = ftplib.FTP(ip_addr)

        ftp.login('ftpuser', 'student')         # ftp connection
        ftp.cwd('/home/student')
        s_cmd_stat=ftp.sendcmd('PWD')
        print(s_cmd_stat)
        files = ftp.nlst()

    except ftplib.error_perm as e:
        print('ftp error: ',e)
    except Exception as e:
        print("Error: ",e)

def main():
    my_parser = setup_parser()

    try:
        args = my_parser.parse_args()
    except ap.ArgumentError as e:
        print("There was an error in the program. Check the provided arguments.")
        print(e)
        exit(1)

    if args.fileName:
        upload_file(args.fileName,args.FTP_SERVER_ID)

    if args.fileExt:
        download_file(args.fileExt)

    if args.fileType:
        execute_command(args.FTP_SERVER_ID)

    print("The program is done.... have a great day!")

if __name__ == '__main__':
    main()
