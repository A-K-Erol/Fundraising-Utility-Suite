
import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const REST_API_BASE_URL = "http://localhost:5000";

const TextGenComponent = () => {
  const [output, setOutput] = useState({ content: 'Your AI-generated response goes here.' });

  const [formData, setFormData] = useState({
    requestText: '',
    mode: '',
    length: '',
    platform: '',
    values: ''
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const filteredData = Object.fromEntries(
        Object.entries(formData).filter(([_, value]) => value !== '')
      );

      const response = await axios.post(REST_API_BASE_URL + "/query", filteredData);
      setOutput(response.data);
    } catch (error) {
      console.error(error);
      // Handle error if needed
    }
  };

  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit}>
        <div className="row mb-3">
          <div className="col">
            <label htmlFor="mode" className="form-label">Mode:</label>
            <select
              id="mode"
              name="mode"
              value={formData.mode}
              onChange={handleInputChange}
              className="form-select"
              placeholder="Select Mode"
            >
              <option value="">Select Mode</option>
              <option value="grants">Grants</option>
              <option value="social media">Social Media</option>
              <option value="emails">Emails</option>
            </select>
          </div>
          <div className="col">
            <label htmlFor="length" className="form-label">Length:</label>
            <input
              type="text"
              id="length"
              name="length"
              value={formData.length}
              onChange={handleInputChange}
              className="form-control"
              placeholder="Optional: word limit"
            />
          </div>
          <div className="col">
            <label htmlFor="platform" className="form-label">Platform:</label>
            <input
              type="text"
              id="platform"
              name="platform"
              value={formData.platform}
              onChange={handleInputChange}
              className="form-control"
              placeholder="Optional: platform name"
            />
          </div>
        </div>

        <div className="row mb-3">
          <div className="col">
            <label htmlFor="requestText" className="form-label">Request Text:</label>
            <textarea
              id="requestText"
              name="requestText"
              value={formData.requestText}
              onChange={handleInputChange}
              className="form-control"
              rows="5"
              placeholder="Enter the question or request here - example: What is your organization's mission?"
            />
          </div>
        </div>

        <div className="row mb-3">
          <div className="col">
            <label htmlFor="values" className="form-label">Values:</label>
            <textarea
              id="values"
              name="values"
              value={formData.values}
              onChange={handleInputChange}
              className="form-control"
              rows="2"
              style={{ width: '100%' }}
              placeholder="Optional: Any emotions, concepts like diversity and inclusion, or other values you want to include in the response."
            />
          </div>
        </div>

        <button type="submit" className="btn btn-primary" style={{ backgroundColor: '#004080' }}>Submit</button>
      </form>

      <div className="mt-4">
        <p>Output:</p>
        <div className="border p-3" style={{ width: '100%' }}>
          <p style={{ textAlign: 'left' }}>{output.content}</p>
        </div>
      </div>
    </div>
  );
};

export default TextGenComponent;