import {GET_LEADS, DELETE_LEAD, ADD_LEAD, GET_FARMERS} from '../actions/types.js';

const initialState  = {
    farmers:[],
}

export default function(state = initialState, action){
switch(action.type){
    // case GET_LEADS:
    // return {
    //     ...state,
    //     leads:action.payload
    // };

    // case DELETE_LEAD:
    // return {
    //     ...state,
    //     leads:state.leads.filter(lead => lead.id !== action.payload)
    // };

    // case ADD_LEAD:
    // return {
    //     ...state,
    //     leads: [...state.leads]
    // };

    case GET_FARMERS:
    return {
        ...state,
        farmers:action.payload
    }

    default:
    return state;
}
}