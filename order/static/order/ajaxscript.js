  /*
      On submitting the form, send the POST ajax
      request to server and after successfull submission
      display the object.
  */
  // $(document).ready(function () {
  // $("#order_form").submit(function (e) {
  $(document).on("submit", "#order_form", function (e) {
    // prevent page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    // make POST ajax call
    $.ajax({
      type: 'POST',
    //   url: "{% url 'order:post_order' %}",
      url: "/order/postorder/",
      data: serializedData,
      success: function (response) {
        // clear the form
        $("#order_form").trigger('reset');
      },
      error: function (response) {
      }
    });
    $.ajax({
    //   url: "{% url 'order:your_orders' %}",
    url: "/order/yourorders/",
      success: function (response) {
        $("#YourOrdersDiv").load("/order/yourorders/");
      },
      error: function (response) {
      }
    });
    $.ajax({
    //   url: "{% url 'order:all_orders' %}",
      url: "/order/allorders/",
      success: function (response) {
        $("#AllOrdersDiv").load("/order/allorders/");
      },
      error: function (response) {
      }
    });
  });

  $(document).on("submit", "#cancel_button", function (e) {
    e.preventDefault();
    $.ajax({
      url: e.target.action,
      success: function (response) {
        $("#YourOrdersDiv").load("/order/yourorders/");
      },
      error: function (response) {
      }
    });
    $.ajax({
      url: e.target.action,
      success: function (response) {
        $("#AllOrdersDiv").load("/order/allorders/");
      },
      error: function (response) {
      }
    });
  });

  $(document).ready(function() {
   $('#acompany_dropdown').on('change', function() {
     $.ajax({
       type: 'GET',
       url: "/order/activefilter/",
       data: {"company": $("#acompany_dropdown").val()},
       success: function (data) {
         console.log(data)
         console.log("it worked!")
         $('#YourOrdersDiv').html(data)
       },
       error: function (data) {
       }
     });
   });
 });

  $(document).ready(function() {
   $('#company_dropdown').on('change', function() {
     $.ajax({
       type: 'GET',
       url: "/order/orderfilter/",
       data: {"company": $("#company_dropdown").val()},
       success: function (data) {
         $('#AllOrdersDiv').html(data)
       },
       error: function (data) {
       }
     });
   });
});
