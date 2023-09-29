// Action Types
const SET_BUSINESS = "business/SET_BUSINESS";
const REMOVE_BUSINESS = "business/REMOVE_BUSINESS";
const SET_ALL_BUSINESSES = "business/SET_ALL_BUSINESSES";
const SET_ONE_BUSINESS = "business/SET_ONE_BUSINESS";
const UPDATE_BUSINESS = "business/UPDATE_BUSINESS";
const ADD_BUSINESS = "business/ADD_BUSINESS";
const SEARCH_BUSINESS = "business/search";
// Initial State

// Action Creators
export const setBusiness = (business) => ({
  type: SET_BUSINESS,
  payload: business,
});

export const removeAllBusinesses = () => ({
  type: REMOVE_BUSINESS,
});

export const setAllBusinesses = (businesses) => ({
  type: SET_ALL_BUSINESSES,
  payload: businesses,
});

export const setOneBusiness = (business) => ({
  type: SET_ONE_BUSINESS,
  payload: business,
});

export const addBusiness = (business) => ({
  type: ADD_BUSINESS,
  payload: business,
});

export const updateBusiness = (business) => ({
  type: UPDATE_BUSINESS,
  payload: business,
});

export const searchBusiness = (search) => ({
  type: SEARCH_BUSINESS,
  payload: search,
});

// Thunks
export const searchBusinessByName = (search) => async (dispatch) => {
  const response = await fetch(`api/business/search`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ search }),
  });
  if (response.ok) {
    const results = await response.json();
    console.log("YOOOO SEARCH THUNK ", results);
    dispatch(searchBusiness(results));
  } else {
    const errorData = await response.json();
    return errorData;
  }
};

export const getBusiness = (id) => async (dispatch) => {
  const response = await fetch(`/api/business/${id}`);
  if (response.ok) {
    const data = await response.json();
    dispatch(setBusiness(data));
  } else {
    console.error("Thunk Error: Bad Req");
  }
};

export const getAllBusinesses = () => async (dispatch) => {
  const response = await fetch(`/api/business`);
  console.log("response", response);
  if (response.ok) {
    const data = await response.json();
    console.log("data", data);
    dispatch(setAllBusinesses(data));
  } else {
    console.error("Thunk Error: Bad Req");
  }
};

export const createNewBusiness = (business) => async (dispatch) => {
  console.log("This is the create Bussiness:", business);
  const response = await fetch(`/api/business/new-business`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(business),
  });

  if (response.ok) {
    const data = await response.json();
    console.log("This is the data:", data);
    dispatch(addBusiness(data));
    return data;
  } else {
    console.error("Thunk Error: Failed to add business");
  }
};

export const fetchOneBusiness = (id) => async (dispatch) => {
  const response = await fetch(`/api/business/${id}`);
  if (response.ok) {
    const business = await response.json();
    dispatch(setOneBusiness(business));
  } else {
    const errorData = await response.json();
    console.error("Thunk Error: Failed to add business", errorData);
  }
};

export const editBusiness = (id, updatedBusiness) => async (dispatch) => {
  const response = await fetch(`/api/business/${id}/edit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updatedBusiness),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(updateBusiness(data));
  } else {
    console.error("Thunk Error: Failed to edit business");
  }
};

const initialState = {
  list: [],
  current: null,
  selectedBusiness: null,
  search: null
};

// Reducer
const businessReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_ALL_BUSINESSES:
      return {
        ...state,
        list: action.payload,
      };
    case SEARCH_BUSINESS:
      return {
        ...state,
        search: action.payload,
      };
    case SET_BUSINESS:
      return { ...state, current: action.payload };
    case SET_ONE_BUSINESS:
      return { ...state, selectedBusiness: action.payload };
    case REMOVE_BUSINESS:
      return { ...state, current: null, selectedBusiness: null };
    case ADD_BUSINESS:
      return { ...state, list: [...state.list, action.payload] };
    case UPDATE_BUSINESS:
      return {
        ...state,
        list: state.list.map((business) =>
          business.id === action.payload.id ? action.payload : business
        ),
        current:
          action.payload.id === state.current.id
            ? action.payload
            : state.current,
      };
    default:
      return state;
  }
};

export default businessReducer;
