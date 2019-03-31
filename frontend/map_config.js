/*
 * Re-render the map with the provided country highlighted.
 * Expects a two character acronym (ISO 3166 alpha2)
 */
function setActiveCountry(map, country) {
  map.dataProvider.areas = [
    {
      id: country,
      showAsSelected: true
    }
  ];
  // maintain the zoom status on refresh
  map.dataProvider.zoomLevel = map.zoomLevel();
  map.dataProvider.zoomLatitude = map.dataProvider.zoomLatitudeC = map.zoomLatitude();
  map.dataProvider.zoomLongitude = map.dataProvider.zoomLongitudeC = map.zoomLongitude();

  // refresh the map to use the new country
  map.validateData();
}

/*
 * Renders AmCharts map on the element specified by divName.
 * Returns the map object for future adjustments.
 */
function createMap(divName) {
  return AmCharts.makeChart(divName, {
    type: "map",
    theme: "dark",
    projection: "mercator",
    panEventsEnabled: true,
    backgroundColor: "#535364",
    backgroundAlpha: 1,
    zoomControl: {
      zoomControlEnabled: true
    },
    dataProvider: {
      map: "worldHigh",
      getAreasFromMap: true,
      areas: []
    },
    areasSettings: {
      autoZoom: true,
      color: "#B4B4B7",
      colorSolid: "#84ADE9",
      selectedColor: "#84ADE9",
      outlineColor: "#666666",
      rollOverColor: "#9EC2F7",
      rollOverOutlineColor: "#000000"
    }
  });
}
