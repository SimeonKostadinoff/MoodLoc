import {
  default as React,
  Component,
} from "react";

import { render } from 'react-dom';

import {
  withGoogleMap,
  GoogleMap,
    Marker
} from "react-google-maps";

/*
 * Sample From: https://developers.google.com/maps/documentation/javascript/examples/map-simple
 */
const SimpleMapExampleGoogleMap = withGoogleMap(props => (
  <GoogleMap
    defaultZoom={6}
    defaultCenter={{ lat: 53.690201, lng: -1.757813 }}
  >
      {props.data.map((lat, lng, search, percentage, index) =>
      <Marker position={new google.maps.LatLng(lat, lng)} icon={'https://thumb.ibb.co/nAjjfa/8m_OKjql_Imgur.png'} opacity={percentage} key={index}/>
    )}
  </GoogleMap>
));

/* icon={'https://thumb.ibb.co/nAjjfa/8m_OKjql_Imgur.png'}
 * Add <script src="https://maps.googleapis.com/maps/api/js"></script> to your HTML to provide google.maps reference
 */
export default class MapComponent extends Component {
    constructor(props){
        super(props)
    }
  render() {
    return (
      <SimpleMapExampleGoogleMap
        containerElement={
          <div style={{ height: `100%` }} />
        }
        mapElement={
          <div style={{ height: `100%` }} />
        }
        data={this.props.data}
      />
    );
  }
}