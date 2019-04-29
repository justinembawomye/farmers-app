import React, { Component, Fragment } from 'react'
import {connect} from 'react-redux'
import PropTypes from 'prop-types';
import {getfarmers, deletefarmer} from "../actions/farmer";


export class Farmers extends Component {
  static PropTypes = {
    farmers: PropTypes.array.isRequired,
    getfarmers:PropTypes.func.isRequired,
    deletefarmer:PropTypes.func.isRequired
  };

  componentDidMount(){
    this.props.getfarmers();
  }
  render() {
    return (
      <div>
        <Fragment>
        <h3>All Farmers</h3>
        <table className="table table-striped">
          <thead>
          <tr>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Gender</th>
            <th>Age</th>
            <th>Status</th>
          </tr>
          </thead>

          <tbody>
            {this.props.farmers.map(farmer =>(
              <tr key={farmer.id}>
              <td>{farmer.id}</td>
              <td>{farmer.firstname}</td>
              <td>{farmer.lastname}</td>
              <td>{farmer.gender}</td>
              <td>{farmer.age}</td>
              <td>{farmer.marriage_status}</td>
              <td><button className='btn btn-danger btn-sm'onClick={this.props.deletefarmer.bind(this, farmer.id)}>Del</button></td>
              </tr>
            ))}
          </tbody>
        </table>
        </Fragment>
      
      </div>
    )
  }
}
const mapStateToProps = state =>({
  farmers:state.Farmers.farmers
});
export default connect(mapStateToProps, {getfarmers, deletefarmer})(Farmers);
