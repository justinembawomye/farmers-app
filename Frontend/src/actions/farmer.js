import axios from 'axios';

import {GET_FARMERS, DELETE_FARMER, ADD_FARMER} from './types';

// Get farmers

export const getfarmers = (farmer) => dispatch => {
    axios.get('api/farmers', farmer)
    .then(res => {
        dispatch({
            type:GET_FARMERS,
            payload: res.data
        });
    })
    .catch(err => console.log(err))
}


export const deletefarmer = (id) => dispatch => {
    axios.delete(`api/farmers/${id}`)
    .then(res => {
        dispatch({
            type:DELETE_FARMER,
            payload:id
        });
    })
    .catch(err => console.log(err))
}




export const addfarmer = postData => dispatch => {
    fetch('api/farmers', {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "X-CSRFToken":"gfgbjkfgjegjjgkegjkkogeipogoip"
      },
      body: JSON.stringify(postData)
    })
      .then(res => res.json())
      .then(post =>
        dispatch({
          type: ADD_FARMER,
          payload: post
        })
      );
  };