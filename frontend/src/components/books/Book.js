import React, { Component } from "react";

export class Book extends Component {
  render() {
    const { book } = this.props;
    return (
      <div>
        <h3 className="p-4">{book.title}</h3>
      </div>
    );
  }
}

export default Book;
