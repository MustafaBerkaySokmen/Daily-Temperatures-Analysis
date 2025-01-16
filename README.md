# Daily Temperatures Analysis

## Overview
The **Daily Temperatures Analysis** project is a Python program designed to process and analyze daily temperature data. It provides functionalities to read temperature records from a file, calculate monthly and yearly averages, and filter data by year. The program is suitable for analyzing temperature trends across multiple years.

## Features
- **Read Temperature Data:** Parses a file containing daily temperature records.
- **Filter Data by Year:** Removes records for a specific year.
- **Calculate Monthly Averages:** Computes average temperatures for each month in a given year.
- **Calculate Yearly Averages:** Computes and saves yearly averages to an output file.

## Installation
To run this project, ensure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/daily-temperatures-analysis.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd daily-temperatures-analysis
   ```
3. **Ensure data files are available:**
   Place temperature data files (e.g., `ISTANBUL.txt`, `ANKARA.txt`) in the project directory.
4. **Run the script:**
   ```bash
   python DailyTemperatures.py
   ```

## Usage
1. The program contains the following primary functions:
   - `read_temperatures(filename)`: Reads temperature data from a file and returns it as a list of records.
   - `delete_year(data, year)`: Removes all records for the specified year.
   - `monthly_averages(data, year)`: Calculates the average temperature for each month in a given year.
   - `yearly_average(data)`: Computes yearly average temperatures and saves them to a file.
2. Modify the test cases in the `main()` function to analyze different data files or parameters.
3. Running the script prints results and generates output files as needed.

## Example Output
```
Ankara Data:
[[1, 1, 2017, 3.5], [1, 2, 2017, -1.0], ..., [12, 31, 2019, 6.2]]
Filtered Data:
[[1, 1, 2017, 3.5], [1, 2, 2017, -1.0], ..., [12, 31, 2019, 6.2]]
Monthly Averages (2017):
[4.5, 3.2, 7.8, ..., 2.9]
Yearly Averages:
Saved to `out.txt`
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

