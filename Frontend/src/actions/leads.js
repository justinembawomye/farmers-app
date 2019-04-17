import axios from 'axios';

import {GET_LEADS, DELETE_LEAD, ADD_LEAD} from './types';

// Get leads

export const getleads = (lead) => dispatch => {
    axios.get('api/farmers', lead)
    .then(res => {
        dispatch({
            type:GET_LEADS,
            payload: res.data
        });
    })
    .catch(err => console.log(err))
}


// Delete leads

export const deletelead = (id) => dispatch => {
    axios.delete(`api/farmers/${id}`)
    .then(res => {
        dispatch({
            type:DELETE_LEAD,
            payload:id
        });
    })
    .catch(err => console.log(err))
}



// add farmer

export const addlead = () => dispatch => {
    axios.post('api/add-farmer')
    .then(res => {
        dispatch({
            type:ADD_LEAD,
            payload: res.data
        });
    })
    .catch(err => console.log(err))
}

