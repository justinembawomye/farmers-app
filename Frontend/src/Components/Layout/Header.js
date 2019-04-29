import { HashRouter as Router, Route, Link, Switch } from "react-router-dom";

import React, { Component, Fragment } from "react";
import Farmers from "../Farmer";
import FarmerForm from "../AddFarmer";


class Navbar extends Component {
  render() {
    return (
      <Router>
        <Fragment>
          <nav className="navbar navbar-default navbar-static-top right">
            <ul className="nav nav-pills right">
              <li>
                <Link to="/" className="active">
                  Farmers
                </Link>
              </li>
              <li>
                <Link to="/add-farmer" className="active">
                  Add farmer
                </Link>
              </li>
            </ul>
          </nav>

          <Switch>
            <Route path="/" component={Farmers} exact />
            <Route path="/add-farmer" component={FarmerForm} />
          </Switch>
        </Fragment>
      </Router>
    );
  }
}
export default Navbar;
