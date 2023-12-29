import axios from 'axios';
const REST_API_BASE_URL = "http://localhost:5000";


export const generateText = async (request) => {
    const response = await axios.post(REST_API_BASE_URL + "/query", request)
    return response.data }

export const test = () => {
    return axios.post(REST_API_BASE_URL + "/query", {'request_text': 'Who are you?', 'length':'20'})}