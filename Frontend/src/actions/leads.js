import axios from 'axios';

import {GET_LEADS} from './types';

// Get leads

export const getleads = () => dispatch => {
    axios.get('api/allfarmers')
    .then(res => {
        dispatch({
            type:GET_LEADS,
            payload: res.data
        });
    })
    .catch(err => console.log(err))
}