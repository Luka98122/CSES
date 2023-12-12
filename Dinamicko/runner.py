import subprocess
import threading


def terminate_process(process):
    process.terminate()


def run_script(script_path):
    process = subprocess.Popen(
        ["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Timer to terminate the process after 1 second
    timer = threading.Timer(5.0, terminate_process, [process])
    timer.start()

    try:
        stdout, stderr = process.communicate()
    finally:
        timer.cancel()

    return stdout, stderr


# Replace 'your_script.py' with the path to the script you want to run
output, error = run_script("BookShopv6.py")
print("Output:", output.decode())
print("Error:", error.decode())
