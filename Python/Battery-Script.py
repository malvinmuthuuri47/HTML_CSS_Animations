# import subprocess

# def get_battery_percentage():
#     try:
#         output = subprocess.check_output(["powershell", "-Command",
#                                           "(Get-WmiObject -Query 'SELECT * FROM Win32_Battery').EstimatedChargeRemaining"])
#         battery_percentage = int(output.decode().strip())
#         return f"Battery Percentage: {battery_percentage}%"
#     except subprocess.CalledProcessError:
#         return "COuld not retrieve battery percentage."

# if __name__ == "__main__":
#     print(get_battery_percentage())

import subprocess

def get_battery_percentage():
    try:
        output = subprocess.check_output(["powershell", "-Command", 
                                          "(Get-WmiObject -Query 'SELECT * FROM Win32_Battery').EstimatedChargeRemaining"])
        battery_percentage = output.decode().strip()
        if not battery_percentage:
            return "No battery found or the compliant driver is disabled."
        return f"Battery Percentage: {battery_percentage}%"
    except subprocess.CalledProcessError:
        return "Could not retrieve battery percentage."

if __name__ == "__main__":
    print(get_battery_percentage())