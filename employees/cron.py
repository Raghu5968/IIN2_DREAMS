from croniter import croniter
import datetime

# Define a cron expression (every day at 2:30 PM)
cron_expression = "30 09 * * *"

# Create a cron iterator
cron = croniter(cron_expression)

# Get the next 5 scheduled run times
for _ in range(5):
    next_run_time = cron.get_next(datetime.datetime)
    print(next_run_time)