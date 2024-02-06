import subprocess


def command(command):

    # Run the command using subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def apply_reg_file(reg_file_path):
    try:
        subprocess.run(['regedit', '/s', reg_file_path], check=True)
        print("Registry file applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error applying registry file: {e}")
