import subprocess
import tempfile
import shutil


__author__ = 'G4l_B1t'

"""
This script was created for my Bsides TLV demo.
Creating artifacts searched by malware using this script may repel potential attackers.
Feel free to use it **at your own risk**.

This script creates dynamic artifacts, thus less practical. check out its static sibling for better results and usability.
"""


temp_folder = tempfile.gettempdir()
actual_proc = "C:\\Windows\\System32\\ftp.exe"


def create_exe(fake_name):
    fake_proc = temp_folder + "\\" + fake_name
    shutil.copyfile(actual_proc, fake_proc)


def run_exe(command):
    try:
        subprocess.Popen(command)
    except Exception as e:
        print "Got exception {0} while creating {1}".format(e, command)
    return


if __name__ == '__main__':
    processes_to_mimic = [
        "Wireshark.exe",
        "OLLYDBG.exe",
        "windbg.exe",
        "joeboxcontrol",
        "sandbox.exe",
        "vmtoolsd.exe",
        "vboxtray.exe",
        "procmon.exe"
    ]

    for proc_name in processes_to_mimic:
        create_exe(proc_name)
        run_exe(temp_folder + "\\" + proc_name)

    print "Processes create successfully, close this window to terminate the sub-processes.\n"

    while True:
        pass

