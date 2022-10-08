# Assessment_fast_peacock_test
CSV file with drivers and times, calculate the average
lap time for each driver, and sort them in ascending order.

Finally, an output with the top 3 drivers by average lap time should
be generated. For each driver, include the fastest and average lap
times. 

The output is written to CSV File.

For the batch process , fast_racer.py can be scheduled in Airflow scheduler/any scheduler to run at a desired point of time.
In Airflow scheduler, this can be scheduled using Python operator in the DAG.
