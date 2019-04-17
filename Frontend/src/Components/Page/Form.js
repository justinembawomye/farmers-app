import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addlead } from "../../actions/leads";

export class Form extends Component {
  state = {
    firstname: "",
    lastname: "",
    age: "",
    marriage_status: "",
    telephone: "",
    image: "",
    gender: "",
    village: "",
    community_status: "",
    instructor_possibility: "",
    farm_area: "",
    crop_type: "",
    past_harvests: "",
    latitude: "",
    longitude: "",
    officer: ""
  };

  static PropTypes = {
    addlead: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: [e.target.value] });

  onSubmit = e => {
    e.preventDefault();
    const {
      firstname,
      lastname,
      age,
      marriage_status,
      telephone,
      image,
      gender,
      village,
      community_status,
      instructor_possibility,
      farm_area,
      crop_type,
      past_harvests,
      latitude,
      longitude
    } = this.state;

    const lead = {
      firstname,
      lastname,
      age,
      marriage_status,
      telephone,
      image,
      gender,
      village,
      community_status,
      instructor_possibility,
      farm_area,
      crop_type,
      past_harvests,
      latitude,
      longitude
    };
    this.props.addlead(lead);
  };

  render() {
    const {
      firstname,
      lastname,
      age,
      marriage_status,
      telephone,
      image,
      gender,
      village,
      community_status,
      instructor_possibility,
      farm_area,
      crop_type,
      past_harvests,
      latitude,
      longitude
    } = this.state;
    return (
      <div className="card card-body">
        <h1>Add Farmer</h1>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>first name</label>
            <input
              type="text"
              name="firstname"
              onChange={this.onChange}
              value={firstname}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>last name</label>
            <input
              type="text"
              name="lastname"
              onChange={this.onChange}
              value={lastname}
              className="form-control"
            />
          </div>
          <div className="form-group">
            <label>age</label>
            <input
              type="text"
              name="age"
              onChange={this.onChange}
              value={age}
              className="form-control"
            />
          </div>

                 <div className="form-group">
            <label>marriage status</label>
            <input
              type="text"
              name="marriage_status"
              onChange={this.onChange}
              value={marriage_status}
              className="form-control"
            />
          </div>


          <div className="form-group">
            <label>Telephone</label>
            <input
              type="text"
              name="telephone"
              onChange={this.onChange}
              value={telephone}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>Choose photo</label>
            <input
              type="file"
              id="myFile"
              onChange={this.onChange}
              value={image}
              name="image"
            />
          </div>

               <div className="form-group">
            <label>Gender</label>
            <input
              type="text"
              name="gender"
              onChange={this.onChange}
              value={gender}
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
            <label>community_status</label>
            <input
              type="text"
              name="community_status"
              onChange={this.onChange}
              value={community_status}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>Instructor possibility</label>
            <input
              type="checkbox"
              name="instructor_possibility"
              value={instructor_possibility}
            />{" "}
          </div>

          <div className="form-group">
            <label>Farm area</label>
            <input
              type="text"
              name="farm_area"
              onChange={this.onChange}
              value={farm_area}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>Crop type</label>
            <input
              type="text"
              name="crop_type"
              onChange={this.onChange}
              value={crop_type}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>past harvests</label>
            <input
              type="text"
              name="past_harvests"
              onChange={this.onChange}
              value={past_harvests}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>latitude</label>
            <input
              type="text"
              name="latitude"
              onChange={this.onChange}
              value={latitude}
              className="form-control"
            />
          </div>

          <div className="form-group">
            <label>longitude</label>
            <input
              type="text"
              name="longitude"
              onChange={this.onChange}
              value={longitude}
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
  { addlead }
)(Form);
