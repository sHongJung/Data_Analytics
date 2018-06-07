/*
 (c) 2014, Vladimir Agafonkin
 simpleheat, a tiny JavaScript library for drawing heatmaps with Canvas
 https://github.com/mourner/simpleheat
*/
!(function() {


  function t(i) {
    return this instanceof t ? (this._canvas = i = typeof i === "string" ? document.getElementById(i) : i, this._ctx = i.getContext("2d"), this._width = i.width, this._height = i.height, this._max = 1, void this.clear()) : new t(i);
  }t.prototype = { defaultRadius: 25,
    defaultGradient: { 0.4: "blue", 0.6: "cyan", 0.7: "lime", 0.8: "yellow", 1: "red" },
    data: function(t, i) {
      return this._data = t, this;
    },
    max: function(t) {
      return this._max = t, this;
    },
    add: function(t) {
      return this._data.push(t), this;
    },
    clear: function() {
      return this._data = [], this;
    },
    radius: function(t, i) {
      i = i || 15; var a = this._circle = document.createElement("canvas"),
        s = a.getContext("2d"),
        e = this._r = t + i; return a.width = a.height = 2 * e, s.shadowOffsetX = s.shadowOffsetY = 200, s.shadowBlur = i, s.shadowColor = "black", s.beginPath(), s.arc(e - 200, e - 200, t, 0, 2 * Math.PI, !0), s.closePath(), s.fill(), this;
    },
    gradient: function(t) {
      var i = document.createElement("canvas"),
        a = i.getContext("2d"),
        s = a.createLinearGradient(0, 0, 0, 256); i.width = 1, i.height = 256; for (var e in t)s.addColorStop(e, t[e]); return a.fillStyle = s, a.fillRect(0, 0, 1, 256), this._grad = a.getImageData(0, 0, 1, 256).data, this;
    },
    draw: function(t) {
      this._circle || this.radius(this.defaultRadius), this._grad || this.gradient(this.defaultGradient); var i = this._ctx; i.clearRect(0, 0, this._width, this._height); for (var a, s = 0, e = this._data.length; e > s; s++)a = this._data[s], i.globalAlpha = Math.max(a[2] / this._max, t || 0.05), i.drawImage(this._circle, a[0] - this._r, a[1] - this._r); var n = i.getImageData(0, 0, this._width, this._height); return this._colorize(n.data, this._grad), i.putImageData(n, 0, 0), this;
    },
    _colorize: function(t, i) {
      for (var a, s = 3, e = t.length; e > s; s += 4)a = 4 * t[s], a && (t[s - 3] = i[a], t[s - 2] = i[a + 1], t[s - 1] = i[a + 2]);
    } }, window.simpleheat = t;
}()), /*

/* Add GeoJSON */
$.getJSON('../basic/crimes_by_district.geojson', function (geojson) {
  L.choropleth(geojson, {
    valueProperty: function (feature) {
      return feature.properties.incidents / feature.properties.area_sqmi
    },
    scale: ['white', 'red'],
    steps: 5,
    mode: 'q',
    style: {
      color: '#fff',
      weight: 2,
      fillOpacity: 1.5
    },
    onEachFeature: function (feature, layer) {
      layer.bindPopup('District ' + feature.properties.dist_num + '<br>' +
        feature.properties.incidents.toLocaleString() + ' incidents<br>' +
        Math.round(feature.properties.area_sqmi).toLocaleString() + ' sq mi')
    }
  }).addTo(map)
})
