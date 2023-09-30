import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import businessReducer from './business'
import reviewReducer from './review'
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'
import bus_images from './images';
const rootReducer = combineReducers({
  session, 
  business: businessReducer,
  reviews: reviewReducer,
  bus_images
});

const persistConfig = {
  key: 'root',
  storage,
};


const persistedReducer = persistReducer(
  persistConfig,
  rootReducer
);


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  let store =  createStore(persistedReducer, preloadedState, enhancer);
  let persistor = persistStore(store)
  return { store , persistor}
};




export default configureStore;
