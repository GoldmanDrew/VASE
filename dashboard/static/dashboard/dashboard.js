
    var price_data = {};
    var dates = new Set();
    for (price in all_prices) {
      curr_date = all_prices[price]["fields"]["Time"];
      var curr_name = all_prices[price]["fields"]["Token"];
      var curr_price = all_prices[price]["fields"]["Price"];
      if (curr_date in price_data) {
        price_data[curr_date].push({ "series": curr_name, "y": curr_price });
      }
      else {
        price_data[curr_date] = [{ "series": curr_name, "y": curr_price }];
      }
    }

    var fakedata = [];
    for (var token in price_data) {
      obj = price_data[token]
      obj.sort(function (a, b) {
        var textA = a.series.toUpperCase();
        var textB = b.series.toUpperCase();
        return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
      })

      var newarr = [new Date(token)]
      for (var i = 0; i < obj.length; i++) {
        newarr.push(obj[i].y)
      }
      fakedata.push(newarr)
    }

    g = new Dygraph(
      document.getElementById("graphdiv"),
      fakedata,
      {
        rollPeriod: 2,
        showRoller: false,  //TODO: make these labels automatically
        labels: ["Date", "Token 0", "Token 1", "Token 2", "Token 3", "Token 4",
          "Token 5", "Token 6", "Token 7", "Token 8", "Token 9"],
        labelsDiv: document.getElementById("labels"),
        // ylabel: "Price",
        highlightCircleSize: 0,
        strokeWidth: 2,
        strokeBorderWidth: 0,
        drawGapEdgePoints: true,
        connectSeparatedPoints: true,
        showRangeSelector: true,
        // hideOverlayOnMouseOut: false,
        legend: "always",
        legendFormatter: legendFormatter,
        highlightSeriesBackgroundAlpha: 0.33,
        highlightSeriesBackgroundColor: "rgb(40, 75, 99)",
        // eventually want dateWindow, which initially zooms to a specific time (ex: earliest/latest day)
        highlightSeriesOpts: {
          strokeWidth: 3,
          strokeBorderWidth: 0,
          highlightCircleSize: 5
        },
        rangeSelectorBackgroundLineWidth: 2,
        rangeSelectorForegroundLineWidth: 2,
        rangeSelectorHeight: 70,
        rangeSelectorPlotFillColor: "black",
        rangeSelectorPlotFillGradientColor: "",
        rangeSelectorPlotLineWidth: 3,
        rangeSelectorPlotStrokeColor: "red"

      }
    );

    window.intervalId = setInterval(function () {
      var x = new Date();  // current time
      var y = Math.random();
      data.push([x, y]);
      g.updateOptions({ 'file': data });
    }, 1000);

    var onclick = function (ev) {
      if (g.isSeriesLocked()) {
        g.clearSelection();
      } else {
        g.setSelection(g.getSelection(), g.getHighlightSeries(), true);
      }
    };

    function showtoken(el) {
      g.setVisibility(el.id, el.checked);
    }

    function legendFormatter(data) {
      if (data.x == null) {
        // This happens when there's no selection
        return '<br>' + data.series.map(function (series) {
          var labeldata = `<span style="color: ${series.color}; font-weight: bold">` + series.labelHTML + '</span>';
          return series.dashHTML + ' ' + labeldata
        }).join('<br>');
        // return ''
      }
      var html = '<br><b>' + this.getLabels()[0] + '</b>' + ': ' + data.xHTML;
      data.series.forEach(function (series) {
        if (!series.isVisible) return;
        var labeledData = `<span style="color: ${series.color}; font-weight: bold">` + series.labelHTML + '</span>' + ': ' + series.yHTML;
        if (series.isHighlighted) {
          labeledData = '<mark><b>' + labeledData + '</b></mark>';
        }
        html += '<br>' + series.dashHTML + ' ' + labeledData;
      });
      return html;
    }


// Chart.defaults.global.defaultFontColor = '#ce796b'


// document.getElementById('checkbox-list').setAttribute("style","height:"+(document.getElementById('all_chart').offsetHeight-20));
// window.onresize = resize_scroll;
// function resize_scroll(e) {
//   document.getElementById('checkbox-list').setAttribute("style","height:"+(document.getElementById('all_chart').offsetHeight-20));;
// }

// // $('#class-modal').on('shown.bs.modal', function (event) {
// //   var button = event.relatedTarget;
// //   var button_id = button.id;
// //   var components = button_id.split("_");
// //   var classname = components[0];
// //   var buy_sell = components[1];
// //   document.getElementById("modal-label").innerHTML = classname;
// //   document.getElementById("buy-sell-label").innerHTML = "Quantity to " + buy_sell;
// //   $.ajax({
// //     type:"GET",
// //     url: "/dashboard/get_prices",
// //     data:{"class":classname},
// //     dataType: 'json',
// //     success: function(data){
// //       var ctx = document.getElementById('myChart').getContext('2d');
// //       var graph_data = [];
// //       var time = [];
// //       for(price in data){
// //         var curr_date = new Date(data[price]["fields"]["Time"]);
// //         var curr_price = data[price]["fields"]["Price"];
// //         time.push(curr_date);
// //         graph_data.push({"x": curr_date, "y": curr_price});
// //       }
// //       var myChart = new Chart(ctx, {
// //           type: 'line',
// //           data: {
// //             lineColor: "#fffbfa",
// //               labels: time,
// //               datasets: [{
// //                   lineTension: 0,
// //                   fill: false,
// //                   borderWidth: 3,
// //                   borderColor: "#84b082",
// //                   // borderColor: "rgba(0, 0, 0, 0.3)",
// //                   label: 'Prices',
// //                   data: graph_data,
// //                   backgroundColor: "rgba(0, 0, 0, 0.3)"
// //               }]
// //           },
// //           options: {
// //               legend: {
// //                   display: false
// //               },
// //               scales: {
// //                   yAxes: [{
// //                       ticks: {
// //                           beginAtZero: true
// //                       },
// //                       scaleLabel: {
// //                           display: true,
// //                           labelString: 'Price',
// //                           fontSize: 16
// //                       }
// //                   }],
// //                   xAxes: [{
// //                       scaleLabel: {
// //                           display: true,
// //                           labelString: 'Date',
// //                           fontSize: 16
// //                       },
// //                       type: 'time',
// //                       time: {
// //                         unit: 'hour',
// //                         unitStepSize: 2,
// //                         displayFormats: {
// //                           'hour': 'MM/DD/YY h:00 a',
// //                         },
// //                         distribution: 'linear'
// //                     }
// //                   }]
// //               },
// //           }
// //       });
// //     },
// //     error: function(data) {
// //     },
// //    })
// // });

// var price_data = {};
// var time = [];
// for(price in all_prices){
//   var curr_name = all_prices[price]["fields"]["Token"];
//   var curr_date = new Date(all_prices[price]["fields"]["Time"]);
//   var curr_price = all_prices[price]["fields"]["Price"];
//   time.push(curr_date);
//   if (curr_name in price_data){
//     price_data[curr_name].push({"x": curr_date, "y": curr_price});
//   }
//   else{
//     price_data[curr_name]= [{"x": curr_date, "y": curr_price}];
//   }
// }

// var ctx2 = document.getElementById('all_chart').getContext('2d');
// window.allChart = new Chart(ctx2, {
//     type: 'line',
//     data: {
//       lineColor: "#fffbfa",
//       labels: time,
//       datasets: [],
//     },
//     options: {
//         tooltips: {
//           mode: 'point'
//         },
//         legend: {
//             display: false
//         },
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 },
//                 scaleLabel: {
//                     display: true,
//                     labelString: 'Price',
//                     fontSize: 16
//                 }
//             }],
//             xAxes: [{
//                 scaleLabel: {
//                     display: true,
//                     labelString: 'Date',
//                     fontSize: 16
//                 },
//                 type: 'time',
//                 time: {
//                   unit: 'hour',
//                   unitStepSize: 6,
//                   displayFormats: {
//                     'hour': 'MM/DD/YY h:00 a',
//                   },
//                   distribution: 'linear'
//               }
//             }]
//         },

//     }
// });

// populate_data();

// $('#checkbox-form-id').change(function(){
//   populate_data();
// });

// function populate_data(){
//   allChart.data.datasets = [];
//   for (var name in price_data) {
//       var checkbox_html = document.getElementById("check_"+ name);
//       var class_name = document.getElementById("label_"+name).innerHTML;
//       if(checkbox_html.checked){
//         var red = Math.floor(Math.random() * Math.floor(256));
//         var green = Math.floor(Math.random() * Math.floor(256));
//         var blue = Math.floor(Math.random() * Math.floor(256));
//         document.getElementById("label_"+name).setAttribute("style", "color:rgb(" + red + ", " + green + ", " + blue + ")");
//         if (price_data.hasOwnProperty(name)) {
//           allChart.data.datasets.push({
//               lineTension: 0,
//               fill: false,
//               borderWidth: 3,
//               borderColor: "rgba(" + red + ", " + green + ", " + blue + ", " + "0.3)",
//               label: class_name,
//               data: price_data[name],
//               backgroundColor: "rgba(" + red + ", " + green + ", " + blue + ", " + "0.7)",
//           });
//         }
//       }
//   }
//   window.allChart.update();
// }
