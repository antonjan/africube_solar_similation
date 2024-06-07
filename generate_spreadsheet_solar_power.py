import pandas as pd
import math

# Constants
solar_panel_efficiency = 0.8448  # Solar panel efficiency (20%)
solar_constant = 1  # Solar constant (W/m^2)


# Function to calculate power generated
def calculate_power(angle):
    angle_radians = math.radians(angle)
    power = solar_panel_efficiency * solar_constant * math.cos(angle_radians)
    return power

# Create a DataFrame
df = pd.DataFrame(columns=['Angle (degrees)', 'Power (W)'])

# Calculate power for different angles
for angle in range(0, 365, 1):
    power = calculate_power(angle)
    df = df.append({'Angle (degrees)': angle, 'Power (W)': power}, ignore_index=True)

# Save the DataFrame to a spreadsheet
df.to_excel('solar_panel_power2.xlsx', index=False)
print("Spreadsheet generated successfully!")

