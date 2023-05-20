console.log("js test");
// var equipmentDataUrl = "{% url 'cms:equipment_data' %}";
var $equipos = $('#equipos');
console.log($equipos);
console.log($equipos.data('url'));
$(document).ready(function () {
  var table = $('#equipos').DataTable({
    "ajax": "http://localhost:85"+ $equipos.data('url'),
    "processing": $equipos.data('processing'),
    "serverSide": $equipos.data('server-side'),
    "columns": [
      { "data": "id" },
      { "data": "serial_number" },
      { "data": "equipment_type" },
      { "data": "manufacturer" },
      { "data": "model" },
      { "data": "calibration_date" },
      { "data": "last_service_date" },
      { "data": "is_active" },
      { "data": "actions" },

    ],
    "order": [[1, 'asc']],
    "paging": false,
    "ordering": true,
    "info": false,
    "filter": false,
  });

  // Handle edit button click event
  $(document).on('click', '#edit-btn', function(e) {
    e.preventDefault();
    var equipmentId = $(this).data('equipment-id');
    // Use equipmentId to perform necessary actions, such as opening the edit modal
    // You can customize this based on your modal implementation
    console.log('Edit button clicked for equipment ID:', equipmentId);
  });

  // Handle delete button click event
  $(document).on('click', '#delete-btn', function(e) {
    e.preventDefault();
    var equipmentId = $(this).data('equipment-id');
    // Use equipmentId to perform necessary actions, such as opening the delete modal
    // You can customize this based on your modal implementation
    console.log('Delete button clicked for equipment ID:', equipmentId);
  });

});