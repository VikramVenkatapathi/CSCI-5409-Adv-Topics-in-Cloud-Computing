import bcryptjs from 'bcryptjs';
import axios from 'axios';

export const handler = async (event, context) => {
  try {
    // Retrieve the input data from the event
    const value = event.value;
    const course_uri = event.course_uri;

    // Perform Bcrypt hashing
    const hashed_value = bcryptjs.hashSync(value, 12); 

    // Prepare the response
    const response = {
      banner: "B00936916",
      result: hashed_value,
      arn: context.invokedFunctionArn,
      action: 'bcrypt',
      value: value
    };

    // Send the response to the course_uri using axios
    const axiosConfig = {
      headers: {
        'Content-Type': 'application/json'
      }
    };

    axios.post(course_uri, response, axiosConfig);

    return response; // Return the response as-is
  } catch (error) {
    // Handle any potential errors
    return {
      statusCode: 400,
      body: { error: error.message }
    };
  }
};
