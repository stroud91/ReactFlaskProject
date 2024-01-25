import React from 'react';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

export function GoogleMapSearch({ google, businesses }) {
  const displayMarkers = () => {
    return businesses.map((business, index) => {
      return (
        <Marker key={index} id={index}
          position={{
            lat: business.latitude,
            lng: business.longitude
          }}
          onClick={() => console.log("You clicked me!")} />
      )
    })
  };

  return (
    <Map
      google={google}
      zoom={10}
      style={{ width: '100%', height: '100%' }}
      initialCenter={{
        lat: businesses[0]?.latitude,
        lng: businesses[0]?.longitude,
      }}
    >
      {displayMarkers()}
    </Map>
  );
}

export default GoogleApiWrapper({
  apiKey: (process.env.REACT_APP_GOOGLE_MAPS_API_KEY)
})(GoogleMapSearch);
