import React from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

export function MapContainer({ google, business }) {
  console.log("THIS IS INFO PASSED FOR GOOGLE MAPS", google, business )

  const busId= business.id
  
  const mapStyles = {
    width: '400px',
    height: '400px',
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
  apiKey: 'AIzaSyCRM7INOx0mR1yvgWECwy8rGbrJEV_pBEU'
})(MapContainer);
