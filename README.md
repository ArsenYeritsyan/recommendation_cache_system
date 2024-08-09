Running the Application
To start the application services, run:  docker-compose up

generator: Handles the generation of random values based on input.
Generator Service: Available at http://localhost:5001/generate

invoker: Invokes multiple models and fetches results from the generator.
Invoker Service: Available at http://localhost:5002/recommend?user_id=<id>

redis: Caches the results to improve performance.


Running Tests
To run the tests, use the following command:   docker-compose up tests
This command will: Test the generator service. Test the invoker service. Verify the cache using Redis.
