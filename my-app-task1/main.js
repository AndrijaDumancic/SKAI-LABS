import './style.css';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector.js';
import OSM from 'ol/source/OSM';
import Feature from 'ol/Feature.js';
import Polygon from 'ol/geom/Polygon.js';
import VectorSource from 'ol/source/Vector.js';

import { fromLonLat } from 'ol/proj';
import { getCenter } from 'ol/extent';


(async () => {
  try {
    // Fetching polygon coordinates from JSON file
    const response = await fetch('./data/polygon.json');
    const data = await response.json();

    // Extracting polygon coordinates from the fetched data
    const polygonCoordinates = data.polygon;

    // Creating an array to store polygon coordinates
    const coordinates = [];

    // Iterating through the coordinates and converting them to OpenLayers format
    polygonCoordinates.forEach(coordinate => {
      coordinates.push(fromLonLat(coordinate));
    });

    // Creating a polygon feature
    const polygonFeature = new Feature({
      geometry: new Polygon([coordinates])
    });

    // Creating a source and layer for the polygon
    const vectorSource = new VectorSource({
      features: [polygonFeature]
    });

    const vectorLayer = new VectorLayer({
      source: vectorSource
    });

    // Creating the map centered on the polygon
    const map = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new OSM()
        }),
        vectorLayer
      ],
      view: new View({
        center: getCenter(polygonFeature.getGeometry().getExtent()),
        zoom: 8.5
      })
    });
  } catch (error) {
    console.error('Error:', error);
  }
})();



