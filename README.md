# Sales Scheduler
This will be used by audiance to book available slots. The available slots will be calculated based on the minimum appointment taken by a sales person among group of registered sales reps.

# Requirements
Schedule an incoming stream of call requests with different connected google calendars based on the availability of the calendar for the requested slot. Optimize for equal number of calls across different calendars per day.

# More Details
What is expected - A webpage to do the following A google oAuth integration (using a dummy app), for user to connect his calendars. A form to allow user to define his availability per day. (User can choose multiple blocks of time per day). The form should also allow user to define his timezone. All calls requests are 30 mins each. Only consider user's primary calendar for call bookings. Also multiple users can connect their calendars and hence this will need some form of database support. Another webpage where a call request (start time of the call) can be defined along with the timezone. (You might want to preload all available slots for a day and let user pick one). On submit, the request should be matched with the relevant calendar. The page should list all bookings made till then. i.e list of call request ids along with the calendars they are booked to.

# Help
Write to me at saketbairoliya2@gmail.com for any other help with project.
