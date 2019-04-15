import React, { Component, Fragment } from 'react'
import {connect} from 'react-redux'
import PropTypes from 'prop-types';
import {getleads} from '../../actions/leads'

export class Leads extends Component {
  static PropTypes = {
    leads: PropTypes.array.isRequired
  };

  componentDidMount(){
    this.props.getleads();
  }
  render() {
    return (
      <div>
        <Fragment>
        <h3>All Rice Farmers</h3>
        <table className="table table-striped">
          <thead>
          <tr>
            <th>ID</th>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Gender</th>
            <th>Age</th>
            <th>Status</th>
          </tr>
          </thead>

          <tbody>
            {this.props.leads.map(lead =>(
              <tr key={lead.id}>
              <td>{lead.id}</td>
              <td>{lead.firstname}</td>
              <td>{lead.lastname}</td>
              <td>{lead.gender}</td>
              <td>{lead.age}</td>
              <td>{lead.marriage_status}</td>
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
  leads:state.Leads.leads
});
export default connect(mapStateToProps, {getleads})(Leads);
