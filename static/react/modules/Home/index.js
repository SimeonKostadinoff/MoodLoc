import React, {Component} from "react"
import { render } from "react-dom"
import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers,
} from "redux"
import { Provider } from "react-redux"
import thunk from "redux-thunk"


import * as reducers from "./reducers/index"

import HomeContainer from './containers/HomeContainer';

let finalCreateStore = compose(
  applyMiddleware(thunk),
  window.devToolsExtension ? window.devToolsExtension() : f => f
)(createStore)
let reducer = combineReducers(reducers)
let store = finalCreateStore(reducer)

class Home extends Component {
  render() {
    return (
      <Provider store={store}>
        <HomeContainer />
      </Provider>
    )
  }
}

render(<Home/>, document.getElementById('home'))