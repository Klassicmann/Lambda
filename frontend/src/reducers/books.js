import { GET_BOOKS, DELETE_BOOK, ADD_BOOK } from "../actions/types";

const initialState = {
  books: [],
};
export default function (state = initialState, { type, payload }) {
  switch (type) {
    case GET_BOOKS:
      return {
        ...state,
        books: payload,
      };
    case DELETE_BOOK:
      return {
        ...state,
        books: state.books.filter((book) => book.id !== payload),
      };
    case ADD_BOOK:
      return {
        ...state,
        books: [...state.books, payload],
      };
    default:
      return state;
  }
}
