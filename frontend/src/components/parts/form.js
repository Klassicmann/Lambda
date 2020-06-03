import React, { Component } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { addBook } from '../../actions/books'

class Form extends Component {
    static propTypes = {
        addBook: PropTypes.func.isRequired
    }

    state ={
        authur: '',
        about_authur: '',
        book_title: '',
        
    }
    change = e => this.setState({ [e.target.name] : e.target.value})

    checkSubmit = e => {
        e.preventDefault()
        const {authur, about_authur,book_title} = this.state
        const book = {authur, about_authur,book_title}

        this.props.addBook(book)
    }

    render() {
      const {authur, about_authur,book_title, } = this.state
        return (
            <div>
                <div className= "card card-body mt-4 mb-4">
                    <h3> Add Book</h3>
                    <form onSubmit={this.checkSubmit} >
                    <div className="form-group">
                        <label htmlFor="authur">Authur</label>
                        <input 
                        type="text" 
                        className="form-control" 
                        name="authur" 
                        aria-describedby="emailHelp"
                         placeholder="Enter authurs name"
                          value={authur} 
                          onChange={this.change}/>

                        <small id="aHelp" className="form-text text-muted">
                            Enter authurs name as shown on the book cover
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="about_authur">About Authur</label>

                        <textarea className="form-control"  name="about_authur"  placeholder="About name" value={about_authur} onChange={this.change}></textarea>
                        <small id="aAHelp" className="form-text text-muted">
                            Provide short information about the authur of the book. Maximum 50 words
                        </small>
                    </div>
                    <div className="form-group">
                        <label htmlFor="book_title">Book Title</label>
                        <input type="text" className="form-control" name="book_title" aria-describedby="emailHelp" placeholder="About name" value={book_title} onChange={this.change}/>
                        <small id="titileHelp" className="form-text text-muted">
                           
                        </small>
                   </div>
                    {/* 
                    <div className="form-group">
                        <label htmlFor="book_type">Book Type</label>
                        <input type="text" className="form-control" name="book_type" aria-describedby="emailHelp" placeholder="About name" value={book_type} onChange={this.change}/>
                        <small id="typeHelp" className="form-text text-muted">
                            Provide short information about the authur of the book. Maximum 50 words
                        </small>
                    </div>
                    <div className="form-group">
                        <label htmlFor="level">Level</label>
                        <input type="text" className="form-control" name="level" aria-describedby="emailHelp" placeholder="About name" value={level} onChange={this.change}/>
                        <small id="levelHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="departments">Departments</label>
                        <input type="text" className="form-control" name="departments" aria-describedby="emailHelp" placeholder="About name" value={departments} onChange={this.change}/>
                        <small id="departmentsHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="price">Price</label>
                        <input type="text" className="form-control" name="price" aria-describedby="emailHelp" placeholder="About name" value={price} onChange={this.change}/>
                        <small id="priceHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="file">File</label>
                        <input type="text" className="form-control" name="file" aria-describedby="emailHelp" placeholder="About name" value={file} onChange={this.change}/>
                        <small id="fileHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="book_front_cover">Book Front Cover</label>
                        <input type="text" className="form-control" name="book_front_cover" aria-describedby="emailHelp" placeholder="About name" value={book_front_cover} onChange={this.change}/>
                        <small id="bfcHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="book_back_cover">Book Front Cover</label>
                        <input type="text" className="form-control" name="book_back_cover" aria-describedby="emailHelp" placeholder="About name" value={book_back_cover} onChange={this.change}/>
                        <small id="bbcHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="description">Description</label>
                        <input type="text" className="form-control" name="description" aria-describedby="emailHelp" placeholder="About name" value={description} onChange={this.change}/>
                        <small id="bfcHelp" className="form-text text-muted">
                            This book will be shown only to people of this shool level
                        </small>
                    </div> */}

                    <button className="btn btn-sm btn-primary" type="submit"> Submit</button>

                    </form>

                </div>

             </div>
                
          
        )
    }
}

export default connect(null, {addBook})(Form)