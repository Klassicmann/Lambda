import { GET_BOOKS, DELETE_BOOK, ADD_BOOK } from "./types";
import Axios from "axios";

export const getBooks = () => (dispatch) => {
  Axios.get("http://127.0.0.1:8000/videos/api/videos/")
    .then((response) =>
      dispatch({
        type: GET_BOOKS,
        payload: response.data,
      })
    )
    .catch((err) => console.log(err));
};
export const deleteBook = (id) => (dispatch) => {
  Axios.delete(`http://127.0.0.1:8000/books/api/books/${id}/`, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  })
    .then((data) =>
      dispatch({
        type: DELETE_BOOK,
        payload: id,
      })
    )
    .catch((err) => console.log(err));
};

export const addBook = (book) => (dispatch) => {
  Axios.post(`http://127.0.0.1:8000/books/api/books/`, book, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  })
    .then((data) =>
      dispatch({
        type: ADD_BOOK,
        payload: book,
      })
    )
    .catch((err) => console.log(err));
};
