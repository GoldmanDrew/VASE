Chart.defaults.global.defaultFontColor = '#fffbfa'


document.getElementById('checkbox-list').setAttribute("style","height:"+(document.getElementById('all_chart').offsetHeight-20));
window.onresize = resize_scroll;
function resize_scroll(e) {
  document.getElementById('checkbox-list').setAttribute("style","height:"+(document.getElementById('all_chart').offsetHeight-20));
}

$('#class-modal').on('shown.bs.modal', function (event) {
  var button = event.relatedTarget;
  var classname = button.id;
  document.getElementById("modal-label").innerHTML = classname;
  $.ajax({
    type:"GET",
    url: "/class/get_prices",
    data:{"class":button.id},
    dataType: 'json',
    success: function(data){
      var ctx = document.getElementById('myChart').getContext('2d');
      var graph_data = [];
      var time = [];
      for(price in data){
        var curr_date = new Date(data[price]["fields"]["Time"]);
        var curr_price = data[price]["fields"]["Price"];
        time.push(curr_date);
        graph_data.push({"x": curr_date, "y": curr_price});
      }
      var myChart = new Chart(ctx, {
          type: 'line',
          data: {
            lineColor: "#fffbfa",
              labels: time,
              datasets: [{
                  lineTension: 0,
                  fill: false,
                  borderWidth: 3,
                  // borderColor: #fffbfa;
                  borderColor: "rgba(0, 0, 0, 0.3)",
                  label: 'Prices',
                  data: graph_data,
                  backgroundColor: "rgba(0, 0, 0, 0.3)"
              }]
          },
          options: {
              legend: {
                  display: false
              },
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      },
                      scaleLabel: {
                          display: true,
                          labelString: 'Price',
                          fontSize: 16
                      }
                  }],
                  xAxes: [{
                      scaleLabel: {
                          display: true,
                          labelString: 'Date',
                          fontSize: 16
                      },
                      type: 'time',
                      time: {
                        unit: 'hour',
                        unitStepSize: 2,
                        displayFormats: {
                          'hour': 'MM/DD/YY h:00 a',
                        },
                        distribution: 'linear'
                    }
                  }]
              },
          }
      });
    },
    error: function(data) {
    },
   })
});

var price_data = {};
var time = [];
for(price in all_prices){
  var curr_name = all_prices[price]["fields"]["OrderBookName"];
  var curr_date = new Date(all_prices[price]["fields"]["Time"]);
  var curr_price = all_prices[price]["fields"]["Price"];
  time.push(curr_date);
  if (curr_name in price_data){
    price_data[curr_name].push({"x": curr_date, "y": curr_price});
  }
  else{
    price_data[curr_name]= [{"x": curr_date, "y": curr_price}];
  }
}

var ctx2 = document.getElementById('all_chart').getContext('2d');
window.allChart = new Chart(ctx2, {
    type: 'line',
    data: {
      lineColor: "#fffbfa",
      labels: time,
      datasets: [],
    },
    options: {
        tooltips: {
          mode: 'point'
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Price',
                    fontSize: 16
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Date',
                    fontSize: 16
                },
                type: 'time',
                time: {
                  unit: 'hour',
                  unitStepSize: 6,
                  displayFormats: {
                    'hour': 'MM/DD/YY h:00 a',
                  },
                  distribution: 'linear'
              }
            }]
        },

    }
});

populate_data();

$('#checkbox-form-id').change(function(){
  populate_data();
});

function populate_data(){
  allChart.data.datasets = [];
  for (var ticker in price_data) {
      var checkbox_html = document.getElementById("check_"+ticker);
      var class_name = document.getElementById("label_"+ticker).innerHTML;
      if(checkbox_html.checked){
        var red = Math.floor(Math.random() * Math.floor(256));
        var green = Math.floor(Math.random() * Math.floor(256));
        var blue = Math.floor(Math.random() * Math.floor(256));
        document.getElementById("label_"+ticker).setAttribute("style", "color:rgb(" + red + ", " + green + ", " + blue + ")");
        if (price_data.hasOwnProperty(ticker)) {
          allChart.data.datasets.push({
              lineTension: 0,
              fill: false,
              borderWidth: 3,
              borderColor: "rgba(" + red + ", " + green + ", " + blue + ", " + "0.3)",
              label: class_name,
              data: price_data[ticker],
              backgroundColor: "rgba(" + red + ", " + green + ", " + blue + ", " + "0.7)",
          });
        }
      }
  }
  window.allChart.update();
}
