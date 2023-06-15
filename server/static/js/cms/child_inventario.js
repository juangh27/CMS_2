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
      { "data": "actions" },

    ],
    "order": [[1, 'asc']],
    "paging": false,
    "ordering": true,
    "info": false,
    "filter": false,
  });

  $('#equipos tbody').on('click', 'tr', function (e) {
    // Check if the click target is an edit or delete button
    if (e.target.id === 'edit-btn' || e.target.id === 'delete-btn') {
      return; // Ignore the event for edit and delete buttons
    }

    var equipmentId = table.row(this).data().id;
    console.log("tbody");
    showModal()

    // Add visual indication to the clicked row
    $(this).addClass('clicked');
  });
  // Handle edit button click event
  $(document).on('click', '#edit-btn', function (e) {
    e.preventDefault();
    var equipmentId = $(this).data('equipment-id');
    showModalajax(equipmentId);
    // Use equipmentId to perform necessary actions, such as opening the edit modal
    // You can customize this based on your modal implementation
    console.log('Edit button clicked for equipment ID:', equipmentId);
  });

  // Handle delete button click event
  $(document).on('click', '#delete-btn', function (e) {
    e.preventDefault();
    var equipmentId = $(this).data('equipment-id');
    // Use equipmentId to perform necessary actions, such as opening the delete modal
    // You can customize this based on your modal implementation
    console.log('Delete button clicked for equipment ID:', equipmentId);
  });
  $(document).on('click', '#new_equipment_btn', function (e) {
    e.preventDefault();
    var test = 0
    showModalajax(test);
    resetVisualIndication();



  });


  $('#equipos tbody').on('mouseenter', 'tr', function () {
    $(this).addClass('hover');
  }).on('mouseleave', 'tr', function () {
    $(this).removeClass('hover');
  });

  function showModalajax(equipmentId) {
    if (equipmentId == 0){
      var url = '/cms/edit-equipment/'
    }
    else {
      var url = '/cms/edit-equipment/' + equipmentId;
    }
    // var url = equipmentId ? '/cms/edit-equipment/' + equipmentId + '/' : '/cms/edit-equipment/';
    $('#btn-label').text('Guardar');
    // Make an AJAX request to fetch the form HTML from the server
    $.ajax({
      url: url,
      type: 'GET',
      success: function (response) {
        resetVisualIndication();
        if (equipmentId > 0) {
          // Editing existing equipment
          // Update the modal content, excluding the header and footer
          $('#editEquipmentModal .modal-body').html($(response).find('.modal-body').html());
          // Show the modal
          $('#editEquipmentModal').modal('show');
          $('#editEquipmentModalLabel').text('Editar Equipo');
          console.log(equipmentId );
          console.log(url);
        } else {
          $('#editEquipmentModalLabel').text('Agregar equipo');

          // Adding new equipment 
          // Create a new modal with the form HTML, excluding the header and footer
          $('#editEquipmentModal .modal-body').html($(response).find('.modal-body').html());
          $('#editEquipmentModal').modal('show');
        }
          $('#editEquipmentModal form').on('submit', function (e) {
            e.preventDefault();

            var formData = $(this).serialize();

            $.ajax({
              url: $(this).attr('action'),
              type: $(this).attr('method'),
              data: formData,
              success: function (response) {
                if (response.success) {
                  // Form submission successful
                  // Trigger table reload
                  $('#equipos').DataTable().ajax.reload();
                  $('#editEquipmentModal').modal('hide'); // Close the modal
                  // Optionally, perform other actions
                  // ...
                } else {
                  // Form submission failed
                  // Handle errors in the form
                  // ...  
                }
              },
              error: function (xhr, status, error) {
                // Handle error
                console.error(error);
              }
            });
          });
        }
      
    });
  }


  function showModal(equipmentId) {
    // Make an AJAX request or perform necessary actions to retrieve the data for the equipment
    // Populate the modal content with the retrieved data
    // Show the modal
    console.log('Modal opened for equipment ID:', equipmentId);
    // Handle modal close event
    $('#equipmentDetailsModal').modal('show');
    $('#equipmentDetailsModal').on('hidden.bs.modal', function () {
      resetVisualIndication();
    });
  }

  // Function to reset visual indication
  function resetVisualIndication() {
    $('#equipos tbody tr.clicked').removeClass('clicked');
  }
});
