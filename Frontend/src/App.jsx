import React, { Component, Fragment } from "react";
import Header from "./Components/Layout/Header";
import Dashboard from "./Components/Page/Dashboard";
import "./styles.css";
import { Provider } from "react-redux";
import store from "./store";
import 'bootstrap/dist/css/bootstrap.css'

class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="container">
            <Dashboard />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

export default App;
