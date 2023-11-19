import React from 'react';
import { Map, Marker, GoogleApiWrapper} from 'google-maps-react';

const API_KEY = process.env.REACT_APP_GOOGLE_MAPS_API_KEY



export function MapContainer({ google, business }) {


  const busId= business.id

  const mapStyles = {
    width: '300px',
    height: '240px',
  };

  return (
    <Map
      google={google}
      zoom={14}
      style={mapStyles}
      key={busId}
      initialCenter={{ lat: business.latitude, lng: business.longitude }}
    >
      <Marker position={{ lat: business.latitude, lng: business.longitude }} />
    </Map>
  );
}

export default GoogleApiWrapper({
  apiKey: API_KEY
})(MapContainer);
