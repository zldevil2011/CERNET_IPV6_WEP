//$(function () {
//    $('#year_container').highcharts({
//        title: {
//            text: 'Monthly Average Temperature',
//            x: -20 //center
//        },
//        subtitle: {
//            text: 'Source: WorldClimate.com',
//            x: -20
//        },
//        xAxis: {
//            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
//        },
//        yAxis: {
//            title: {
//                text: 'Temperature (°C)'
//            },
//            plotLines: [{
//                value: 0,
//                width: 1,
//                color: '#808080'
//            }]
//        },
//        tooltip: {
//            valueSuffix: '°C'
//        },
//        legend: {
//            layout: 'vertical',
//            align: 'right',
//            verticalAlign: 'middle',
//            borderWidth: 0
//        },
//        series: [{
//            name: '地点',
//            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
//        }]
//    });
//});
//$(function () {
//    $('#month_container').highcharts({
//        chart: {
//            type: 'spline'
//        },
//        title: {
//            text: 'Monthly Temperature'
//        },
//        subtitle: {
//            text: 'Source: WorldClimate.com'
//        },
//        xAxis: {
//            categories: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
//        },
//        yAxis: {
//            title: {
//                text: 'Temperature'
//            },
//            labels: {
//                formatter: function() {
//                    return this.value +'°'
//                }
//            }
//        },
//        tooltip: {
//            crosshairs: true,
//            shared: true
//        },
//        plotOptions: {
//            spline: {
//                marker: {
//                    radius: 4,
//                    lineColor: '#666666',
//                    lineWidth: 1
//                }
//            }
//        },
//        series: [{
//            name: 'Place',
//            marker: {
//                symbol: 'diamond'
//            },
//            data: [{
//                y: 3.9,
//                marker: {
//                    symbol: 'url(/demo/img/snow.png)'
//                }
//            }, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8, 3.6,4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8,4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6]
//        }]
//    });
//});
//$(function () {
//
//    $('#real_wind').highcharts({
//
//	    chart: {
//	        type: 'gauge',
//	        plotBackgroundColor: null,
//	        plotBackgroundImage: null,
//	        plotBorderWidth: 0,
//	        plotShadow: false
//	    },
//
//	    title: {
//	        text: 'Cloud_Speed'
//	    },
//
//	    pane: {
//	        startAngle: -150,
//	        endAngle: 150,
//	        background: [{
//	            backgroundColor: {
//	                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
//	                stops: [
//	                    [0, '#FFF'],
//	                    [1, '#333']
//	                ]
//	            },
//	            borderWidth: 0,
//	            outerRadius: '109%'
//	        }, {
//	            backgroundColor: {
//	                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
//	                stops: [
//	                    [0, '#333'],
//	                    [1, '#FFF']
//	                ]
//	            },
//	            borderWidth: 1,
//	            outerRadius: '107%'
//	        }, {
//	            // default background
//	        }, {
//	            backgroundColor: '#DDD',
//	            borderWidth: 0,
//	            outerRadius: '105%',
//	            innerRadius: '103%'
//	        }]
//	    },
//
//	    // the value axis
//	    yAxis: {
//	        min: 0,
//	        max: 18,
//
//	        minorTickInterval: 'auto',
//	        minorTickWidth: 1,
//	        minorTickLength: 10,
//	        minorTickPosition: 'inside',
//	        minorTickColor: '#666',
//
//	        tickPixelInterval: 30,
//	        tickWidth: 2,
//	        tickPosition: 'inside',
//	        tickLength: 10,
//	        tickColor: '#666',
//	        labels: {
//	            step: 2,
//	            rotation: 'auto'
//	        },
//	        title: {
//	            text: 'm/s'
//	        },
//	        plotBands: [{
//	            from: 0,
//	            to: 5,
//	            color: '#55BF3B' // green
//	        }, {
//	            from: 5,
//	            to: 10,
//	            color: '#DDDF0D' // yellow
//	        }, {
//	            from: 12,
//	            to: 18,
//	            color: '#DF5353' // red
//	        }]
//	    },
//
//	    series: [{
//	        name: 'Speed',
//	        data: [4],
//	        tooltip: {
//	            valueSuffix: ' m/s'
//	        }
//	    }]
//
//	},
//	// Add some life
//	function (chart) {
//		if (!chart.renderer.forExport) {
//		    setInterval(function () {
//		        var point = chart.series[0].points[0],
//		            newVal,
//		            inc = Math.round((Math.random() - 0.5) * 20);
//
//		        newVal = point.y + inc;
//		        if (newVal < 0 || newVal > 18) {
//		            newVal = point.y - inc;
//		        }
//
//		        point.update(newVal);
//
//		    }, 3000);
//		}
//	});
//});
//$(function () {
//    $('#real_info_tem').highcharts({
//        chart: {
//            type: 'line'
//        },
//        title: {
//            text: ''
//        },
//        subtitle: {
//            text: ''
//        },
//        xAxis: {
//            categories: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
//        },
//        yAxis: {
//            title: {
//                text: 'Temperature (°C)'
//            }
//        },
//        tooltip: {
//            enabled: false,
//            formatter: function() {
//                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
//            }
//        },
//        plotOptions: {
//            line: {
//                dataLabels: {
//                    enabled: true
//                },
//                enableMouseTracking: false
//            }
//        },
//        series: [{
//            name: '整点温度',
//            data: [3.9, 4.2, 5.7, 3.5, 11.9, 13.2, 10.0, 14.6, 12.2, 10.3, 6.6, 4.8,3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8,3.5]
//        }]
//    });
//});
//$(function () {
//    $('#real_info_humidity').highcharts({
//        chart: {
//            type: 'line'
//        },
//        title: {
//            text: ''
//        },
//        subtitle: {
//            text: ''
//        },
//        xAxis: {
//            categories: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
//        },
//        yAxis: {
//            title: {
//                text: 'Temperature (°C)'
//            }
//        },
//        tooltip: {
//            enabled: false,
//            formatter: function() {
//                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
//            }
//        },
//        plotOptions: {
//            line: {
//                dataLabels: {
//                    enabled: true
//                },
//                enableMouseTracking: false
//            }
//        },
//        series: [{
//            name: '湿度',
//            data: [2.9, 4.2, 5.7, 3.5, 9.9, 13.2, 9.0, 13.6, 2.2, 8.3, 6.6, 4.8,3.9, 4.2, 5.7, 8.5, 11.9, 5.2, 7.0, 6.6, 14.2, 10.3, 6.6, 4.8,3.5]
//        }]
//    });
//});
//$(function () {
//    $('#real_info_precipitation').highcharts({
//        chart: {
//            type: 'line'
//        },
//        title: {
//            text: ''
//        },
//        subtitle: {
//            text: ''
//        },
//        xAxis: {
//            categories: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
//        },
//        yAxis: {
//            title: {
//                text: 'Temperature (°C)'
//            }
//        },
//        tooltip: {
//            enabled: false,
//            formatter: function() {
//                return '<b>'+ this.series.name +'</b><br/>'+this.x +': '+ this.y +'°C';
//            }
//        },
//        plotOptions: {
//            line: {
//                dataLabels: {
//                    enabled: true
//                },
//                enableMouseTracking: false
//            }
//        },
//        series: [{
//            name: '整点降水量',
//            data: [3.9, 4.2, 5.9, 3.5, 1.9, 8.2, 10.0, 14.6, 12.2, 3.3, 6.6, 4.8,3.9, 4.2, 5.7, 8.5, 13.9, 13.2, 13.0, 13.6, 14.2, 10.3, 6.6, 4.8,3.5]
//        }]
//    });
//});
//$(function () {
//    $('#real_info_air_quality').highcharts({
//        chart: {
//            type: 'column',
//            margin: [ 50, 50, 100, 80]
//        },
//        title: {
//            text: ''
//        },
//        xAxis: {
//            categories: [
//               0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0
//            ],
//            labels: {
//                rotation: -45,
//                align: 'right',
//                style: {
//                    fontSize: '13px',
//                    fontFamily: 'Verdana, sans-serif'
//                }
//            }
//        },
//        yAxis: {
//            min: 0,
//            title: {
//                text: 'PM2.5'
//            }
//        },
//        legend: {
//            enabled: false
//        },
//        tooltip: {
//            pointFormat: 'Population in 2008: <b>{point.y:.1f} millions</b>',
//        },
//        series: [{
//            name: 'Population',
//            data: [34.4, 21.8, 20.1, 20, 19.6, 19.5, 19.1, 18.4, 18,
//                17.3, 16.8, 15, 14.7, 14.5, 13.3, 12.8, 12.4, 11.8,
//                11.7, 11.2,34.4, 21.8, 20.1, 20, 19.6],
//            dataLabels: {
//                enabled: true,
//                rotation: -90,
//                color: '#FFFFFF',
//                align: 'right',
//                x: 4,
//                y: 10,
//                style: {
//                    fontSize: '13px',
//                    fontFamily: 'Verdana, sans-serif',
//                    textShadow: '0 0 3px black'
//                }
//            }
//        }]
//    });
//});
//$(function () {
//    $('#real_info_cloud').highcharts({
//        chart: {
//            plotBackgroundColor: null,
//            plotBorderWidth: null,
//            plotShadow: false
//        },
//        title: {
//            text: ''
//        },
//        tooltip: {
//    	    pointFormat: '{series.name}'
//        },
//        plotOptions: {
//            pie: {
//                allowPointSelect: true,
//                cursor: 'pointer',
//                dataLabels: {
//                    enabled: true,
//                    color: '#000000',
//                    connectorColor: '#000000',
//                    format: '<b>{point.name}</b>'
//                }
//            }
//        },
//        series: [{
//            type: 'pie',
//            name: 'Browser share',
//            data: [
//                ['东风',   0.042],
//                ['西北风',   0.042],
//                ['东风',   0.042],
//                ['西南风',   0.042],
//                ['东风',   0.042],
//                ['西风',   0.042],
//                ['北风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//                ['东风',   0.042],
//
//            ]
//        }]
//    });
//});
$(function(){
    try{
        var height = $("#real_windy_speed").height();
        console.log(height);
        $("#real_windy_speed").parent().height(height);
    }catch(exception){

    }

});

//index canvasjs
$(function(){
    try{
        rainfull();
        temperature();
        $("#rainfall").removeClass("active");
    }catch(exception){

    }

});

function rainfull(){
    var chart = new CanvasJS.Chart("temperature-chart", {
        backgroundColor: "rgba(6,135,147,0.5)",
        title:{
        },
          data: [{
            dataPoints: [
            { x: 10, y: 2.7, label: "1月"},
            { x: 20, y: 4.4,  label: "2月" },
            { x: 30, y: 9.9,  label: "3月"},
            { x: 40, y: 24.7,  label: "4月"},
            { x: 50, y: 37.3,  label: "5月"},
            { x: 60, y: 71.9, label: "6月"},
            { x: 70, y: 160.1,  label: "7月"},
            { x: 80, y: 138.2,  label: "8月"},
            { x: 90, y: 48.5,  label: "9月"},
            { x: 100, y: 22.8,  label: "10月"},
            { x: 110, y: 9.5,  label: "11月"},
            { x: 120, y: 1,  label: "12月"}
            ]
          }
          ]
        });
    chart.render();
}
function temperature(){
    var chart = new CanvasJS.Chart("rainfall-chart", {
        backgroundColor: "rgba(6,135,147,0.5)",
        title:{
        },
        data: [{
            type: "line",
            dataPoints: [
            { x: 10, y: 1.8 , label: "1月"},
            { x: 20, y: 5,  label: "2月" },
            { x: 30, y: 11.6,  label: "3月" },
            { x: 40, y: 20.3 ,  label: "4月"},
            { x: 50, y: 26 ,  label: "5月"},
            { x: 60, y: 30,  label: "6月" },
            { x: 70, y: 30,  label: "7月" },
            { x: 80, y: 29.7,  label: "8月" },
            { x: 90, y: 25.8,  label: "9月" },
            { x: 100, y: 19.1,  label: "10月" },
            { x: 110, y: 10.1,  label: "11月" },
            { x: 120, y: 3.7,  label: "12月" }
            ]
        }]
    });
    chart.render();
}