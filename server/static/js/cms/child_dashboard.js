console.log("js test");
// var equipmentDataUrl = "{% url 'cms:equipment_data' %}";
var $equipos = $('#equipos');
console.log($equipos);
console.log($equipos.data('url'));
$(document).ready(function () {
  var table = $('#equipos').DataTable({
    "ajax": {
      "url": "/cms/equipment-data/",  // Specify the relative URL here
      "type": "GET"
    },
    "processing": $equipos.data('processing'),
    "serverSide": $equipos.data('server-side'),
    "columns": [
      { "data": "id" },
      { "data": "equipo" },
      { "data": "marca" },
      { "data": "modelo" },
      { "data": "no_serie" },
      { "data": "servicio_ult" },
      { "data": "servicio_prox" },
      { "data": "estado" },
      { "data": "area" },
      { "data": "subarea" },
      { "data": "encargado" },
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