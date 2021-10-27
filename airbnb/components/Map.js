import { useState } from "react";
import ReactMapGL, { Marker, Popup } from "react-map-gl";
import { getCenter } from "geolib";

function Map({ searchResults }) {
  const [selectedLocation, setSelectedLocation] = useState({});

  // Transform the serach results object into the
  // { latitude: 52.516272, longtitude: 13.377722 }
  // Object

  const coordinates = searchResults.map(({ long, lat }) => ({
    longitude: long,
    latitude: lat,
  }));

  const center = getCenter(coordinates);

  const [viewport, setViewport] = useState({
    width: "100%",
    height: " 100%",
    latitude: center.latitude,
    longitude: center.longitude,
    zoom: 11,
  });

  return (
    <ReactMapGL
      mapStyle="mapbox://styles/vijayrjdev/ckv54i4006asl14qk1w6usmnm"
      mapboxApiAccessToken={process.env.mapbox_key}
      {...viewport}
      onViewportChange={(nextViewport) => setViewport(nextViewport)}
    >
      {searchResults.map((result) => (
        <div key={result.long}>
          <Marker
            longitude={result.long}
            latitude={result.lat}
            offsetLeft={-20}
            offsetTop={-20}
          >
            <p
              onClick={() => setSelectedLocation(result)}
              className=" cursor-pointer text-2xl animate-bounce"
            >
              📌
            </p>
          </Marker>

          {/* This is the popup when click on a marker */}
          {selectedLocation.long === result.long ? (
            <Popup
              onClose={() => setSelectedLocation({})}
              closeOnClick={true}
              latitude={result.lat}
              longitude={result.long}
            >
              {result.title}
            </Popup>
          ) : (
            false
          )}
        </div>
      ))}
    </ReactMapGL>
  );
}

export default Map;
