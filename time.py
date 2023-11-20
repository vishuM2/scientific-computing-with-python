def add_time(start, duration, start_day=None):
  # Parse start time
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  start_hour = start_hour % 12 + 12 if period == 'PM' else start_hour % 12

  # Parse duration time
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Calculate total minutes
  total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

  # Calculate days and remaining minutes
  days = total_minutes // (24 * 60)
  remaining_minutes = total_minutes % (24 * 60)

  # Calculate result time
  result_hour = remaining_minutes // 60
  result_minute = remaining_minutes % 60

  # Determine period (AM/PM)
  period = 'PM' if result_hour >= 12 else 'AM'

  # Format the result time
  result_time = f"{result_hour % 12 or 12}:{result_minute:02d} {period}"

  # Determine day of the week if start_day is provided
  if start_day:
    start_day = start_day.capitalize()
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    start_day_index = days_of_week.index(start_day)
    result_day_index = (start_day_index + days) % 7
    result_day = days_of_week[result_day_index]
    result_time += f", {result_day}"

  # Determine days later message
  days_later = f" ({days} days later)" if days > 0 else ""

  # Return the final result
  return result_time + days_later