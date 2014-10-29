$(function(){

var chartData;
var url = "/app/data/bloodgroup-population";

/* draw pie chart */
function draw_pie_chart(){

  var chart = AmCharts.makeChart("piechart", {
    "type": "pie",
    "theme": "none",
    "dataProvider": chartData,
    "valueField": "count",
    "titleField": "bloodgroup",
    "outlineAlpha": 0.4,
    "depth3D": 15,
    "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
    "angle": 30,
  });
  chart.pathToImages = "/amcharts/images/";

}

/* draw line chart */
function draw_line_chart(){

  var chart = AmCharts.makeChart("linechart", {
    "type": "serial",
    "theme": "none",
    "dataProvider": chartData,
    "categoryField": "bloodgroup",
    "graphs": [{
      "valueField": "count"
    }],
    "chartCursor": {
      "oneBalloonOnly": true
    },
  });
  chart.pathToImages = "/amcharts/images/";

}

/* fetch data */
$.get(url, function(data){
  chartData = jQuery.parseJSON(data);
  draw_pie_chart();
  draw_line_chart();
});

});
