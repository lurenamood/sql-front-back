import { useState } from "react";
import axios from "axios";

export const useAxios = (basePath = "http://localhost:8000/") => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const get = async (path = "", config = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`${basePath}${path}`, config);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const post = async (path = "", data = {}, config = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${basePath}${path}`, data, config);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const put = async (path = "", data = {}, config = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.put(`${basePath}${path}`, data, config);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const del = async (path = "", config = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.delete(`${basePath}${path}`, config);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { get, post, put, del, loading, error };
};
