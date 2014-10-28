$(function(){

var chartData;
var url = "/app/data/bloodgroup-population";

/* draw chart */
function draw_chart(){

  var chart = AmCharts.makeChart("chartdiv", {
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

/* fetch data */
$.get(url, function(data){
  chartData = jQuery.parseJSON(data);
  draw_chart();
});

});
