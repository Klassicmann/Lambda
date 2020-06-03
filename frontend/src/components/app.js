import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Form from "./parts/form";
import BookList from "./books/BookFrontend";
import { Provider } from "react-redux";
import store from "./store";
import Navbar from "./Navbar";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Navbar />
          <div className="p-3">
            <BookList />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
