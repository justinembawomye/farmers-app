import axios from 'axios';

import {GET_FARMERS, DELETE_FARMER} from './types';

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