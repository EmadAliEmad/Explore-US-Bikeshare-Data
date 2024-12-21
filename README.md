# Explore-US-Bikeshare-Data

## Project Description

This project utilizes Python to analyze bike share data for three major US cities: Chicago, New York City, and Washington D.C. The primary goal is to provide insights into bike share usage patterns by computing descriptive statistics. Additionally, the project includes a script that allows users to interact with the data via a terminal interface.

The script allows users to filter data by city, month, and day of the week, then presents key statistics about the data, including:

*   **Time Statistics:** Most common month, day of the week, and start hour.
*   **Station Statistics:** Most commonly used start and end stations, along with the most frequent combination of start and end stations.
*   **Trip Duration Statistics:** Total travel time and mean travel time.
*   **User Statistics:** Counts of user types, gender breakdown (when available), and birth year data.

Finally, the script also provides the option to display a subset of the raw data, allowing the user to explore the data directly.

## Files in this Repository

*   **`.idea`:** Folder containing IntelliJ IDEA project settings (can be ignored).
*   **`_MACOSX`:** Folder containing macOS specific files (can be ignored).
*   **`README.md`:** This file, providing an overview of the project.
*   **`bikeshare_2.py`:** The main Python script containing the data analysis logic.
*   **`chicago.csv`:** Dataset for Chicago bikeshare data.
*   **`new_york_city.csv`:** Dataset for New York City bikeshare data.
*   **`washington.csv`:** Dataset for Washington D.C. bikeshare data.

## How to Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/EmadAliEmad/Explore-US-Bikeshare-Data.git
    cd Explore-US-Bikeshare-Data
    ```

2.  **Ensure You Have Python Installed:** This project requires Python 3.6 or higher.

3.  **Install Required Libraries:**
    ```bash
    pip install pandas numpy
    ```

4.  **Run the Script:**
    ```bash
    python bikeshare_2.py
    ```
5.  **Follow the Prompts:** The script will guide you through selecting the city, month, and day of the week for analysis.  It will then present the results in the terminal. You'll have an option to view raw data, and also to restart the whole analysis again, and pick a new selection of data.

## Project Logic Overview

The `bikeshare_2.py` script consists of the following key functions:

*   **`get_filters()`**: Obtains the user inputs for filtering the data based on the selected city, month, and day. It uses a while loop to handle invalid inputs.
*   **`load_data(city, month, day)`**: Loads the specified city's data and filters it according to the user's specified month and day (if any).
*   **`time_stats(df)`**: Calculates and displays the most frequent times of travel (most common month, day of week, start hour).
*   **`station_stats(df)`**:  Calculates and displays the most popular stations and trips (most common start station, end station, and combination of both).
*  **`trip_duration_stats(df)`**: Calculates and displays statistics on the total and average trip duration.
*   **`user_stats(df, city)`**: Calculates and displays statistics on bikeshare users (counts of user types, gender, and birth year data when available, except for Washington).
*    **`display_data(df)`**: Allows user to view the raw data. It iterates through the filtered data in sets of 5 rows each, giving the user the option to view additional rows.
*   **`main()`**: The main function of the script that organizes all previous functions and prompts user to restart or exit the analysis.

## Data Source

The data for this project is stored in the following CSV files:
    * `chicago.csv`: Bike share data for the city of Chicago.
    * `new_york_city.csv`: Bike share data for the city of New York.
    * `washington.csv`: Bike share data for the city of Washington.
These files should be in the same directory as the `bikeshare_2.py` script.

## Dependencies

*   **Python 3.6 or higher**
*   **Pandas:** For data manipulation and analysis.
*   **NumPy:** For numerical calculations.

## Potential Improvements

*   Implement better user input validation.
*   Expand analysis to include more granular data breakdowns.
*   Add a graphical user interface (GUI) for improved user experience.
*   Incorporate data visualization to aid in presenting the analysis findings.
*   Add some basic error handling.
*   Add some additional details in the README file, regarding how to run the project.
*   Add more documentation regarding code in the `bikeshare_2.py` file.
*   Add additional filters to data.

## License

This project is open source and available for use under the MIT License.

## Author

*   **Emad Ali Emad**
    [GitHub Profile](https://github.com/EmadAliEmad)
