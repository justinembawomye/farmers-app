import React, { Component, Fragment } from "react";
import Navbar from "./Components/Layout/Header";
import Dashboard from "./Components/Dashboard";
import 'bootstrap/dist/css/bootstrap.css';
import "./styles.css";
import { Provider } from "react-redux";
import store from "./store";

class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Navbar />
          <div className="container">
            <Dashboard />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

export default App;
