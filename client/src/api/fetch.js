import axios from "axios";
import { appStates } from "../store/store";

export const sendRequest = async (method, url, data = null) => {
  try {
    const config = {
      method,
      url,
      headers: {
        "Content-Type": "application/json",
      },
      data: data ? JSON.stringify(data) : null,
    };

    const response = await axios(config);

    // Check if the request was successful
    if (response.status >= 200 && response.status < 300) {
      return response.data;
    } else {
      console.error(`Request failed with status ${response.status}`);
      return null;
    }
  } catch (error) {
    if (error) {
      appStates().showErrorMessage(error.response.data);
      console.log("Error response:", error);
    }
    return null;
  }
};

// You can create similar methods for other HTTP verbs
export const getData = async (url) => sendRequest("GET", url);
export const postData = async (url, data) => sendRequest("POST", url, data);
export const putData = async (url, data) => sendRequest("PUT", url, data);
export const deleteData = async (url) => sendRequest("DELETE", url);

// Usage examples
// const fetchData = async () => {
//     const result = await getData('http://example.com/api/data');
//     if (result) {
//       // Process the fetched data
//     } else {
//       console.error('Failed to fetch data');
//     }
// };
