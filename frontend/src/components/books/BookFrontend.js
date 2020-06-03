import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getBooks, deleteBook } from "../../actions/books";
import Book from "./Book";
import Detail from "../parts/Detail";

class BookList extends Component {
  state = {
    image: "",
    title: "title",
    show: [],
    loading: true,
  };
  static propTypes = {
    books: PropTypes.array.isRequired,
    deleteBook: PropTypes.func.isRequired,
  };
  componentDidMount() {
    this.props.getBooks();
  }

  changeDetails = (id) => {
    let show = this.props.books.filter((item) => item.id === id);
    this.setState({ show: show, loading: false });
  };

  render() {
    const bookList = this.props.books.map((book) => (
      <a key={book.id} className="" onClick={() => this.changeDetails(book.id)}>
        <Book book={book} />
      </a>
    ));
    return (
      <Fragment>
        <div className="vid-container">
          <div className="row ">
            <div className="col-5" id="">
              <div className="p-3" id="vidList">
                {bookList ? bookList : <h1> Loading </h1>}
              </div>
            </div>
            <div className="col-7 m-5 p-3">
              <Detail show={this.state.show} loading={this.state.loading} />
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  books: state.books.books,
});

export default connect(mapStateToProps, { getBooks, deleteBook })(BookList);
