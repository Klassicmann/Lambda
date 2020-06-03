import React, { Component, Fragment } from 'react'
import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import { getBooks, deleteBook } from '../../actions/books'


class BookList extends Component {
    static propTypes ={
        books: PropTypes.array.isRequired,
        deleteBook: PropTypes.func.isRequired
    }
    componentDidMount(){
        this.props.getBooks()
    }
    render() {
        return (
            <Fragment>
                <h4>Book List</h4>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Title</th>
                            <th>Authur</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.books.map(book => (
                            <tr key={book.id}>
                                <td>{book.id}</td>
                                <td>{book.book_title}</td>
                                <td>{book.authur}</td>
                                <td>
                                    <button className="btn btn-danger btn-sm" onClick={this.props.deleteBook.bind(this, book.id)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state =>({
    books: state.books.books
})

export default connect(mapStateToProps, {getBooks, deleteBook})(BookList)
