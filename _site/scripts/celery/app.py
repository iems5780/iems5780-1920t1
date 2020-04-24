from task import generate_squares

# Use .delay to execute the Celery task asynchronously
for i in range(5):
    generate_squares.delay(10)
