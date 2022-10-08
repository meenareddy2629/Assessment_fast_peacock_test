# Program description: Read racer_info CSV file with drivers and times, calculate the average lap time for each
# driver, and sort them in ascending order. Finally, generate an output  CSV file with the top 3 drivers by average
# lap time and fastest lap time.


# Import modules
import pandas as pd


def read_write_to_csv():
    # Assigning column names , reading file and assigning to a dataframe
    df = pd.read_csv(input_filename, names=['player', 'time'])
    print(df)
    #  dropping null values in any of the columns
    df2 = df.dropna()
    # Finding Average lap time of the player
    grouped_df = df2.groupby(['player']).mean()
    # Finding the minimum lap time of the player and adding the minimum time column.
    grouped_df['min_time'] = df.groupby(['player']).min()
    # Listing only the top 3 Players
    top3 = grouped_df.sort_values(['time']).head(3)
    # print(top3)
    top3.to_csv(output_filename)
    return top3


if __name__ == "__main__":
    # File name declaration
    input_filename = 'racer_info.csv'
    output_filename = 'fast_racer_list.csv'
    print("Reading racer info file from file:" + input_filename)
    try:
        top3_players_df = read_write_to_csv()
        print("Top3 Players list with avg lap time and minimum lap time:")
        print(top3_players_df)
    except Exception as e:
        print(repr(e))

