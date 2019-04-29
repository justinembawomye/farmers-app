import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addfarmer } from "../actions/farmer";

export class FarmerForm extends Component {
  state = {
    username: "",
    email:"",
    village:""
  };

  static PropTypes = {
    addfarmer: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: [e.target.value] });

  onSubmit = e => {
    e.preventDefault();
  
    const { username, email, village } = this.state;

    const farmer = {
      username,
      email,
      village
    };
    this.props.addfarmer(farmer);
  };

  render() {
    const { username, email, village } = this.state;
    return (
      <div className="card card-body container farmers-container">
        <h1>Add Farmer</h1>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>username</label>
            <input
              type="text"
              name="username"
              onChange={this.onChange}
              value={username}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>email</label>
            <input
              type="text"
              name="email"
              onChange={this.onChange}
              value={email}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>village</label>
            <input
              type="text"
              name="village"
              onChange={this.onChange}
              value={village}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <button className="btn btn-info" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  null,
  { addfarmer }
)(FarmerForm);
